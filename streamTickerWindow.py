import json
import sys
from tkinter import Tk, filedialog, messagebox, BooleanVar

from mainMenu import getMainMenu
from utils.helperMethods import readJSON, writeJSON

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
        self.messages = readJSON(self.messagesPath)
        self.settings = readJSON(self.settingsPath)
        self.alwaysOnTop = BooleanVar()
        self.alwaysOnTop.set(self.getOnStartup("alwaysontop", False))
        self.updateAlwaysOnTop()

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

    def clearMessages(self):
        self.messages = {}
        messagebox.showinfo("Info", "Messages cleared.")

    def loadMessages(self):
        fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load messages", filetypes=[("StreamTicker Messages", "*.stm")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.messages = readJSON(fileToLoad)
                self.messagesPath = fileToLoad
                messagebox.showinfo("Info", "Messages were loaded successfully.")
            except:
                messagebox.showerror("Error", "Failed to load messages!")

    def loadSettings(self):
        fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Load settings", filetypes=[("StreamTicker Messages", "*.sts")])
        if not fileToLoad or fileToLoad is None:
            return
        else:
            try:
                self.settings = readJSON(fileToLoad)
                self.settingsPath = fileToLoad
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
        if writeJSON(saveFile, self.settings):
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
        if writeJSON(saveFile, self.messages):
            self.messagesPath = saveFile
            messagebox.showinfo("Info", "Messages were saved successfully.")
        else:
            messagebox.showerror("Error", "Failed to save messages!")