import json
from tkinter import BooleanVar, StringVar, messagebox

from utils import helperMethods
from settings import Settings

class SettingsGUIFields():
    def __init__(self):
        self.VAR_CHECK_SLIDING_RIGHT = BooleanVar()
        self.VAR_CHECK_SLIDING_LEFT = BooleanVar()
        self.VAR_CHECK_SLIDING_UP = BooleanVar()
        self.VAR_CHECK_SLIDING_DOWN = BooleanVar()
        self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = BooleanVar()
        self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = BooleanVar()
        self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = BooleanVar()
        self.VAR_CHECK_COVERING_WITH_RECTANGLES = BooleanVar()

        self.VAR_DEFAULT_IMAGE = StringVar()
        self.VAR_MESSAGE_STYLE = StringVar()
        self.VAR_ENTRY_MESSAGE_DURATION = StringVar()
        self.VAR_ENTRY_MESSAGE_INTERMISSION = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_TEXT = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = ""
        self.VAR_FONT_COMBO_BOX = StringVar()
        self.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES = StringVar()
        self.VAR_ENTRY_SMALLER_FONT_SIZE = StringVar()
        self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP = StringVar()
        self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES = StringVar()

        self.VAR_ENTRY_WINDOW_WIDTH = StringVar()
        self.VAR_ENTRY_MESSAGE_X_POS = StringVar()
        self.VAR_ENTRY_IMAGE_X_POS = StringVar()
        self.VAR_ENTRY_WINDOW_HEIGHT = StringVar()
        self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = ""
        self.VAR_LABEL_WINDOW_BG_COLOR_TEXT = StringVar()
        self.VAR_DISPLAY_WINDOW_BG_IMAGE = StringVar()
        self.VAR_PATH_WINDOW_BG_IMAGE = StringVar()
        self.VAR_ENTRY_BACKGROUND_X_POS = StringVar()
        self.VAR_ENTRY_BACKGROUND_Y_POS = StringVar()
        self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY = StringVar()
        self.getDefaultValues(False)

    def getDefaultValues(self, confirm, mFrame=None, bgFrame=None):
        if not confirm or messagebox.askokcancel("Confirm New Settings", "All changes made will be lost, and the default values will be set. Do you want to continue?"):
            self.VAR_CHECK_SLIDING_RIGHT.set(True)
            self.VAR_CHECK_SLIDING_LEFT.set(True)
            self.VAR_CHECK_SLIDING_UP.set(True)
            self.VAR_CHECK_SLIDING_DOWN.set(True)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.set(True)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.set(True)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.set(True)
            self.VAR_CHECK_COVERING_WITH_RECTANGLES.set(False)

            self.VAR_DEFAULT_IMAGE.set("imagefiles/stLogo28.png")
            self.VAR_MESSAGE_STYLE.set("")
            self.VAR_ENTRY_MESSAGE_DURATION.set("5")
            self.VAR_ENTRY_MESSAGE_INTERMISSION.set("0.5")
            self.VAR_LABEL_MESSAGE_COLOR_TEXT.set("#ffffff")
            self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = "#ffffff"
            self.VAR_FONT_COMBO_BOX.set("Courier New")
            self.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.set("16")
            self.VAR_ENTRY_NORMAL_FONT_SIZE.set("26")
            self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP.set("20")
            self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.set("4")
            self.VAR_ENTRY_SMALLER_FONT_SIZE.set("22")
            self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP.set("16")
            self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.set("6")

            self.VAR_ENTRY_WINDOW_WIDTH.set("400")
            self.VAR_ENTRY_WINDOW_HEIGHT.set("44")
            self.VAR_ENTRY_MESSAGE_X_POS.set("60")
            self.VAR_ENTRY_IMAGE_X_POS.set("22")
            self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = "#000000"
            self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set("#000000")
            self.VAR_PATH_WINDOW_BG_IMAGE.set("imagefiles/background.png")
            self.VAR_DISPLAY_WINDOW_BG_IMAGE.set("background1.png")
            self.VAR_ENTRY_BACKGROUND_X_POS.set("202")
            self.VAR_ENTRY_BACKGROUND_Y_POS.set("44")
            self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set("Fast")
            if mFrame and bgFrame:
                self.updateColorBoxes(mFrame, bgFrame)

    def loadJson(self, file, mFrame, bgFrame):
        # Todo: backup the current settings so that if load fails, we can revert to those rather than doing a partial load
        try:
            with open(file) as f:
                data = json.loads(f.read())
            s = Settings(data)
            self.VAR_CHECK_SLIDING_RIGHT.set(s.ENABLE_DEPARTING_BY_SLIDING_RIGHT)

            self.VAR_CHECK_SLIDING_LEFT.set(s.ENABLE_DEPARTING_BY_SLIDING_LEFT)
            self.VAR_CHECK_SLIDING_UP.set(s.ENABLE_DEPARTING_BY_SLIDING_UP)
            self.VAR_CHECK_SLIDING_DOWN.set(s.ENABLE_DEPARTING_BY_SLIDING_DOWN)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.set(s.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.set(s.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
            self.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.set(s.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
            self.VAR_CHECK_COVERING_WITH_RECTANGLES.set(s.ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES)

            self.VAR_DEFAULT_IMAGE.set(s.DEFAULT_IMAGE)
            self.VAR_MESSAGE_STYLE.set(s.MESSAGE_STYLE)
            self.VAR_ENTRY_MESSAGE_DURATION.set(s.MESSAGE_DURATION)
            self.VAR_ENTRY_MESSAGE_INTERMISSION.set(s.MESSAGE_INTERMISSION)
            self.VAR_LABEL_MESSAGE_COLOR_TEXT.set(s.MESSAGE_COLOR)
            self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = s.MESSAGE_COLOR
            self.VAR_FONT_COMBO_BOX.set(s.MESSAGE_FONT_FACE)
            self.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.set(s.MAX_LENGTH_FOR_NORMAL_FONT_SIZE)
            self.VAR_ENTRY_NORMAL_FONT_SIZE.set(s.NORMAL_FONT_SIZE)
            self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP.set(s.NORMAL_FONT_SIZE_GAP)
            self.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.set(s.NORMAL_FONT_SIZE_GAP_FOR_SPACES)
            self.VAR_ENTRY_SMALLER_FONT_SIZE.set(s.SMALLER_FONT_SIZE)
            self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP.set(s.SMALLER_FONT_SIZE_GAP)
            self.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.set(s.SMALLER_FONT_SIZE_GAP_FOR_SPACES)

            self.VAR_ENTRY_MESSAGE_X_POS.set(s.MESSAGE_X_POS)
            self.VAR_ENTRY_IMAGE_X_POS.set(s.IMAGE_X_POS)
            self.VAR_ENTRY_WINDOW_WIDTH.set(s.WINDOW_WIDTH)
            self.VAR_ENTRY_WINDOW_HEIGHT.set(s.WINDOW_HEIGHT)
            self.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(s.WINDOW_BG_COLOR)
            self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = s.WINDOW_BG_COLOR
            self.VAR_PATH_WINDOW_BG_IMAGE.set(s.WINDOW_BG_IMAGE)
            self.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(s.WINDOW_BG_IMAGE))
            self.VAR_ENTRY_BACKGROUND_X_POS.set(s.BACKGROUND_X_POS)
            self.VAR_ENTRY_BACKGROUND_Y_POS.set(s.BACKGROUND_Y_POS)
            self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(self.convertDelayValueToName(float(s.MOVE_ALL_ON_LINE_DELAY)))
            self.updateColorBoxes(mFrame, bgFrame)
            messagebox.showinfo("Success", "Settings loaded!")
            return True
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Unable to load file. Please select a valid layout file.")
            return False

    def convertDelayNameToValue(self, name):
        delayDict = {'Fastest': ".002",
                     'Fast': ".004",
                     'Normal': ".006",
                     'Slow': ".008",
                     'Slowest': ".01"}
        return delayDict[name] if delayDict[name] else ".004"

    def convertDelayValueToName(self, value):
        delayDict = {.002: "Fastest",
                     .004: "Fast",
                     .006: "Normal",
                     .008: "Slow",
                     .01: "Slowest"
                     }
        return delayDict[value] if delayDict[value] else "Fast"

    def updateColorBoxes(self, mFrame, bgFrame):
        bgFrame.CANVAS_WINDOW_BG_IMAGE.itemconfig(bgFrame.RECTANGLE_WINDOW_BG_IMAGE, fill=self.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)
        mFrame.CANVAS_MESSAGE_COLOR.itemconfig(mFrame.RECTANGLE_MESSAGE_COLOR, fill=self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
