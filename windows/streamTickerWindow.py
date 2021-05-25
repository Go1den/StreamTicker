import json
import os
import sys
import time
import urllib.request
from random import shuffle
from threading import Thread
from tkinter import Tk, filedialog, messagebox, BooleanVar, Canvas, NW, W
from tkinter.font import Font
from urllib.error import HTTPError

from PIL import Image
from PIL.ImageTk import PhotoImage

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
        self.resizable(False, False)
        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.streamTickerWindowJSON = self.getSettingsJSONOnStartup()
        self.messagesPath = self.getOnStartup("messages", "")
        self.settingsPath = self.getOnStartup("settings", "")
        self._offsetx = self.getOnStartup("offsetx", 0)
        self._offsety = self.getOnStartup("offsety", 0)
        self.geometry('+{x}+{y}'.format(x=self._offsetx, y=self._offsety))
        self.messages = self.getMessages(self.messagesPath)
        self.title("StreamTicker")
        self.currentIndex = 0
        self.xCoord = 0
        self.yCoord = 0
        self.yCoord2 = 0
        self.images = []
        self.settings = self.getSettings(self.settingsPath)
        self.alwaysOnTop = BooleanVar()
        self.alwaysOnTop.set(self.getOnStartup("alwaysontop", False))
        self.iconbitmap('imagefiles/stIcon.ico')
        self.updateAlwaysOnTop()
        self.shufflePool = []

        self.canvas = Canvas(self, width=self.settings.windowSettings.width, height=self.settings.windowSettings.height, bd=0, highlightthickness=0,
                             background=self.settings.windowSettings.bgColor)
        self.canvas.bind('<Button-3>', self.rightClickMenu)

        try:
            self.bgImage = PhotoImage(file=self.settings.windowSettings.bgImage)
        except Exception:
            self.bgImage = None
        self.canvas.create_image(0, 0, anchor=NW, image=self.bgImage)

        self.canvas.grid(row=0, column=0)
        self.updateCurrentDirectoryInUpdaterSettings()
        self.after(1000, self.checkForUpdates)
        self.thread = Thread(target=self.displayThread, daemon=True).start()
        self.mainloop()

    def updateCurrentDirectoryInUpdaterSettings(self):
        updaterSettings = readJSON("updater/updaterSettings.cfg")
        updaterSettings["destinationDirectory"] = os.getcwd()
        writeJSON("updater/updaterSettings.cfg", updaterSettings)

    def displayThread(self):
        while True:
            self.displayNextMessage()

    def getNextShuffledMessage(self):
        if len(self.messages) == 0:
            return 0
        if not self.shufflePool:
            self.shufflePool = list(range(len(self.messages)))
            shuffle(self.shufflePool)
        candidate = self.shufflePool.pop()
        # do this check because scared of going out of bounds if a message gets removed after shuffle gets turned on
        if candidate >= len(self.messages):
            candidate = 0
        return candidate

    def displayNextMessage(self):
        try:
            currentMessage = self.messages[self.currentIndex]
        except IndexError:
            self.clearCanvasAndResetVariables(5)
            self.displayNextMessage()
        fontFamily = currentMessage.overrides.font if currentMessage.overrides.font else self.settings.messageSettings.fontFace
        fontSize = currentMessage.overrides.fontSize if currentMessage.overrides.fontSize else self.settings.messageSettings.fontSize
        fontColor = currentMessage.overrides.fontColor if currentMessage.overrides.fontColor else self.settings.messageSettings.color
        bold = currentMessage.overrides.bold if currentMessage.overrides.bold else self.settings.messageSettings.bold
        bold = "bold" if bold else "normal"
        italic = currentMessage.overrides.italic if currentMessage.overrides.italic else self.settings.messageSettings.italic
        italic = "italic" if italic else "roman"
        overstrike = currentMessage.overrides.overstrike if currentMessage.overrides.overstrike else self.settings.messageSettings.overstrike
        overstrike = 1 if overstrike else 0
        alignment = currentMessage.overrides.alignment if currentMessage.overrides.alignment else self.settings.messageSettings.alignment
        duration = float(currentMessage.overrides.duration) if currentMessage.overrides.duration else float(self.settings.messageSettings.duration)
        intermission = float(currentMessage.overrides.intermission) if currentMessage.overrides.intermission else float(self.settings.messageSettings.intermission)
        scrollSpeed = getScrollSpeedFloat(currentMessage.overrides.scrollSpeed) if currentMessage.overrides.scrollSpeed else getScrollSpeedFloat(
            self.settings.windowSettings.moveAllOnLineDelay)
        arrival = currentMessage.overrides.arrival if currentMessage.overrides.arrival else self.settings.messageSettings.arrival
        if arrival == "Pick For Me":
            arrival = pickArrival(italic)
        departure = currentMessage.overrides.departure if currentMessage.overrides.departure else self.settings.messageSettings.departure
        if departure == "Pick For Me":
            departure = pickDeparture(italic)
        font = Font(family=fontFamily, size=fontSize, weight=bold, overstrike=overstrike, slant=italic)
        width, height = getWidthAndHeight(currentMessage, self.settings, font)
        self.xCoord, self.yCoord, self.yCoord2 = getStartingXYCoordinates(width, height, arrival, self.settings, alignment)
        self.setupCanvas(arrival, currentMessage, font, fontColor)
        selectArrivalAnimation(self.canvas, self.settings, arrival, height, scrollSpeed, width, alignment)
        time.sleep(duration)
        selectDepartureAnimation(self.canvas, self.settings, departure, height, scrollSpeed, width, alignment)
        self.clearCanvasAndResetVariables(intermission)

    def clearCanvasAndResetVariables(self, intermission):
        self.canvas.delete("currentMessage")
        self.images = []
        self.xCoord = 0
        self.yCoord = 0
        if len(self.messages) > 0:
            if self.settings.windowSettings.shuffle:
                self.currentIndex = self.getNextShuffledMessage()
            else:
                self.currentIndex = (self.currentIndex + 1) % len(self.messages)
        else:
            self.currentIndex = 0
        time.sleep(intermission)

    def setupCanvas(self, arrival: str, currentMessage: Message, font: Font, fontColor: str):
        for part in sorted(currentMessage.parts, key=lambda x: x.sortOrder):
            if part.partType == "Pixel Gap":
                self.xCoord += int(part.value)
            elif part.partType == "Text":
                for char in part.value:
                    self.canvas.create_text(self.xCoord, self.yCoord, fill=fontColor, text=char, font=font, tags="currentMessage", anchor=W)
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2]
                    self.swapYCoords(arrival)
            elif part.partType == "Text From File":
                fileText = readFile(part.value)
                for char in fileText:
                    self.canvas.create_text(self.xCoord, self.yCoord, fill=fontColor, text=char, font=font, tags="currentMessage", anchor=W)
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2]
                    self.swapYCoords(arrival)
            elif part.partType == "Image":
                try:
                    img = PhotoImage(Image.open(part.value))
                    self.images.append(img)
                    self.canvas.create_image(self.xCoord, self.yCoord, image=img, anchor=W, tags="currentMessage")
                    box = self.canvas.bbox(self.canvas.find_withtag("currentMessage")[-1])
                    self.xCoord = box[2]
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

            overrides = message.get("overrides", {})
            override = Override(overrides.get("duration", ""),
                                overrides.get("intermission", ""),
                                overrides.get("scrollSpeed", ""),
                                overrides.get("font", ""),
                                overrides.get("fontSize", ""),
                                overrides.get("fontColor", ""),
                                overrides.get("arrival", ""),
                                overrides.get("departure", ""),
                                overrides.get("bold", False),
                                overrides.get("italic", False),
                                overrides.get("overstrike", False))
            messages.append(Message(nickname, sortOrder, parts, override))
        return messages

    def getSettings(self, path) -> Settings:
        s = readJSON(path)
        w = s.get("windowSettings", {})
        windowSettings = WindowSettings(w.get('moveAllOnLineDelay', "99"),
                                        w.get('bgImage', "imagefiles/background.png"),
                                        w.get('width', "400"),
                                        w.get('height', "44"),
                                        w.get('bgColor', "#000000"),
                                        w.get('shuffle', False))

        m = s.get("messageSettings", {})
        messageSettings = MessageSettings(m.get('color', "#ffffff"),
                                          m.get('fontFace', "Courier New"),
                                          m.get('intermission', ".5"),
                                          m.get('fontSize', "26"),
                                          m.get('duration', "10"),
                                          m.get('arrival', "Pick For Me"),
                                          m.get('departure', "Pick For Me"),
                                          m.get('bold', False),
                                          m.get('italic', False),
                                          m.get('overstrike', False),
                                          m.get('alignment', "Left"))
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
        fileToLoad = filedialog.askopenfilename(initialdir=os.getcwd() + "/messages", title="Load messages", filetypes=[("StreamTicker Messages", "*.stm")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.messages = self.getMessages(fileToLoad)
                self.messagesPath = fileToLoad
                messagebox.showinfo("Info", "Messages were loaded successfully.", parent=self)
            except:
                messagebox.showerror("Error", "Failed to load messages!", parent=self)

    def checkForUpdates(self):
        currentVersion = "2.0.8"
        try:
            f = urllib.request.urlopen('https://www.go1den.com/streamtickerversion/version.txt')
            if not currentVersion == str(f.read().decode()) and messagebox.askyesno("New Version Available",
                                                                                    "A new version of StreamTicker is available. You can run the updater.exe script while StreamTicker is closed to update. Would you like to close StreamTicker now?",
                                                                                    parent=self):
                self.updateStreamTicker()
        except HTTPError:
            messagebox.showerror("Error", "Failed to update. You may need to download the new version manually.", parent=self)

    def updateStreamTicker(self):
        # This is not compatible with Mac or Linux
        os.startfile(os.getcwd() + "/updater")
        exit(0)

    def loadDefaultSettings(self):
        if messagebox.askokcancel("Restore Default Settings", "Are you sure you want to restore the default settings for StreamTicker?", parent=self):
            self.settings = Settings()
            self.applyCurrentWindowSettings()

    def loadDefaultMessages(self):
        if messagebox.askokcancel("Restore Default Messages", "Are you sure you want to restore the default messages for StreamTicker?", parent=self):
            self.messages = [Message("StreamTicker", 1, [MessagePart("Pixel Gap", 1, "8"),
                                                         MessagePart("Image", 2, "imagefiles/stLogo28.png"),
                                                         MessagePart("Pixel Gap", 3, "8"),
                                                         MessagePart("Text", 4, "StreamTicker")]),
                             Message("StreamTicker", 2, [MessagePart("Pixel Gap", 1, "8"),
                                                         MessagePart("Image", 2, "imagefiles/stLogo28.png"),
                                                         MessagePart("Pixel Gap", 3, "8"),
                                                         MessagePart("Text", 4, "Made by Go1den")])]

    def loadSettings(self):
        fileToLoad = filedialog.askopenfilename(initialdir=os.getcwd() + "/settings", title="Load settings", filetypes=[("StreamTicker Messages", "*.sts")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.settings = self.getSettings(fileToLoad)
                self.settingsPath = fileToLoad
                self.applyCurrentWindowSettings()
                messagebox.showinfo("Info", "Settings were loaded successfully.", parent=self)
            except:
                messagebox.showerror("Error", "Failed to load settings!", parent=self)

    def saveSettings(self, saveAs):
        if self.settingsPath == "" or saveAs:
            saveFile = filedialog.asksaveasfilename(initialdir=os.getcwd() + "/settings", title="Save as...", filetypes=[("StreamTicker Settings", "*.sts")],
                                                    defaultextension='.sts')
        else:
            saveFile = self.settingsPath
        if not saveFile or saveFile is None:
            return
        if writeSettingsToJSON(saveFile, self.settings):
            self.settingsPath = saveFile
            messagebox.showinfo("Info", "Settings were saved successfully.", parent=self)
        else:
            messagebox.showerror("Error", "Failed to save settings!", parent=self)

    def saveMessages(self, saveAs):
        if self.messagesPath == "" or saveAs:
            saveFile = filedialog.asksaveasfilename(initialdir=os.getcwd() + "/messages", title="Save as...", filetypes=[("StreamTicker Messages", "*.stm")],
                                                    defaultextension='.stm')
        else:
            saveFile = self.messagesPath
        if not saveFile or saveFile is None:
            return
        if writeMessagesToJSON(saveFile, self.messages):
            self.messagesPath = saveFile
            messagebox.showinfo("Info", "Messages were saved successfully.", parent=self)
        else:
            messagebox.showerror("Error", "Failed to save messages!", parent=self)

    def applyCurrentWindowSettings(self):
        self.canvas.delete("all")
        self.canvas.configure(width=self.settings.windowSettings.width, height=self.settings.windowSettings.height, background=self.settings.windowSettings.bgColor)
        try:
            self.bgImage = PhotoImage(file=self.settings.windowSettings.bgImage)
        except Exception:
            self.bgImage = None
        self.canvas.create_image(0, 0, anchor=NW, image=self.bgImage)

    def closeWindow(self):
        self.streamTickerWindowJSON["messages"] = self.messagesPath
        self.streamTickerWindowJSON["settings"] = self.settingsPath
        self.streamTickerWindowJSON["offsetx"] = self.winfo_x()
        self.streamTickerWindowJSON["offsety"] = self.winfo_y()
        self.streamTickerWindowJSON["alwaysontop"] = self.alwaysOnTop.get()
        writeJSON("settings.cfg", self.streamTickerWindowJSON)
        sys.exit(1)
