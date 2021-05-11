from tkinter import Frame, GROOVE, E

from utils.hoverButton import HoverButton

class ChallongeOkCancelFrame:
    def __init__(self, challongeWindow):
        self.frame = Frame(challongeWindow.master)
        self.window = challongeWindow

        self.okButton = HoverButton(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.window.generateChallongeMessages(self.window.challongeFrame.url.get()))
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = HoverButton(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)
