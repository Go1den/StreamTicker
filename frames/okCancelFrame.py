from tkinter import Frame, Button, E, GROOVE

from objects.messageSettings import MessageSettings
from objects.settings import Settings
from objects.windowSettings import WindowSettings
from validations import validateWindowSettings, validateMessageSettings, validateFontSettings

class OkCancelFrame:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window.master)

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateCurrentSettings())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)

    def validateBeforeSaving(self):
        return validateWindowSettings.validate(self.window.fields) \
               and validateMessageSettings.validate(self.window.fields) \
               and validateFontSettings.validate(self.window.fields)

    def updateCurrentSettings(self):
        if self.validateBeforeSaving():
            windowSettings = WindowSettings(
                self.window.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get(),
                self.window.fields.VAR_PATH_WINDOW_BG_IMAGE.get(),
                self.window.fields.VAR_WINDOW_WIDTH.get(),
                self.window.fields.VAR_WINDOW_HEIGHT.get(),
                self.window.fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.get(),
            )
            messageSettings = MessageSettings(
                self.window.fields.VAR_MESSAGE_STYLE.get(),
                self.window.mFrame.LABEL_MESSAGE_COLOR.cget("text"),
                self.window.fields.VAR_FONT_COMBO_BOX.get(),
                self.window.fields.VAR_ENTRY_MESSAGE_INTERMISSION.get(),
                self.window.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get(),
                self.window.fields.VAR_ENTRY_MESSAGE_DURATION.get(),
                self.window.fields.VAR_ARRIVAL.get(),
                self.window.fields.VAR_DEPARTURE.get()
            )
            self.window.parent.settings = Settings(windowSettings, messageSettings)
            self.window.master.destroy()
