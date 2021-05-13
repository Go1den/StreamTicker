from tkinter import Frame, GROOVE, Label, W, Entry, E, Checkbutton

class SettingsWindowFrame:
    def __init__(self, master, fields):
        self.fields = fields
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_WINDOW_SETTINGS = 0
        ROW_DIMENSIONS = 1
        ROW_MESSAGE_SHUFFLE = 2

        Label(self.frame, text="Window Settings").grid(row=ROW_WINDOW_SETTINGS, column=0, columnspan=3, sticky=W)

        self.frameDimensions = Frame(self.frame)
        self.LABEL_WINDOW_WIDTH = Label(self.frameDimensions, text="Width:")
        self.LABEL_WINDOW_WIDTH.grid(row=0, column=0, sticky=E, pady=1)
        self.ENTRY_WINDOW_WIDTH = Entry(self.frameDimensions, textvariable=self.fields.VAR_WINDOW_WIDTH, width=5)
        self.ENTRY_WINDOW_WIDTH.grid(row=0, column=1, sticky=W, pady=1)
        Label(self.frameDimensions, text="pixels").grid(row=0, column=2, sticky=W, padx=(0, 20), pady=1)

        self.LABEL_WINDOW_HEIGHT = Label(self.frameDimensions, text="Height:")
        self.LABEL_WINDOW_HEIGHT.grid(row=0, column=3, sticky=E, pady=1)
        self.ENTRY_WINDOW_HEIGHT = Entry(self.frameDimensions, textvariable=self.fields.VAR_WINDOW_HEIGHT, width=5)
        self.ENTRY_WINDOW_HEIGHT.grid(row=0, column=4, sticky=W, pady=1)
        Label(self.frameDimensions, text="pixels").grid(row=0, column=5, sticky=W, pady=1)
        self.frameDimensions.grid(row=ROW_DIMENSIONS, sticky=W, pady=1)

        self.frameShuffle = Frame(self.frame)
        self.checkButtonShuffle = Checkbutton(self.frameShuffle, borderwidth=0, text="Display Messages in Random Order", variable=self.fields.VAR_MESSAGE_SHUFFLE)
        self.checkButtonShuffle.grid(pady=1, sticky=W)
        self.frameShuffle.grid(row=ROW_MESSAGE_SHUFFLE, sticky=W, pady=1)
