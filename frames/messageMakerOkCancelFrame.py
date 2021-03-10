from tkinter import Frame, Button, GROOVE, E

class MessageMakerOkCancelFrame:
    def __init__(self, messageMakerWindow):
        self.frame = Frame(messageMakerWindow.master)
        self.window = messageMakerWindow

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateMessage())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)

    def updateMessage(self):
        return
# todo update the existing message, possibly just call this method from within the window itself
