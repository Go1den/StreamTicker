from tkinter import Frame, GROOVE, Label, Entry, E, W, StringVar

class MessageMakerFrame:
    def __init__(self, master, existingMessage):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        self.message = existingMessage

        self.nickname = StringVar()
        self.populateFieldsOnLoad()

        labelMessageSettings = Label(self.frame, text="Message Settings")
        labelMessageSettings.grid(row=0, column=0, sticky=W, padx=1, pady=1)

        labelNickname = Label(self.frame, text="Nickname this message:")
        labelNickname.grid(row=1, column=0, sticky=E, padx=1, pady=1)

        entryNickname = Entry(self.frame, textvariable=self.nickname, width=35)
        entryNickname.grid(row=1, column=1, sticky=W, padx=1, pady=1)

    def populateFieldsOnLoad(self):
        if self.message:
            self.nickname.set(self.message.nickname)
