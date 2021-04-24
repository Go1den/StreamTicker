from tkinter import StringVar, BooleanVar

class GlobalMessageSettings:
    def __init__(self):
        self.VAR_ENTRY_MESSAGE_DURATION = StringVar()
        self.VAR_ENTRY_MESSAGE_INTERMISSION = StringVar()
        self.VAR_FONT_COMBO_BOX = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = StringVar()
        self.VAR_LABEL_MESSAGE_COLOR_TEXT = StringVar()
        self.VAR_ENTRY_NORMAL_FONT_SIZE = StringVar()
        self.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY = StringVar()
        self.VAR_ARRIVAL = StringVar()
        self.VAR_DEPARTURE = StringVar()
        self.VAR_FONT_IS_BOLD = BooleanVar()
        self.VAR_FONT_IS_ITALIC = BooleanVar()
        self.VAR_FONT_IS_OVERSTRIKE = BooleanVar()
        self.VAR_MESSAGE_SHUFFLE = BooleanVar()