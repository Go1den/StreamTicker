from tkinter import StringVar, messagebox

from utils import helperMethods

class SettingsGUIFields:
    def __init__(self):
        self.VAR_MESSAGE_STYLE = StringVar()
        self.VAR_ENTRY_MESSAGE_DURATION = StringVar()
        self.VAR_ENTRY_MESSAGE_INTERMISSION = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_TEXT = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = ""
        self.VAR_FONT_COMBO_BOX = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE = StringVar()
        self.VAR_ARRIVAL = StringVar()
        self.VAR_DEPARTURE = StringVar()

        self.VAR_WINDOW_WIDTH = StringVar()
        self.VAR_WINDOW_HEIGHT = StringVar()
        self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = ""
        self.VAR_LABEL_WINDOW_BG_COLOR_TEXT = StringVar()
        self.VAR_DISPLAY_WINDOW_BG_IMAGE = StringVar()
        self.VAR_PATH_WINDOW_BG_IMAGE = StringVar()
        self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY = StringVar()
        self.getDefaultValues(False)

    def getDefaultValues(self, confirm, mFrame=None, bgFrame=None):
        if not confirm or messagebox.askokcancel("Confirm New Settings", "All changes made will be lost, and the default values will be set. Do you want to continue?"):
            self.VAR_MESSAGE_STYLE.set("")
            self.VAR_ENTRY_MESSAGE_DURATION.set("5")
            self.VAR_ENTRY_MESSAGE_INTERMISSION.set("0.5")
            self.VAR_LABEL_MESSAGE_COLOR_TEXT.set("#ffffff")
            self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = "#ffffff"
            self.VAR_FONT_COMBO_BOX.set("Courier New")
            self.VAR_ENTRY_NORMAL_FONT_SIZE.set("26")
            self.VAR_ARRIVAL.set("Pick For Me")
            self.VAR_DEPARTURE.set("Pick For Me")

            self.VAR_WINDOW_WIDTH.set("400")
            self.VAR_WINDOW_HEIGHT.set("44")
            self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = "#000000"
            self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set("#000000")
            self.VAR_PATH_WINDOW_BG_IMAGE.set("imagefiles/background.png")
            self.VAR_DISPLAY_WINDOW_BG_IMAGE.set("background1.png")
            self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set("Fast")
            if mFrame and bgFrame:
                self.updateColorBoxes(mFrame, bgFrame)

    def loadSettings(self, parent, mFrame, bgFrame):
        # Todo: backup the current settings so that if load fails, we can revert to those rather than doing a partial load
        try:
            s = parent.settings
            if s.get("message"):
                m = s.get("message")
                self.VAR_MESSAGE_STYLE.set(m.get("MESSAGE_STYLE"))
                self.VAR_ENTRY_MESSAGE_DURATION.set(m.get("MESSAGE_DURATION"))
                self.VAR_ENTRY_MESSAGE_INTERMISSION.set(m.get("MESSAGE_INTERMISSION"))
                self.VAR_LABEL_MESSAGE_COLOR_TEXT.set(m.get("MESSAGE_COLOR"))
                self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = m.get("MESSAGE_COLOR")
                self.VAR_FONT_COMBO_BOX.set(m.get("MESSAGE_FONT_FACE"))
                self.VAR_ENTRY_NORMAL_FONT_SIZE.set(m.get("NORMAL_FONT_SIZE"))
                self.VAR_ARRIVAL.set(m.get("ARRIVAL"))
                self.VAR_DEPARTURE.set(m.get("DEPARTURE"))

            if s.get("window"):
                w = s.get("window")
                self.VAR_WINDOW_WIDTH.set(w.get("WINDOW_WIDTH"))
                self.VAR_WINDOW_HEIGHT.set(w.get("WINDOW_HEIGHT"))
                self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(w.get("WINDOW_BG_COLOR"))
                self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = w.get("WINDOW_BG_COLOR")
                self.VAR_PATH_WINDOW_BG_IMAGE.set(w.get("WINDOW_BG_IMAGE"))
                self.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(w.get("WINDOW_BG_IMAGE")))
                self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(w.get("MOVE_ALL_ON_LINE_DELAY"))
                self.updateColorBoxes(mFrame, bgFrame)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Unable to load file. Please select a valid layout file.")

    def updateColorBoxes(self, mFrame, bgFrame):
        bgFrame.CANVAS_WINDOW_BG_IMAGE.itemconfig(bgFrame.RECTANGLE_WINDOW_BG_IMAGE, fill=self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)
        mFrame.CANVAS_MESSAGE_COLOR.itemconfig(mFrame.RECTANGLE_MESSAGE_COLOR, fill=self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
