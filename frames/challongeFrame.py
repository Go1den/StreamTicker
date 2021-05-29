from tkinter import Frame, GROOVE, StringVar, Label, Entry, W, Checkbutton, BooleanVar, IntVar
from tkinter.ttk import Combobox

class ChallongeFrame:
    def __init__(self, challongeWindow):
        self.frame = Frame(challongeWindow.master, bd=2, relief=GROOVE)
        self.url = StringVar()
        self.completedCheckbutton = BooleanVar()
        self.inProgressCheckbutton = BooleanVar()
        self.losersBracketCheckbutton = BooleanVar()
        self.prelimsCheckbutton = BooleanVar()
        self.showRecentRoundsOnlyCheckbutton = BooleanVar()
        self.includeShoutoutCheckbutton = BooleanVar()
        self.recentRounds = IntVar()
        self.completedCheckbutton.set(True)
        self.inProgressCheckbutton.set(True)
        self.prelimsCheckbutton.set(True)
        self.losersBracketCheckbutton.set(True)
        self.includeShoutoutCheckbutton.set(True)
        self.recentRounds.set(1)

        self.labelURL = Label(self.frame, text="Enter the Challonge tournament URL:")
        self.labelURL.grid(row=0, column=0, columnspan=3, padx=4, pady=4, sticky=W)

        self.entryURL = Entry(self.frame, textvariable=self.url, width=60)
        self.entryURL.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky=W)

        self.checkButtonComplete = Checkbutton(self.frame, text="Include completed matches", variable=self.completedCheckbutton)
        self.checkButtonComplete.grid(row=2, column=0, columnspan=3, padx=4, pady=(4, 0), sticky=W)

        self.checkButtonComplete = Checkbutton(self.frame, text="Include in-progress matches", variable=self.inProgressCheckbutton)
        self.checkButtonComplete.grid(row=3, column=0, columnspan=3, padx=4, sticky=W)

        self.checkButtonLosersBracket = Checkbutton(self.frame, text="Include losers bracket matches (if they exist)", variable=self.losersBracketCheckbutton)
        self.checkButtonLosersBracket.grid(row=4, column=0, columnspan=3, padx=4, sticky=W)

        self.checkButtonPrelims = Checkbutton(self.frame, text="Include group stage/pools matches (if they exist)", variable=self.prelimsCheckbutton)
        self.checkButtonPrelims.grid(row=5, column=0, columnspan=3, padx=4, sticky=W)

        self.recentRoundsFrame = Frame(self.frame)
        self.checkButtonLosersBracket = Checkbutton(self.recentRoundsFrame, text="Include only", variable=self.showRecentRoundsOnlyCheckbutton)
        self.checkButtonLosersBracket.grid(row=0, column=0, sticky=W)

        self.comboboxRecentRounds = Combobox(self.recentRoundsFrame, values=[1, 2, 3], textvariable=self.recentRounds, state="readonly", width=3)
        self.comboboxRecentRounds.grid(row=0, column=1, sticky=W)

        self.checkButtonShoutout = Checkbutton(self.frame, text="Include \"Powered by StreamTicker\" message (we'd appreciate it!)", variable=self.includeShoutoutCheckbutton)
        self.checkButtonShoutout.grid(row=6, column=0, columnspan=3, padx=4, sticky=W)

        self.labelRecentRounds = Label(self.recentRoundsFrame, text="most recent rounds")
        self.labelRecentRounds.grid(row=0, column=2, sticky=W)
        self.recentRoundsFrame.grid(row=7, column=0, columnspan=3, padx=4, pady=(0, 4), sticky=W)


