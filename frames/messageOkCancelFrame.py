from tkinter import Frame, Button, E, GROOVE

class MessageOkCancelFrame:
    def __init__(self, master):
        self.frame = Frame(master)

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE)
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)
