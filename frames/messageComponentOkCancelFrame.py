from tkinter import Frame, Button, GROOVE, E

class MessageComponentOkCancelFrame:
    def __init__(self, messageComponentWindow):
        self.frame = Frame(messageComponentWindow.master)
        self.window = messageComponentWindow

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.window.returnMessageComponent())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)
