import json
import sys
import time
from threading import Thread
from tkinter import Tk, filedialog, messagebox, BooleanVar, Canvas, PhotoImage, NW, W

from menus.mainMenu import getMainMenu
from objects.message import Message
from objects.messagePart import MessagePart
from objects.messageSettings import MessageSettings
from objects.override import Override
from objects.settings import Settings
from objects.windowSettings import WindowSettings
from utils.arrivalAnimations import getWidthAndHeight, getStartingXYCoordinates, pickArrival, selectArrivalAnimation
from utils.departureAnimations import selectDepartureAnimation, pickDeparture
from utils.helperMethods import readJSON, writeJSON, writeSettingsToJSON, writeMessagesToJSON, readFile, getScrollSpeedFloat

class StreamTickerWindow(Tk):

    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.overrideredirect(True)
        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.streamTickerWindowJSON = self.getSettingsJSONOnStartup()
        self.messagesPath = self.getOnStartup("messages", "")
        self.settingsPath = self.getOnStartup("settings", "")
        self._offsetx = self.getOnStartup("offsetx", 0)
        self._offsety = self.getOnStartup("offsety", 0)
        self.geometry('+{x}+{y}'.format(x=self._offsetx, y=self._offsety))
        self.messages = self.getMessages(self.messagesPath)
        self.currentIndex = 0
        self.xCoord = 0
        self.yCoord = 0
        self.yCoord2 = 0
        self.images = []
        self.settings = self.getSettings(self.settingsPath)
        self.alwaysOnTop = BooleanVar()
        self.alwaysOnTop.set(self.getOnStartup("alwaysontop", False))
        self.iconbitmap('stIcon.ico')
        self.updateAlwaysOnTop()

        self.canvas = Canvas(self, width=self.settings.windowSettings.width, height=self.settings.windowSettings.height, bd=0, highlightthickness=0,
                             background=self.settings.windowSettings.bgColor)
        self.canvas.bind('<Button-3>', self.rightClickMenu)

        self.bgImage = PhotoImage(file=self.settings.windowSettings.bgImage)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bgImage)

        self.canvas.grid(row=0, column=0)

        Thread(target=self.displayNextMessage, daemon=True).start()
        self.mainloop()

    def displayNextMessage(self):
        currentMessage = self.messages[self.currentIndex]
        font = currentMessage.overrides.font if currentMessage.overrides.font else self.settings.messageSettings.fontFace
        fontSize = currentMessage.overrides.fontSize if currentMessage.overrides.fontSize else self.settings.messageSettings.fontSize
        fontColor = currentMessage.overrides.fontColor if currentMessage.overrides.fontColor else self.settings.messageSettings.color
        duration = float(currentMessage.overrides.duration) if currentMessage.overrides.duration else float(self.settings.messageSettings.duration)
        intermission = float(currentMessage.overrides.intermission) if currentMessage.overrides.intermission else float(self.settings.messageSettings.intermission)
        scrollSpeed = getScrollSpeedFloat(currentMessage.overrides.scrollSpeed) if currentMessage.overrides.scrollSpeed else getScrollSpeedFloat(
            self.settings.windowSettings.moveAllOnLineDelay)
        arrival = currentMessage.overrides.arrival if currentMessage.overrides.arrival else self.settings.messageSettings.arrival
        if arrival == "Pick For Me":
            arrival = pickArrival()
        departure = currentMessage.overrides.departure if currentMessage.overrides.departure else self.settings.messageSettings.departure
        if departure == "Pick For Me":
            departure = pickDeparture()
        width, height = getWidthAndHeight(currentMessage, self.settings)
        self.xCoord, self.yCoord, self.yCoord2 = getStartingXYCoordinates(width, height, arrival, self.settings)
        self.setupCanvas(arrival, currentMessage, font, fontColor, fontSize)
        selectArrivalAnimation(self.canvas, self.settings, self.yCoord, self.yCoord2, arrival, height, scrollSpeed, width)
        time.sleep(duration)
        selectDepartureAnimation(self.canvas, self.settings, departure, height, scrollSpeed, width)
        self.clearCanvasAndResetVariables(intermission)
        self.displayNextMessage()

    def clearCanvasAndResetVariables(self, intermission):
        self.canvas.delete("currentMessage")
        self.images = []
        self.xCoord = 0
        self.yCoord = 0
        self.currentIndex = (self.currentIndex + 1) % len(self.messages)
        time.sleep(intermission)

    def setupCanvas(self, arrival: str, currentMessage: Message, font: str, fontColor: str, fontSize: str):
        for part in sorted(currentMessage.parts, key=lambda x: x.sortOrder):
            if part.partType == "Pixel Gap":
                self.xCoord += int(part.value)
            elif part.partType == "Text":
                for char in part.value:
                    # TODO add font style option instead of bold
                    self.canvas.create_text(self.xCoord, self.yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="currentMessage", anchor=W)
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
                    self.swapYCoords(arrival)
            elif part.partType == "Text From File":
                fileText = readFile(part.value)
                for char in fileText:
                    # TODO add font style option instead of bold
                    self.canvas.create_text(self.xCoord, self.yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="currentMessage", anchor=W)
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
                    self.swapYCoords(arrival)
            elif part.partType == "Image":
                try:
                    img = PhotoImage(file=part.value)
                    self.images.append(img)
                    self.canvas.create_image(self.xCoord, self.yCoord, image=img, anchor=W, tags="currentMessage")
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2] - 1
                    self.swapYCoords(arrival)
                except Exception as e:
                    print("Error loading image: " + str(e))

    def swapYCoords(self, arrival: str):
        if arrival == "Zip Forward" or arrival == "Zip Backward" or arrival == "Zip Randomly":
            tmp = self.yCoord2
            self.yCoord2 = self.yCoord
            self.yCoord = tmp

    def getMessages(self, path) -> list[Message]:
        messagesAsJSON = readJSON(path)
        messages = []
        for message in messagesAsJSON:
            sortOrder = message["sortOrder"]
            nickname = message["nickname"]
            parts = []
            for part in message["parts"]:
                partType = part["partType"]
                partSortOrder = part["sortOrder"]
                partValue = part["value"]
                parts.append(MessagePart(partType, partSortOrder, partValue))

            overrides = message["overrides"]
            override = Override(overrides["duration"], overrides["intermission"], overrides["scrollSpeed"], overrides["font"],
                                overrides["fontSize"], overrides["fontColor"], overrides["arrival"], overrides["departure"])
            messages.append(Message(nickname, sortOrder, parts, override))
        return messages

    def getSettings(self, path) -> Settings:
        s = readJSON(path)
        w = s["windowSettings"]
        windowSettings = WindowSettings(w['moveAllOnLineDelay'], w['bgImage'], w['width'], w['height'], w['bgColor'])
        m = s["messageSettings"]
        messageSettings = MessageSettings(m['style'], m['color'], m['fontFace'], m['intermission'], m['fontSize'], m['duration'],
                                          m['arrival'], m['departure'])
        return Settings(windowSettings, messageSettings)

    def updateAlwaysOnTop(self):
        if self.alwaysOnTop.get():
            self.wm_attributes("-topmost", 1)
        else:
            self.wm_attributes("-topmost", 0)

    def dragwin(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def rightClickMenu(self, e):
        getMainMenu(self, e)

    def getSettingsJSONOnStartup(self):
        try:
            with open("settings.cfg", "r") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading settings on startup: " + str(e))
            return {"messages": "", "settings": ""}

    def getOnStartup(self, key, default):
        val = self.streamTickerWindowJSON.get(key)
        if val:
            return val
        else:
            return default

    def loadMessages(self):
        fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load messages", filetypes=[("StreamTicker Messages", "*.stm")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.messages = self.getMessages(fileToLoad)
                self.messagesPath = fileToLoad
                messagebox.showinfo("Info", "Messages were loaded successfully.")
            except:
                messagebox.showerror("Error", "Failed to load messages!")

    def loadDefaultSettings(self):
        if messagebox.askokcancel("Restore Default Settings", "Are you sure you want to restore the default settings for StreamTicker?"):
            self.settings = Settings()
            self.applyCurrentWindowSettings()

    def loadDefaultMessages(self):
        if messagebox.askokcancel("Restore Default Messages", "Are you sure you want to restore the default messages for StreamTicker?"):
            self.messages = [Message("StreamTicker", 1, [MessagePart("Pixel Gap", 1, "8"),
                                                         MessagePart("Image", 2, "imagefiles/stLogo28.png"),
                                                         MessagePart("Pixel Gap", 3, "8"),
                                                         MessagePart("Text", 4, "StreamTicker")])]

    def loadSettings(self):
        fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load settings", filetypes=[("StreamTicker Messages", "*.sts")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.settings = self.getSettings(fileToLoad)
                self.settingsPath = fileToLoad
                self.applyCurrentWindowSettings()
                messagebox.showinfo("Info", "Settings were loaded successfully.")
            except:
                messagebox.showerror("Error", "Failed to load settings!")

    def saveSettings(self, saveAs):
        if self.settingsPath == "" or saveAs:
            saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("StreamTicker Settings", "*.sts")], defaultextension='.sts')
        else:
            saveFile = self.settingsPath
        if not saveFile or saveFile is None:
            return
        if writeSettingsToJSON(saveFile, self.settings):
            self.settingsPath = saveFile
            messagebox.showinfo("Info", "Settings were saved successfully.")
        else:
            messagebox.showerror("Error", "Failed to save settings!")

    def saveMessages(self, saveAs):
        if self.messagesPath == "" or saveAs:
            saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("StreamTicker Messages", "*.stm")], defaultextension='.stm')
        else:
            saveFile = self.messagesPath
        if not saveFile or saveFile is None:
            return
        if writeMessagesToJSON(saveFile, self.messages):
            self.messagesPath = saveFile
            messagebox.showinfo("Info", "Messages were saved successfully.")
        else:
            messagebox.showerror("Error", "Failed to save messages!")

    def applyCurrentWindowSettings(self):
        self.canvas.delete("all")
        self.canvas.configure(width=self.settings.windowSettings.width, height=self.settings.windowSettings.height, background=self.settings.windowSettings.bgColor)
        self.bgImage = PhotoImage(file=self.settings.windowSettings.bgImage)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bgImage)

    def closeWindow(self):
        self.streamTickerWindowJSON["messages"] = self.messagesPath
        self.streamTickerWindowJSON["settings"] = self.settingsPath
        self.streamTickerWindowJSON["offsetx"] = self.winfo_x()
        self.streamTickerWindowJSON["offsety"] = self.winfo_y()
        self.streamTickerWindowJSON["alwaysontop"] = self.alwaysOnTop.get()
        writeJSON("settings.cfg", self.streamTickerWindowJSON)
        sys.exit(1)
