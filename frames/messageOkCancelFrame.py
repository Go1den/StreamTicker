from tkinter import Frame, Button, E, GROOVE, messagebox

from utils.hoverButton import HoverButton

class MessageOkCancelFrame:
    def __init__(self, messageManagerWindow):
        self.frame = Frame(messageManagerWindow.master)
        self.window = messageManagerWindow

        self.okButton = HoverButton(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateMessages())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = HoverButton(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.cancel())
        self.cancelButton.grid(row=0, column=1, sticky=E)

    def updateMessages(self):
        for message in self.window.messages:
            message.sortOrder = self.window.messages.index(message) + 1
        self.window.window.messages = self.window.messages
        self.window.master.destroy()

    def cancel(self):
        self.window.window.messages = self.window.cancelMessages
        self.window.master.destroy()


