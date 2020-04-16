from tkinter import Label, Entry, Frame, GROOVE, E, W, Button, ttk, NSEW, font, colorchooser

from createToolTip import CreateToolTip

class MessageFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        Label(self.frame, text="Message Settings").grid(row=0, column=0, columnspan=3, sticky=W)
        self.LABEL_MESSAGE_DURATION = Label(self.frame, text="Message Duration:")
        self.LABEL_MESSAGE_DURATION.grid(row=1, column=0, sticky=E)
        messageDurationFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_DURATION = Entry(messageDurationFrame, textvariable=fields.VAR_ENTRY_MESSAGE_DURATION, width=4)
        self.ENTRY_MESSAGE_DURATION.grid(row=0, column=0, sticky=W)
        Label(messageDurationFrame, text="seconds").grid(row=0, column=1, sticky=W)
        messageDurationFrame.grid(row=1, column=1, sticky=W)

        self.LABEL_MESSAGE_INTERMISSION = Label(self.frame, text="Time Between Each Message:")
        self.TOOLTIP_MESSAGE_INTERMISSION = CreateToolTip(self.LABEL_MESSAGE_INTERMISSION,
                                                          "The amount of time between when the previous message disappears\nand the next message appears, in seconds. This can be a decimal value.")
        self.LABEL_MESSAGE_INTERMISSION.grid(row=2, column=0, sticky=E)
        messageIntermissionFrame = Frame(self.frame)
        self.ENTRY_MESSAGE_INTERMISSION = Entry(messageIntermissionFrame, textvariable=fields.VAR_ENTRY_MESSAGE_INTERMISSION, width=4)
        self.ENTRY_MESSAGE_INTERMISSION.grid(row=0, column=0, sticky=W)
        Label(messageIntermissionFrame, text="seconds").grid(row=0, column=1, sticky=W)
        messageIntermissionFrame.grid(row=2, column=1, sticky=W)

        self.LABEL_MESSAGE_FONT_FACE = Label(self.frame, text="Message Font:")
        self.TOOLTIP_MESSAGE_FONT_FACE = CreateToolTip(self.LABEL_MESSAGE_FONT_FACE,
                                                       "The font to be used for all messages.\nDue to the way this program operates, it is STRONGLY recommended that you select a monospaced font.")
        self.LABEL_MESSAGE_FONT_FACE.grid(row=3, column=0, sticky=E)
        self.FONT_FAMILIES = sorted([f for f in font.families()])
        self.FONT_COMBO_BOX = ttk.Combobox(self.frame, values=self.FONT_FAMILIES, textvariable=fields.VAR_FONT_COMBO_BOX, state="readonly")
        self.FONT_COMBO_BOX.grid(row=3, column=1, sticky=W)

        self.BUTTON_MESSAGE_COLOR = Button(self.frame, text='Message Color:', command=lambda: self.updateMessageColor(self.LABEL_MESSAGE_COLOR, fields))
        self.TOOLTIP_MESSAGE_COLOR = CreateToolTip(self.BUTTON_MESSAGE_COLOR, "Color of the font used to display each message.")
        self.BUTTON_MESSAGE_COLOR.grid(row=4, column=0, sticky=E, padx=4)
        self.LABEL_MESSAGE_COLOR = Label(self.frame, textvariable=fields.VAR_LABEL_MESSAGE_COLOR_TEXT, foreground=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
        self.LABEL_MESSAGE_COLOR.grid(row=4, column=1, sticky=W)
        # Label(self.frame, text="Normal Message Font Settings").grid(row=4, column=0, sticky=W)
        self.LABEL_NORMAL_FONT_SIZE = Label(self.frame, text="Normal Message Font Size:")
        self.TOOLTIP_NORMAL_FONT_SIZE = CreateToolTip(self.LABEL_NORMAL_FONT_SIZE, "Font size for messages of standard length.")
        self.LABEL_NORMAL_FONT_SIZE.grid(row=5, column=0, sticky=E)
        self.ENTRY_NORMAL_FONT_SIZE = Entry(self.frame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE, width=4)
        self.ENTRY_NORMAL_FONT_SIZE.grid(row=5, column=1, sticky=W)
        # self.LABEL_NORMAL_FONT_SIZE_GAP = Label(self.frame, text="Font Gap Size:")
        # self.TOOLTIP_NORMAL_FONT_SIZE_GAP = CreateToolTip(self.LABEL_NORMAL_FONT_SIZE_GAP,
        #                                                   "This is the number of pixels between each character in a message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
        # self.LABEL_NORMAL_FONT_SIZE_GAP.grid(row=6, column=0, sticky=E)
        # self.ENTRY_NORMAL_FONT_SIZE_GAP = Entry(self.frame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP, width=4)
        # self.ENTRY_NORMAL_FONT_SIZE_GAP.grid(row=6, column=1, sticky=W)
        # self.LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Label(self.frame, text="Penalty For Spaces:")
        # self.TOOLTIP_NORMAL_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(self.LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES,
        #                                                              "This determines how large the gaps are between words in each message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
        # self.LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=0, sticky=E)
        # self.ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Entry(self.frame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES, width=4)
        # self.ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=1, sticky=W)
        self.LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Label(self.frame, text="Normal Message Max. Length:")
        self.TOOLTIP_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = CreateToolTip(self.LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE,
                                                                     "When a message is longer than this many characters,\nit becomes a 'Long Message' and those settings apply.")
        self.LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=6, column=0, sticky=E)
        maxLengthFrame = Frame(self.frame)
        self.ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Entry(maxLengthFrame, textvariable=fields.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE, width=4)
        self.ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=0, column=0, sticky=W)
        Label(maxLengthFrame, text="characters").grid(row=0, column=1, sticky=W)
        maxLengthFrame.grid(row=6, column=1, sticky=W)

        self.LABEL_SMALLER_FONT_SIZE = Label(self.frame, text="Long Message Font Size:")
        self.TOOLTIP_SMALLER_FONT_SIZE = CreateToolTip(self.LABEL_SMALLER_FONT_SIZE, "Font size for messages of greater than normal message max length.")
        self.LABEL_SMALLER_FONT_SIZE.grid(row=7, column=0, sticky=E)
        self.ENTRY_SMALLER_FONT_SIZE = Entry(self.frame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE, width=4)
        self.ENTRY_SMALLER_FONT_SIZE.grid(row=7, column=1, sticky=W)

        # Label(self.frame, text="Message Style:").grid(row=2, column=6, sticky=E)
        # self.ENTRY_MESSAGE_STYLE = Entry(self.frame)
        # self.ENTRY_MESSAGE_STYLE.insert(0, settings.MESSAGE_STYLE)
        # self.ENTRY_MESSAGE_STYLE.grid(row=2, column=7, sticky=W)

        self.LABEL_MOVE_ALL_ON_LINE_DELAY = Label(self.frame, text="Message Scroll Speed:")
        self.LABEL_MOVE_ALL_ON_LINE_DELAY.grid(row=8, column=0, sticky=E)
        self.MESSAGE_SPEEDS = ["Fastest", "Fast", "Normal", "Slow", "Slowest"]
        self.MESSAGE_SPEED_COMBO_BOX = ttk.Combobox(self.frame, values=self.MESSAGE_SPEEDS, textvariable=fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY, state="readonly")
        self.MESSAGE_SPEED_COMBO_BOX.grid(row=8, column=1, sticky=W)

        # Label(self.frame, text="Long Message Font Settings").grid(row=6, column=2, sticky=W)
        # self.LABEL_SMALLER_FONT_SIZE_GAP = Label(self.frame, text="Font Gap Size:")
        # self.TOOLTIP_SMALLER_FONT_SIZE_GAP = CreateToolTip(self.LABEL_SMALLER_FONT_SIZE_GAP,
        #                                                    "This is the number of pixels between each character in a long message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
        # self.LABEL_SMALLER_FONT_SIZE_GAP.grid(row=6, column=2, sticky=E)
        # self.ENTRY_SMALLER_FONT_SIZE_GAP = Entry(self.frame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP, width=4)
        # self.ENTRY_SMALLER_FONT_SIZE_GAP.grid(row=6, column=3, sticky=W)
        # self.LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Label(self.frame, text="Penalty For Spaces:")
        # self.TOOLTIP_SMALLER_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(self.LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES,
        #                                                               "This determines how large the gaps are between words in each long message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
        # self.LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=2, sticky=E)
        # self.ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Entry(self.frame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES, width=4)
        # self.ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=3, sticky=W)

        self.frame.grid(row=0, column=2, sticky=NSEW, padx=4, pady=4)

    def updateMessageColor(self, label, fields):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(color[1])
            fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = color[1]
            label.configure(foreground=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
