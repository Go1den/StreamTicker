from tkinter import Frame, Button, E, GROOVE

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
            result = {
                'message': {
                    'DEFAULT_IMAGE': self.window.fields.VAR_DEFAULT_IMAGE.get(),
                    'MESSAGE_STYLE': self.window.fields.VAR_MESSAGE_STYLE.get(),
                    'MESSAGE_DURATION': self.window.fields.VAR_ENTRY_MESSAGE_DURATION.get(),
                    'MESSAGE_INTERMISSION': self.window.fields.VAR_ENTRY_MESSAGE_INTERMISSION.get(),
                    'MESSAGE_COLOR': self.window.mFrame.LABEL_MESSAGE_COLOR.cget("text"),
                    'MESSAGE_FONT_FACE': self.window.fields.VAR_FONT_COMBO_BOX.get(),
                    'NORMAL_FONT_SIZE': self.window.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get(),
                    'ARRIVAL': self.window.fields.VAR_ARRIVAL.get(),
                    'DEPARTURE': self.window.fields.VAR_DEPARTURE.get()
                },
                'window': {
                    'WINDOW_WIDTH': self.window.fields.VAR_WINDOW_WIDTH.get(),
                    'WINDOW_HEIGHT': self.window.fields.VAR_WINDOW_HEIGHT.get(),
                    'WINDOW_BG_COLOR': self.window.fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.get(),
                    'WINDOW_BG_IMAGE': self.window.fields.VAR_PATH_WINDOW_BG_IMAGE.get(),
                    'MOVE_ALL_ON_LINE_DELAY': self.window.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()
                }
            }
            self.window.parent.settings = result
            self.window.master.destroy()
