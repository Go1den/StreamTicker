from tkinter import Frame, GROOVE, Label, Entry, E, W, StringVar

class MessageMakerFrame:
    def __init__(self, master, existingMessage):
        self.frame = Frame(master, bd=2, relief=GROOVE)
        self.message = existingMessage
        print("Current message:")
        print(self.message)

        self.nickname = StringVar()
        self.populateFieldsOnLoad()

        labelMessageSettings = Label(self.frame, text="Message Settings")
        labelMessageSettings.grid(row=0, column=0, sticky=W, padx=1, pady=1)

        labelNickname = Label(self.frame, text="Nickname this message:")
        labelNickname.grid(row=1, column=0, sticky=E, padx=1, pady=1)

        entryNickname = Entry(self.frame, textvariable=self.nickname, width=30)
        entryNickname.grid(row=1, column=1, sticky=W, padx=1, pady=1)

        # buttonTextFile = Button(self.frame, text="Select Text File")
        # buttonTextFile.grid(row=3, column=0, sticky=E, padx=1, pady=1)
        #
        # labelTextFile = Label(self.frame, textvariable=self.file)
        # labelTextFile.grid(row=3, column=1, sticky=W, padx=1, pady=1)
        #
        # labelSuffix = Label(self.frame, text="Message Suffix:")
        # labelSuffix.grid(row=4, column=0, sticky=E, padx=1, pady=1)
        #
        # entrySuffix = Entry(self.frame, textvariable=self.suffix, width=30)
        # entrySuffix.grid(row=4, column=1, sticky=W, padx=1, pady=1)
        #
        # buttonImageFile = Button(self.frame, text="Select Image File")
        # buttonImageFile.grid(row=5, column=0, sticky=E, padx=1, pady=(1, 4))
        #
        # labelImageFile = Label(self.frame, textvariable=self.image)
        # labelImageFile.grid(row=5, column=1, sticky=W, padx=1, pady=1)

    def populateFieldsOnLoad(self):
        if self.message:
            self.nickname.set(self.message.get("nickname"))
