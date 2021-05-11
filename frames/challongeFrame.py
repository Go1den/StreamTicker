from tkinter import Frame, GROOVE, StringVar, Label, Entry, W

class ChallongeFrame:
    def __init__(self, challongeWindow):
        self.frame = Frame(challongeWindow.master, bd=2, relief=GROOVE)
        self.url = StringVar()

        self.labelURL = Label(self.frame, text="Enter the Challonge tournament URL:")
        self.labelURL.grid(row=0, padx=4, pady=4, sticky=W)

        self.entryURL = Entry(self.frame, textvariable=self.url, width=60)
        self.entryURL.grid(row=1, padx=4, pady=4, sticky=W)
