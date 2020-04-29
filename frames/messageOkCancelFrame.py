from tkinter import Frame, Button, E, GROOVE

class MessageOkCancelFrame:
    def __init__(self, messagesGUIWindow):
        self.frame = Frame(messagesGUIWindow.master)
        self.window = messagesGUIWindow

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateMessages())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)
        # TODO Cancel is not canceling. The order is somehow maintained? Might be writing to the wrong spot

    def updateMessages(self):
        print(self.window.messages)
        self.window.window.messages["slides"] = self.window.messages
        self.window.master.destroy()

