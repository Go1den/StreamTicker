from tkinter import Frame, GROOVE, Label, Entry, E, W, Button

class MessageMakerFrame:
    def __init__(self, master, existingMessage):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        labelMessageSettings = Label(self.frame, text="Message Settings:")
        labelMessageSettings.grid(row=0, column=0, sticky=W)

        labelNickname = Label(self.frame, text="Nickname this message:")
        labelNickname.grid(row=1, column=0, sticky=E)

        entryNickname = Entry(self.frame)
        entryNickname.grid(row=1, column=1, sticky=W)

        labelPrefix = Label(self.frame, text="Message Prefix:")
        labelPrefix.grid(row=2, column=0, sticky=E)

        entryPrefix = Entry(self.frame)
        entryPrefix.grid(row=2, column=1, sticky=W)

        buttonTextFile = Button(self.frame, text="(Optional) Select Text File")
        buttonTextFile.grid(row=3, column=0, sticky=E)

        entryTextFile = Entry(self.frame)
        entryTextFile.grid(row=3, column=1, sticky=W)

        labelSuffix = Label(self.frame, text="Message Suffix:")
        labelSuffix.grid(row=4, column=0, sticky=E)

        entrySuffix = Entry(self.frame)
        entrySuffix.grid(row=4, column=1, sticky=W)
