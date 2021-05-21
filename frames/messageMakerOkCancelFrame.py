from tkinter import Frame, GROOVE, E

from utils.hoverButton import HoverButton

class MessageMakerOkCancelFrame:
    def __init__(self, messageMakerWindow):
        self.frame = Frame(messageMakerWindow.master)
        self.window = messageMakerWindow

        self.okButton = HoverButton(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.window.updateMessage())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = HoverButton(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.deleteWindow())
        self.cancelButton.grid(row=0, column=1, sticky=E)
