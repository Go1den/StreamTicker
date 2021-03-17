from tkinter import Label, Entry, Frame, GROOVE, E, W, Button, ttk, font, colorchooser, Canvas, EW

class SettingsMessageFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        self.fields = fields

        self.fields.VAR_FONT_COMBO_BOX.trace('w', self.updateFontPreview)

        ROW_MESSAGE_SETTINGS = 0
        ROW_MESSAGE_DURATION = 1
        ROW_MESSAGE_INTERMISSION = 2
        ROW_MESSAGE_SPEED = 3
        ROW_FONT = 4
        ROW_NORMAL_FONT_SIZE = 5
        ROW_MESSAGE_COLOR = 6
        ROW_ARRIVAL = 7
        ROW_DEPARTURE = 8
        ROW_FONT_PREVIEW = 9

        Label(self.frame, text="Global Message Settings").grid(row=ROW_MESSAGE_SETTINGS, column=0, columnspan=3, sticky=W, pady=1)
        self.LABEL_MESSAGE_DURATION = Label(self.frame, text="Message Duration:")
        self.LABEL_MESSAGE_DURATION.grid(row=ROW_MESSAGE_DURATION, column=0, sticky=E, pady=1)
        messageDurationFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_DURATION = Entry(messageDurationFrame, textvariable=self.fields.VAR_ENTRY_MESSAGE_DURATION, width=4)
        self.ENTRY_MESSAGE_DURATION.grid(row=0, column=0, sticky=W, pady=1)
        Label(messageDurationFrame, text="seconds").grid(row=0, column=1, sticky=W, pady=1)
        messageDurationFrame.grid(row=ROW_MESSAGE_DURATION, column=1, sticky=W, pady=1)

        self.LABEL_MESSAGE_INTERMISSION = Label(self.frame, text="Message Intermission:")
        self.LABEL_MESSAGE_INTERMISSION.grid(row=ROW_MESSAGE_INTERMISSION, column=0, sticky=E, pady=1)
        messageIntermissionFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_INTERMISSION = Entry(messageIntermissionFrame, textvariable=self.fields.VAR_ENTRY_MESSAGE_INTERMISSION, width=4)
        self.ENTRY_MESSAGE_INTERMISSION.grid(row=0, column=0, sticky=W, pady=1)
        Label(messageIntermissionFrame, text="seconds").grid(row=0, column=1, sticky=W, pady=1)
        messageIntermissionFrame.grid(row=ROW_MESSAGE_INTERMISSION, column=1, sticky=W, pady=1)

        self.LABEL_MESSAGE_FONT_FACE = Label(self.frame, text="Message Font:")
        self.LABEL_MESSAGE_FONT_FACE.grid(row=ROW_FONT, column=0, sticky=E, pady=1)
        self.FONT_FAMILIES = sorted([f for f in font.families()])
        self.FONT_COMBO_BOX = ttk.Combobox(self.frame, values=self.FONT_FAMILIES, textvariable=self.fields.VAR_FONT_COMBO_BOX, state="readonly")
        self.FONT_COMBO_BOX.grid(row=ROW_FONT, column=1, sticky=W, pady=1)

        self.LABEL_FONT_PREVIEW = Label(self.frame, text="Font Preview, Size 12", font=self.fields.VAR_FONT_COMBO_BOX, borderwidth=2, relief=GROOVE)
        self.LABEL_FONT_PREVIEW.grid(row=ROW_FONT_PREVIEW, column=0, columnspan=2, sticky=EW, pady=(1,0))

        self.BUTTON_MESSAGE_COLOR = Button(self.frame, text='Font Color:', command=lambda: self.updateMessageColor())
        self.BUTTON_MESSAGE_COLOR.grid(row=ROW_MESSAGE_COLOR, column=0, sticky=E, padx=4, pady=1)

        messageColorFrame = Frame(self.frame)
        self.CANVAS_MESSAGE_COLOR = Canvas(messageColorFrame, width=80, height=30)
        self.RECTANGLE_MESSAGE_COLOR = self.CANVAS_MESSAGE_COLOR.create_rectangle(80, 4, 0, 30, fill=self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND, outline="")
        self.CANVAS_MESSAGE_COLOR.grid(row=0, column=0, sticky=W, pady=1)
        self.LABEL_MESSAGE_COLOR = Label(messageColorFrame, textvariable=self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT)
        self.LABEL_MESSAGE_COLOR.grid(row=0, column=1, sticky=W, pady=1)
        messageColorFrame.grid(row=ROW_MESSAGE_COLOR, column=1, sticky=W, pady=1)

        self.LABEL_NORMAL_FONT_SIZE = Label(self.frame, text="Font Size:")
        self.LABEL_NORMAL_FONT_SIZE.grid(row=ROW_NORMAL_FONT_SIZE, column=0, sticky=E, pady=1)
        self.ENTRY_NORMAL_FONT_SIZE = Entry(self.frame, textvariable=self.fields.VAR_ENTRY_NORMAL_FONT_SIZE, width=4)
        self.ENTRY_NORMAL_FONT_SIZE.grid(row=ROW_NORMAL_FONT_SIZE, column=1, sticky=W, pady=1)

        self.LABEL_MOVE_ALL_ON_LINE_DELAY = Label(self.frame, text="Message Scroll Speed:")
        self.LABEL_MOVE_ALL_ON_LINE_DELAY.grid(row=ROW_MESSAGE_SPEED, column=0, sticky=E, pady=1)
        self.MESSAGE_SPEEDS = ["Fastest", "Fast", "Normal", "Slow", "Slowest"]
        self.MESSAGE_SPEED_COMBO_BOX = ttk.Combobox(self.frame, values=self.MESSAGE_SPEEDS, textvariable=self.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY, state="readonly")
        self.MESSAGE_SPEED_COMBO_BOX.grid(row=ROW_MESSAGE_SPEED, column=1, sticky=W, pady=1)

        self.ARRIVAL_ANIMATIONS = ["Pick For Me", "Slide Right", "Slide Left", "Slide Up", "Slide Down", "Zip Forward", "Zip Backward", "Zip Randomly"]
        self.DEPARTURE_ANIMATIONS = ["Pick For Me", "Slide Right", "Slide Left", "Slide Up", "Slide Down", "Unzip Forward", "Unzip Backward", "Unzip Randomly"]

        self.LABEL_ARRIVAL = Label(self.frame, text="Arrival Animation:")
        self.LABEL_ARRIVAL.grid(row=ROW_ARRIVAL, column=0, sticky=E, pady=1)
        self.ARRIVAL_COMBO_BOX = ttk.Combobox(self.frame, values=self.ARRIVAL_ANIMATIONS, textvariable=self.fields.VAR_ARRIVAL, state="readonly")
        self.ARRIVAL_COMBO_BOX.grid(row=ROW_ARRIVAL, column=1, sticky=W, pady=1, padx=(0,4))

        self.LABEL_DEPARTURE = Label(self.frame, text="Departure Animation:")
        self.LABEL_DEPARTURE.grid(row=ROW_DEPARTURE, column=0, sticky=E, pady=1)
        self.DEPARTURE_COMBO_BOX = ttk.Combobox(self.frame, values=self.DEPARTURE_ANIMATIONS, textvariable=self.fields.VAR_DEPARTURE, state="readonly")
        self.DEPARTURE_COMBO_BOX.grid(row=ROW_DEPARTURE, column=1, sticky=W, pady=(1,4))

    def updateMessageColor(self):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(color[1])
            self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = color[1]
            self.CANVAS_MESSAGE_COLOR.itemconfig(self.RECTANGLE_MESSAGE_COLOR, fill=self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)

    def updateFontPreview(self, a, b, c):
        print(self.fields.VAR_FONT_COMBO_BOX.get())
        self.LABEL_FONT_PREVIEW.config(font=(self.fields.VAR_FONT_COMBO_BOX.get(), 12))
