from tkinter import Frame, GROOVE, E

from utils.hoverButton import HoverButton

class TemplateComponentOkCancelFrame:
    def __init__(self, templateComponentWindow):
        self.frame = Frame(templateComponentWindow.master)
        self.window = templateComponentWindow

        self.okButton = HoverButton(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.window.returnMessageComponent())
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = HoverButton(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: self.window.deleteWindow())
        self.cancelButton.grid(row=0, column=1, sticky=E)
