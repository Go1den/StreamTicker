from tkinter import GROOVE, Frame, BooleanVar, Checkbutton, Label, NORMAL, DISABLED, E, W

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
        self.overrideArrival = BooleanVar()
        self.overrideDeparture = BooleanVar()

        self.labelOverride = Label(self.frame, text="Override")
        self.labelOverride.grid(row=0, column=0, columnspan=2, pady=1)

        self.checkboxDuration = Checkbutton(self.frame, variable=self.overrideDuration,
                                            command=lambda: self.toggleField(self.overrideDuration, self.gmsFrame.ENTRY_MESSAGE_DURATION,
                                                                             self.gmsFrame.fields.VAR_ENTRY_MESSAGE_DURATION,
                                                                             self.defaultSettings.get("message").get("MESSAGE_DURATION"),
                                                                             NORMAL))
        self.checkboxDuration.grid(row=1, column=1, sticky=E)

        # self.labelDuration = Label(self.frame, text="Message Duration")
        # self.labelDuration.grid(row=1, column=2, sticky=W)

        self.checkboxIntermission = Checkbutton(self.frame, variable=self.overrideIntermission,
                                                command=lambda: self.toggleField(self.overrideIntermission, self.gmsFrame.ENTRY_MESSAGE_INTERMISSION,
                                                                                 self.gmsFrame.fields.VAR_ENTRY_MESSAGE_INTERMISSION,
                                                                                 self.defaultSettings.get("message").get("MESSAGE_INTERMISSION"),
                                                                                 NORMAL))
        self.checkboxIntermission.grid(row=2, column=1, sticky=E)
        #
        # self.labelIntermission = Label(self.frame, text="Message Intermission")
        # self.labelIntermission.grid(row=2, column=2, sticky=W)

        self.checkboxScrollSpeed = Checkbutton(self.frame, variable=self.overrideScrollSpeed,
                                               command=lambda: self.toggleField(self.overrideScrollSpeed, self.gmsFrame.MESSAGE_SPEED_COMBO_BOX,
                                                                                self.gmsFrame.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY,
                                                                                self.defaultSettings.get("window").get("MOVE_ALL_ON_LINE_DELAY"),
                                                                                "readonly"))
        self.checkboxScrollSpeed.grid(row=3, column=1, sticky=E)

        # self.labelScrollSpeed = Label(self.frame, text="Message Scroll Speed")
        # self.labelScrollSpeed.grid(row=3, column=2, sticky=W)

        self.checkboxFont = Checkbutton(self.frame, variable=self.overrideFont,
                                        command=lambda: self.toggleField(self.overrideFont, self.gmsFrame.FONT_COMBO_BOX,
                                                                         self.gmsFrame.fields.VAR_FONT_COMBO_BOX,
                                                                         self.defaultSettings.get("message").get("MESSAGE_FONT_FACE"),
                                                                         "readonly"))
        self.checkboxFont.grid(row=4, column=1, sticky=E)

        # self.labelFont = Label(self.frame, text="Message Font")
        # self.labelFont.grid(row=4, column=2, sticky=W)

        self.checkboxFontSize = Checkbutton(self.frame, variable=self.overrideFontSize,
                                            command=lambda: self.toggleField(self.overrideFontSize, self.gmsFrame.ENTRY_NORMAL_FONT_SIZE,
                                                                             self.gmsFrame.fields.VAR_ENTRY_NORMAL_FONT_SIZE,
                                                                             self.defaultSettings.get("message").get("NORMAL_FONT_SIZE"),
                                                                             NORMAL))
        self.checkboxFontSize.grid(row=5, column=1, sticky=E)
        #
        # self.labelFontSize = Label(self.frame, text="Font Size")
        # self.labelFontSize.grid(row=5, column=2, sticky=W)

        self.checkboxFontColor = Checkbutton(self.frame, variable=self.overrideFontColor, command=lambda: self.toggleColors())
        self.checkboxFontColor.grid(row=6, column=1, sticky=E)

        # self.labelFontColor = Label(self.frame, text="Font Color")
        # self.labelFontColor.grid(row=6, column=2, sticky=W)

        self.checkboxArrival = Checkbutton(self.frame, variable=self.overrideArrival,
                                           command=lambda: self.toggleField(self.overrideArrival, self.gmsFrame.ARRIVAL_COMBO_BOX,
                                                                            self.gmsFrame.fields.VAR_ARRIVAL,
                                                                            self.defaultSettings.get("message").get("ARRIVAL"),
                                                                            "readonly"))
        self.checkboxArrival.grid(row=7, column=1, sticky=E)

        # self.labelArrival = Label(self.frame, text="Arrival Animation")
        # self.labelArrival.grid(row=7, column=2, sticky=W)

        self.checkboxDeparture = Checkbutton(self.frame, variable=self.overrideDeparture,
                                             command=lambda: self.toggleField(self.overrideDeparture, self.gmsFrame.DEPARTURE_COMBO_BOX,
                                                                              self.gmsFrame.fields.VAR_DEPARTURE,
                                                                              self.defaultSettings.get("message").get("DEPARTURE"),
                                                                              "readonly"))
        self.checkboxDeparture.grid(row=8, column=1, sticky=E)

        # self.labelDeparture = Label(self.frame, text="Departure Animation")
        # self.labelDeparture.grid(row=8, column=2, sticky=W)

    def toggleField(self, checkbox, toggleField, var, defaultSetting, state):
        if checkbox.get():
            toggleField.config(state=state)
        else:
            toggleField.config(state=DISABLED)
            var.set(defaultSetting)

    def toggleColors(self):
        if self.overrideFontColor.get():
            self.gmsFrame.BUTTON_MESSAGE_COLOR.config(state=NORMAL)
        else:
            self.gmsFrame.BUTTON_MESSAGE_COLOR.config(state=DISABLED)
            self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(self.defaultSettings.get("message").get("MESSAGE_COLOR"))
            self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = self.defaultSettings.get("message").get("MESSAGE_COLOR")
            self.gmsFrame.CANVAS_MESSAGE_COLOR.itemconfig(self.gmsFrame.RECTANGLE_MESSAGE_COLOR, fill=self.gmsFrame.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
