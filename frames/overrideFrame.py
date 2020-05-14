from tkinter import GROOVE, Frame, BooleanVar, Checkbutton, Label, NORMAL, DISABLED

class OverrideFrame:
    def __init__(self, master, globalMessagesSettingsFrame, defaultSettings):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        self.gmsFrame = globalMessagesSettingsFrame
        self.defaultSettings = defaultSettings

        self.overrideDuration = BooleanVar()
        self.overrideIntermission = BooleanVar()
        self.overrideScrollSpeed = BooleanVar()
        self.overrideFont = BooleanVar()
        self.overrideFontSize = BooleanVar()
        self.overrideFontColor = BooleanVar()

        self.labelOverride = Label(self.frame, text="Override")
        self.labelOverride.grid(row=0, pady=1)

        self.checkboxDuration = Checkbutton(self.frame, variable=self.overrideDuration,
                                            command=lambda: self.toggleField(self.overrideDuration, self.gmsFrame.ENTRY_MESSAGE_DURATION,
                                                                             self.gmsFrame.fields.VAR_ENTRY_MESSAGE_DURATION,
                                                                             defaultSettings.get("message")[0].get("MESSAGE_DURATION"),
                                                                             NORMAL))
        self.checkboxDuration.grid(row=1)

        self.checkboxIntermission = Checkbutton(self.frame, variable=self.overrideIntermission,
                                                command=lambda: self.toggleField(self.overrideIntermission, self.gmsFrame.ENTRY_MESSAGE_INTERMISSION,
                                                                                 self.gmsFrame.fields.VAR_ENTRY_MESSAGE_INTERMISSION,
                                                                                 defaultSettings.get("message")[0].get("MESSAGE_INTERMISSION"),
                                                                                 NORMAL))
        self.checkboxIntermission.grid(row=2)

        self.checkboxScrollSpeed = Checkbutton(self.frame, variable=self.overrideScrollSpeed,
                                               command=lambda: self.toggleField(self.overrideScrollSpeed, self.gmsFrame.MESSAGE_SPEED_COMBO_BOX,
                                                                                self.gmsFrame.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY,
                                                                                defaultSettings.get("window")[0].get("MOVE_ALL_ON_LINE_DELAY"),
                                                                                "readonly"))
        self.checkboxScrollSpeed.grid(row=3)

        self.checkboxFont = Checkbutton(self.frame, variable=self.overrideFont,
                                        command=lambda: self.toggleField(self.overrideFont, self.gmsFrame.FONT_COMBO_BOX,
                                                                         self.gmsFrame.fields.VAR_FONT_COMBO_BOX,
                                                                         defaultSettings.get("message")[0].get("MESSAGE_FONT_FACE"),
                                                                         "readonly"))
        self.checkboxFont.grid(row=4)

        self.checkboxFontSize = Checkbutton(self.frame, variable=self.overrideFontSize,
                                            command=lambda: self.toggleField(self.overrideFontSize, self.gmsFrame.ENTRY_NORMAL_FONT_SIZE,
                                                                             self.gmsFrame.fields.VAR_ENTRY_NORMAL_FONT_SIZE,
                                                                             defaultSettings.get("message")[0].get("NORMAL_FONT_SIZE"),
                                                                             NORMAL))
        self.checkboxFontSize.grid(row=5)

        self.checkboxFontColor = Checkbutton(self.frame, variable=self.overrideFontColor,
                                             command=lambda: self.toggleField(self.overrideFontColor, self.gmsFrame.BUTTON_MESSAGE_COLOR))
        self.checkboxFontColor.grid(row=6)

    def toggleField(self, checkbox, toggleField, var, defaultSetting, state):
        if checkbox.get():
            print("Checkbox is checked!")
            toggleField.config(state=state)
        else:
            print("Checkbox is NOT checked!")
            toggleField.config(state=DISABLED)
            var.set(defaultSetting)
