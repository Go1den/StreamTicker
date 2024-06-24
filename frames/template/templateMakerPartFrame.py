from tkinter import Frame, GROOVE, NSEW, Label, W

from frames.template.templateMakerButtonFrame import TemplateMakerButtonFrame
from frames.template.templateMakerListFrame import TemplateMakerListFrame
from objects.messagePart import MessagePart

class TemplateMakerPartFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.master, bd=2, relief=GROOVE)
        self.messageParts = [MessagePart(x.get("partType"), x.get("sortOrder"), x.get("value")) for x in self.parent.message.parts]

        labelPartFrame = Label(self.frame, text="Template For Messages Streamed From File:")
        labelPartFrame.grid(row=0, column=0, columnspan=2, sticky=W, padx=1, pady=1)

        self.buttonFrame = TemplateMakerButtonFrame(self)
        self.buttonFrame.frame.grid(row=1, column=0, sticky=NSEW, padx=4, pady=4)

        self.listFrame = TemplateMakerListFrame(self)
        self.listFrame.frame.grid(row=1, column=1, sticky=NSEW, padx=4, pady=4)
