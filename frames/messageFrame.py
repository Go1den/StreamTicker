from tkinter import Label, Entry, Frame, GROOVE, E, W, Button, ttk, font, colorchooser, Canvas

from utils.createToolTip import CreateToolTip

class MessageFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_MESSAGE_SETTINGS = 0
        ROW_MESSAGE_DURATION = 1
        ROW_MESSAGE_INTERMISSION = 2
        ROW_FONT = 4
        ROW_MESSAGE_COLOR = 6
        ROW_NORMAL_FONT_SIZE = 5
        ROW_MESSAGE_SPEED = 3

        Label(self.frame, text="Global Message Settings").grid(row=ROW_MESSAGE_SETTINGS, column=0, columnspan=3, sticky=W, pady=1)
        self.LABEL_MESSAGE_DURATION = Label(self.frame, text="Message Duration:")
        self.LABEL_MESSAGE_DURATION.grid(row=ROW_MESSAGE_DURATION, column=0, sticky=E, pady=1)
        messageDurationFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_DURATION = Entry(messageDurationFrame, textvariable=fields.VAR_ENTRY_MESSAGE_DURATION, width=4)
        self.ENTRY_MESSAGE_DURATION.grid(row=0, column=0, sticky=W, pady=1)
        Label(messageDurationFrame, text="seconds").grid(row=0, column=1, sticky=W, pady=1)
        messageDurationFrame.grid(row=ROW_MESSAGE_DURATION, column=1, sticky=W, pady=1)

        self.LABEL_MESSAGE_INTERMISSION = Label(self.frame, text="Message Intermission:")
        self.LABEL_MESSAGE_INTERMISSION.grid(row=ROW_MESSAGE_INTERMISSION, column=0, sticky=E, pady=1)
        messageIntermissionFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_INTERMISSION = Entry(messageIntermissionFrame, textvariable=fields.VAR_ENTRY_MESSAGE_INTERMISSION, width=4)
        self.ENTRY_MESSAGE_INTERMISSION.grid(row=0, column=0, sticky=W, pady=1)
        Label(messageIntermissionFrame, text="seconds").grid(row=0, column=1, sticky=W, pady=1)
        messageIntermissionFrame.grid(row=ROW_MESSAGE_INTERMISSION, column=1, sticky=W, pady=1)

        self.LABEL_MESSAGE_FONT_FACE = Label(self.frame, text="Message Font:")
        self.TOOLTIP_MESSAGE_FONT_FACE = CreateToolTip(self.LABEL_MESSAGE_FONT_FACE,
                                                       "The font to be used for all messages.\nDue to the way this program operates, it is STRONGLY recommended that you select a monospaced font.")
        self.LABEL_MESSAGE_FONT_FACE.grid(row=ROW_FONT, column=0, sticky=E, pady=1)
        self.FONT_FAMILIES = sorted([f for f in font.families()])
        self.FONT_COMBO_BOX = ttk.Combobox(self.frame, values=self.FONT_FAMILIES, textvariable=fields.VAR_FONT_COMBO_BOX, state="readonly")
        self.FONT_COMBO_BOX.grid(row=ROW_FONT, column=1, sticky=W, pady=1)

        self.BUTTON_MESSAGE_COLOR = Button(self.frame, text='Message Color:', command=lambda: self.updateMessageColor(fields))
        self.TOOLTIP_MESSAGE_COLOR = CreateToolTip(self.BUTTON_MESSAGE_COLOR, "Color of the font used to display each message.")
        self.BUTTON_MESSAGE_COLOR.grid(row=ROW_MESSAGE_COLOR, column=0, sticky=E, padx=4, pady=1)

        messageColorFrame = Frame(self.frame)
        self.CANVAS_MESSAGE_COLOR = Canvas(messageColorFrame, width=80, height=30)
        self.RECTANGLE_MESSAGE_COLOR = self.CANVAS_MESSAGE_COLOR.create_rectangle(80, 4, 0, 30, fill=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND, outline="")
        self.CANVAS_MESSAGE_COLOR.grid(row=0, column=0, sticky=W, pady=1)
        self.LABEL_MESSAGE_COLOR = Label(messageColorFrame, textvariable=fields.VAR_LABEL_MESSAGE_COLOR_TEXT)
        self.LABEL_MESSAGE_COLOR.grid(row=0, column=1, sticky=W, pady=1)
        messageColorFrame.grid(row=ROW_MESSAGE_COLOR, column=1, sticky=W, pady=1)

        self.LABEL_NORMAL_FONT_SIZE = Label(self.frame, text="Font Size:")
        self.TOOLTIP_NORMAL_FONT_SIZE = CreateToolTip(self.LABEL_NORMAL_FONT_SIZE, "Font size for messages of standard length.")
        self.LABEL_NORMAL_FONT_SIZE.grid(row=ROW_NORMAL_FONT_SIZE, column=0, sticky=E, pady=1)
        self.ENTRY_NORMAL_FONT_SIZE = Entry(self.frame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE, width=4)
        self.ENTRY_NORMAL_FONT_SIZE.grid(row=ROW_NORMAL_FONT_SIZE, column=1, sticky=W, pady=1)

        self.LABEL_MOVE_ALL_ON_LINE_DELAY = Label(self.frame, text="Message Scroll Speed:")
        self.LABEL_MOVE_ALL_ON_LINE_DELAY.grid(row=ROW_MESSAGE_SPEED, column=0, sticky=E, pady=1)
        self.MESSAGE_SPEEDS = ["Fastest", "Fast", "Normal", "Slow", "Slowest"]
        self.MESSAGE_SPEED_COMBO_BOX = ttk.Combobox(self.frame, values=self.MESSAGE_SPEEDS, textvariable=fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY, state="readonly")
        self.MESSAGE_SPEED_COMBO_BOX.grid(row=ROW_MESSAGE_SPEED, column=1, sticky=W, pady=1)

    def updateMessageColor(self, fields):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(color[1])
            fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = color[1]
            self.CANVAS_MESSAGE_COLOR.itemconfig(self.RECTANGLE_MESSAGE_COLOR, fill=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
