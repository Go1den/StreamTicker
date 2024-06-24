from tkinter import Frame, GROOVE, DISABLED, NORMAL

from utils.hoverButton import HoverButton

class TemplateMakerButtonFrame:
    def __init__(self, templateMakerPartFrame):
        self.frame = Frame(templateMakerPartFrame.frame)
        self.window = templateMakerPartFrame.parent
        self.templateMakerPartFrame = templateMakerPartFrame

        ROW_UP = 0
        ROW_DOWN = 1
        ROW_ADD = 2
        ROW_EDIT = 3
        ROW_COPY = 4
        ROW_DELETE = 5
        BUTTON_WIDTH = 10
        BUTTON_BORDER = 2
        COLUMN = 0
        PADY = 4

        self.upButton = HoverButton(self.frame, text="Move Up", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.moveSelectedUp())
        self.upButton.grid(row=ROW_UP, column=COLUMN, pady=(1, 4))

        self.downButton = HoverButton(self.frame, text="Move Down", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.moveSelectedDown())
        self.downButton.grid(row=ROW_DOWN, column=COLUMN, pady=PADY)

        self.addButton = HoverButton(self.frame, text="New", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.getMessageComponentWindow(False))
        self.addButton.grid(row=ROW_ADD, column=COLUMN, pady=PADY)

        self.editButton = HoverButton(self.frame, text="Edit", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.getMessageComponentWindow(True))
        self.editButton.grid(row=ROW_EDIT, column=COLUMN, pady=PADY)

        self.copyButton = HoverButton(self.frame, text="Copy", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.copySelected())
        self.copyButton.grid(row=ROW_COPY, column=COLUMN, pady=PADY)

        self.deleteButton = HoverButton(self.frame, text="Delete", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.templateMakerPartFrame.listFrame.deleteSelected())
        self.deleteButton.grid(row=ROW_DELETE, column=COLUMN, pady=PADY)

    def disableButtonsForStreamedText(self):
        self.editButton.config(state=DISABLED)
        self.copyButton.config(state=DISABLED)
        self.deleteButton.config(state=DISABLED)

    def enableButtonsForStreamedText(self):
        self.editButton.config(state=NORMAL)
        self.copyButton.config(state=NORMAL)
        self.deleteButton.config(state=NORMAL)


