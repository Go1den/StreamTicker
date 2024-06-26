from tkinter import Frame, E, GROOVE

from objects.messageSettings import MessageSettings
from objects.settings import Settings
from objects.windowSettings import WindowSettings
from utils.hoverButton import HoverButton
from validations import validateWindowSettings, validateMessageSettings, validateFontSettings

class OkCancelFrame:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window.master)

        self.okButton = HoverButton(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateCurrentSettings())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = HoverButton(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)

    def validateBeforeSaving(self):
        return validateWindowSettings.validate(self.window.fields, self.window.master) \
               and validateMessageSettings.validate(self.window.fields, self.window.master) \
               and validateFontSettings.validate(self.window.fields, self.window.master)

    def updateCurrentSettings(self):
        if self.validateBeforeSaving():
            windowSettings = WindowSettings(
                self.window.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get(),
                self.window.fields.VAR_PATH_WINDOW_BG_IMAGE.get(),
                self.window.fields.VAR_WINDOW_WIDTH.get(),
                self.window.fields.VAR_WINDOW_HEIGHT.get(),
                self.window.fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.get(),
                self.window.fields.VAR_MESSAGE_SHUFFLE.get()
            )
            messageSettings = MessageSettings(
                self.window.mFrame.LABEL_MESSAGE_COLOR.cget("text"),
                self.window.fields.VAR_FONT_COMBO_BOX.get(),
                self.window.fields.VAR_ENTRY_MESSAGE_INTERMISSION.get(),
                self.window.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get(),
                self.window.fields.VAR_ENTRY_MESSAGE_DURATION.get(),
                self.window.fields.VAR_ARRIVAL.get(),
                self.window.fields.VAR_DEPARTURE.get(),
                self.window.fields.VAR_FONT_IS_BOLD.get(),
                self.window.fields.VAR_FONT_IS_ITALIC.get(),
                self.window.fields.VAR_FONT_IS_OVERSTRIKE.get(),
                self.window.fields.VAR_ALIGNMENT.get()
            )
            defaultTemplate = {"parts": [{
                "partType": x.partType,
                "sortOrder": self.window.tFrame.messageParts.index(x) + 1,
                "value": x.value
            } for x in self.window.tFrame.messageParts], "overrides": {}}
            self.window.parent.settings = Settings(windowSettings, messageSettings, defaultTemplate)
            self.window.parent.applyCurrentWindowSettings()
            self.window.master.destroy()
