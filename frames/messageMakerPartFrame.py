from tkinter import Frame, GROOVE, NSEW, Label, W

from frames.messageMakerButtonFrame import MessageMakerButtonFrame
from frames.messageMakerListFrame import MessageMakerListFrame

class MessageMakerPartFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.master, bd=2, relief=GROOVE)

        labelPartFrame = Label(self.frame, text="Message Components:")
        labelPartFrame.grid(row=0, column=0, columnspan=2, sticky=W, padx=1, pady=1)

        self.buttonFrame = MessageMakerButtonFrame(self)
        self.buttonFrame.frame.grid(row=1, column=0, sticky=NSEW, padx=4, pady=4)

        self.listFrame = MessageMakerListFrame(self)
        self.listFrame.frame.grid(row=1, column=1, sticky=NSEW, padx=4, pady=4)
