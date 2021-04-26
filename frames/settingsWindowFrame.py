from tkinter import Frame, GROOVE, Label, W, Entry, E, Checkbutton

class SettingsWindowFrame:
    def __init__(self, master, fields):
        self.fields = fields
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_WINDOW_SETTINGS = 0
        ROW_WIDTH = 1
        ROW_HEIGHT = 2        
        ROW_MESSAGE_SHUFFLE = 3

        Label(self.frame, text="Window Settings").grid(row=ROW_WINDOW_SETTINGS, column=0, columnspan=3, sticky=W)

        self.LABEL_WINDOW_WIDTH = Label(self.frame, text="Width:")
        self.LABEL_WINDOW_WIDTH.grid(row=ROW_WIDTH, column=0, sticky=E, pady=1)
        self.ENTRY_WINDOW_WIDTH = Entry(self.frame, textvariable=self.fields.VAR_WINDOW_WIDTH, width=5)
        self.ENTRY_WINDOW_WIDTH.grid(row=ROW_WIDTH, column=1, sticky=W, pady=1)
        Label(self.frame, text="pixels").grid(row=ROW_WIDTH, column=2, sticky=W, pady=1)

        self.LABEL_WINDOW_HEIGHT = Label(self.frame, text="Height:")
        self.LABEL_WINDOW_HEIGHT.grid(row=ROW_HEIGHT, column=0, sticky=E, pady=1)
        self.ENTRY_WINDOW_HEIGHT = Entry(self.frame, textvariable=self.fields.VAR_WINDOW_HEIGHT, width=5)
        self.ENTRY_WINDOW_HEIGHT.grid(row=ROW_HEIGHT, column=1, sticky=W, pady=1)
        Label(self.frame, text="pixels").grid(row=ROW_HEIGHT, column=2, sticky=W, pady=1)

        self.checkButtonShuffle = Checkbutton(self.frame, borderwidth=0, text="Shuffle Message Order", variable=self.fields.VAR_MESSAGE_SHUFFLE)
        self.checkButtonShuffle.grid(row=ROW_MESSAGE_SHUFFLE, column=0, pady=1, sticky=E)
