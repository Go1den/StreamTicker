from tkinter import GROOVE, Frame, BooleanVar, Checkbutton, Label, NORMAL, DISABLED, E

from frames.settingsMessageFrame import SettingsMessageFrame

class OverrideFrame:
    def __init__(self, master, globalMessagesSettingsFrame: SettingsMessageFrame, defaultSettings):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        self.gmsFrame = globalMessagesSettingsFrame
        self.defaultSettings = defaultSettings

        self.overrideDuration = BooleanVar()
        self.overrideIntermission = BooleanVar()
        self.overrideScrollSpeed = BooleanVar()
        self.overrideFont = BooleanVar()
        self.overrideFontSize = BooleanVar()
        self.overrideFontColor = BooleanVar()
        self.overrideArrival = BooleanVar()
        self.overrideDeparture = BooleanVar()
        self.overrideFontStyle = BooleanVar()

        self.labelOverride = Label(self.frame, text="Override")
        self.labelOverride.grid(row=0, column=0, columnspan=2, pady=(1, 3))

        self.checkboxDuration = Checkbutton(self.frame, borderwidth=0, variable=self.overrideDuration,
                                            command=lambda: self.toggleField(self.overrideDuration, self.gmsFrame.ENTRY_MESSAGE_DURATION,
                                                                             self.gmsFrame.fields.VAR_ENTRY_MESSAGE_DURATION,
                                                                             self.defaultSettings.messageSettings.duration,
                                                                             NORMAL))
        self.checkboxDuration.grid(row=1, column=1, sticky=E, pady=(0, 4))

        self.checkboxIntermission = Checkbutton(self.frame, borderwidth=0, variable=self.overrideIntermission,
                                                command=lambda: self.toggleField(self.overrideIntermission, self.gmsFrame.ENTRY_MESSAGE_INTERMISSION,
                                                                                 self.gmsFrame.fields.VAR_ENTRY_MESSAGE_INTERMISSION,
                                                                                 self.defaultSettings.messageSettings.intermission,
                                                                                 NORMAL))
        self.checkboxIntermission.grid(row=2, column=1, sticky=E, pady=(0, 4))

        self.checkboxScrollSpeed = Checkbutton(self.frame, borderwidth=0, variable=self.overrideScrollSpeed,
                                               command=lambda: self.toggleField(self.overrideScrollSpeed, self.gmsFrame.entryMoveAllOnLineDelay,
                                                                                self.gmsFrame.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY,
                                                                                self.defaultSettings.windowSettings.moveAllOnLineDelay,
                                                                                NORMAL))
        self.checkboxScrollSpeed.grid(row=3, column=1, sticky=E, pady=(0, 3))

        self.checkboxFont = Checkbutton(self.frame, borderwidth=0, variable=self.overrideFont,
                                        command=lambda: self.toggleField(self.overrideFont, self.gmsFrame.FONT_COMBO_BOX,
                                                                         self.gmsFrame.fields.VAR_FONT_COMBO_BOX,
                                                                         self.defaultSettings.messageSettings.fontFace,
                                                                         "readonly"))
        self.checkboxFont.grid(row=4, column=1, sticky=E, pady=(0, 2))

        self.checkboxFontSize = Checkbutton(self.frame, borderwidth=0, variable=self.overrideFontSize,
                                            command=lambda: self.toggleField(self.overrideFontSize, self.gmsFrame.ENTRY_NORMAL_FONT_SIZE,
                                                                             self.gmsFrame.fields.VAR_ENTRY_NORMAL_FONT_SIZE,
                                                                             self.defaultSettings.messageSettings.fontSize,
                                                                             NORMAL))
        self.checkboxFontSize.grid(row=5, column=1, sticky=E, pady=(0, 2))

        self.checkboxFontStyle = Checkbutton(self.frame, borderwidth=0, variable=self.overrideFontStyle,
                                             command=lambda: self.toggleFontFields(self.overrideFontStyle,
                                                                                   [self.gmsFrame.checkButtonBold,
                                                                                    self.gmsFrame.checkButtonItalic,
                                                                                    self.gmsFrame.checkButtonOverstrike],
                                                                                   [self.gmsFrame.fields.VAR_FONT_IS_BOLD,
                                                                                    self.gmsFrame.fields.VAR_FONT_IS_ITALIC,
                                                                                    self.gmsFrame.fields.VAR_FONT_IS_OVERSTRIKE],
                                                                                   [self.defaultSettings.messageSettings.bold,
                                                                                    self.defaultSettings.messageSettings.italic,
                                                                                    self.defaultSettings.messageSettings.overstrike],
                                                                                   NORMAL))
        self.checkboxFontStyle.grid(row=6, column=1, sticky=E, pady=(0, 40))

        self.checkboxFontColor = Checkbutton(self.frame, borderwidth=0, variable=self.overrideFontColor, command=lambda: self.toggleColors())
        self.checkboxFontColor.grid(row=7, column=1, sticky=E, pady=(0, 10))

        self.checkboxArrival = Checkbutton(self.frame, borderwidth=0, variable=self.overrideArrival,
                                           command=lambda: self.toggleField(self.overrideArrival, self.gmsFrame.ARRIVAL_COMBO_BOX,
                                                                            self.gmsFrame.fields.VAR_ARRIVAL,
                                                                            self.defaultSettings.messageSettings.arrival,
                                                                            "readonly"))
        self.checkboxArrival.grid(row=8, column=1, sticky=E, pady=(0, 4))

        self.checkboxDeparture = Checkbutton(self.frame, borderwidth=0, variable=self.overrideDeparture,
                                             command=lambda: self.toggleField(self.overrideDeparture, self.gmsFrame.DEPARTURE_COMBO_BOX,
                                                                              self.gmsFrame.fields.VAR_DEPARTURE,
                                                                              self.defaultSettings.messageSettings.departure,
                                                                              "readonly"))
        self.checkboxDeparture.grid(row=9, column=1, sticky=E)

    def toggleField(self, checkbox, toggleField, var, defaultSetting, state):
        if checkbox.get():
            toggleField.config(state=state)
        else:
            toggleField.config(state=DISABLED)
            var.set(defaultSetting)

    def toggleFontFields(self, checkbox, toggleFields, varList, defaultSettings, state):
        if checkbox.get():
            for field in toggleFields:
                field.config(state=state)
        else:
            for field in toggleFields:
                field.config(state=DISABLED)
            for idx in range(0, len(varList)):
                varList[idx].set(defaultSettings[idx])
        self.gmsFrame.updateFontPreview(None, None, None)

    def toggleColors(self):
        if self.overrideFontColor.get():
            self.gmsFrame.BUTTON_MESSAGE_COLOR.config(state=NORMAL)
        else:
            self.gmsFrame.BUTTON_MESSAGE_COLOR.config(state=DISABLED)
            self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(self.defaultSettings.messageSettings.color)
            self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = self.defaultSettings.messageSettings.color
            self.gmsFrame.CANVAS_MESSAGE_COLOR.itemconfig(self.gmsFrame.RECTANGLE_MESSAGE_COLOR, fill=self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
