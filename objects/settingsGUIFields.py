from tkinter import StringVar, messagebox, BooleanVar

from utils import helperMethods

class SettingsGUIFields:
    def __init__(self):
        self.VAR_ENTRY_MESSAGE_DURATION = StringVar()
        self.VAR_ENTRY_MESSAGE_INTERMISSION = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_TEXT = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = ""
        self.VAR_FONT_COMBO_BOX = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE = StringVar()
        self.VAR_ARRIVAL = StringVar()
        self.VAR_DEPARTURE = StringVar()
        self.VAR_FONT_IS_BOLD = BooleanVar()
        self.VAR_FONT_IS_ITALIC = BooleanVar()
        self.VAR_FONT_IS_OVERSTRIKE = BooleanVar()
        self.VAR_ALIGNMENT = StringVar()

        self.VAR_WINDOW_WIDTH = StringVar()
        self.VAR_WINDOW_HEIGHT = StringVar()
        self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = ""
        self.VAR_LABEL_WINDOW_BG_COLOR_TEXT = StringVar()
        self.VAR_DISPLAY_WINDOW_BG_IMAGE = StringVar()
        self.VAR_PATH_WINDOW_BG_IMAGE = StringVar()
        self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY = StringVar()
        self.VAR_MESSAGE_SHUFFLE = BooleanVar()
        self.getDefaultValues()

    def getDefaultValues(self, mFrame=None, bgFrame=None):
        self.VAR_ENTRY_MESSAGE_DURATION.set("5")
        self.VAR_ENTRY_MESSAGE_INTERMISSION.set("0.5")
        self.VAR_LABEL_MESSAGE_COLOR_TEXT.set("#ffffff")
        self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = "#ffffff"
        self.VAR_FONT_COMBO_BOX.set("Courier New")
        self.VAR_ENTRY_NORMAL_FONT_SIZE.set("26")
        self.VAR_ARRIVAL.set("Pick For Me")
        self.VAR_DEPARTURE.set("Pick For Me")
        self.VAR_FONT_IS_BOLD.set(False)
        self.VAR_FONT_IS_ITALIC.set(False)
        self.VAR_FONT_IS_OVERSTRIKE.set(False)
        self.VAR_ALIGNMENT.set("Left")

        self.VAR_WINDOW_WIDTH.set("400")
        self.VAR_WINDOW_HEIGHT.set("44")
        self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = "#000000"
        self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set("#000000")
        self.VAR_PATH_WINDOW_BG_IMAGE.set("imagefiles/background.png")
        self.VAR_DISPLAY_WINDOW_BG_IMAGE.set("background.png")
        self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set("99")
        self.VAR_MESSAGE_SHUFFLE.set(False)
        if mFrame and bgFrame:
            self.updateColorBoxes(mFrame, bgFrame)

    def loadSettings(self, master, parent, mFrame, bgFrame):
        try:
            s = parent.settings
            if s.messageSettings:
                m = s.messageSettings
                self.VAR_ENTRY_MESSAGE_DURATION.set(m.duration)
                self.VAR_ENTRY_MESSAGE_INTERMISSION.set(m.intermission)
                self.VAR_LABEL_MESSAGE_COLOR_TEXT.set(m.color)
                self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = m.color
                self.VAR_FONT_COMBO_BOX.set(m.fontFace)
                self.VAR_ENTRY_NORMAL_FONT_SIZE.set(m.fontSize)
                self.VAR_ARRIVAL.set(m.arrival)
                self.VAR_DEPARTURE.set(m.departure)
                self.VAR_FONT_IS_BOLD.set(m.bold)
                self.VAR_FONT_IS_ITALIC.set(m.italic)
                self.VAR_FONT_IS_OVERSTRIKE.set(m.overstrike)
                self.VAR_ALIGNMENT.set(m.alignment if m.alignment else "Left")
                mFrame.updateFontPreview(None, None, None)

            if s.windowSettings:
                w = s.windowSettings
                self.VAR_WINDOW_WIDTH.set(w.width)
                self.VAR_WINDOW_HEIGHT.set(w.height)
                self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(w.bgColor)
                self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = w.bgColor
                self.VAR_PATH_WINDOW_BG_IMAGE.set(w.bgImage)
                self.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(w.bgImage))
                self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(w.moveAllOnLineDelay)
                self.VAR_MESSAGE_SHUFFLE.set(w.shuffle)

                self.updateColorBoxes(mFrame, bgFrame)
        except Exception:
            messagebox.showerror("Error", "Something is wrong with the current settings. Reverting to default values.", parent=master)
            self.getDefaultValues(mFrame, bgFrame)

    def updateColorBoxes(self, mFrame, bgFrame):
        bgFrame.CANVAS_WINDOW_BG_IMAGE.itemconfig(bgFrame.RECTANGLE_WINDOW_BG_IMAGE, fill=self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)
        mFrame.CANVAS_MESSAGE_COLOR.itemconfig(mFrame.RECTANGLE_MESSAGE_COLOR, fill=self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
