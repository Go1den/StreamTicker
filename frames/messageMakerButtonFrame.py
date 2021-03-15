from tkinter import Frame, GROOVE, Button

class MessageMakerButtonFrame:
    def __init__(self, messageMakerPartFrame):
        self.frame = Frame(messageMakerPartFrame.frame)
        self.window = messageMakerPartFrame.parent
        self.messageMakerPartFrame = messageMakerPartFrame

        ROW_UP = 0
        ROW_DOWN = 1
        ROW_COPY = 2
        ROW_DELETE = 3
        ROW_ADD = 4
        BUTTON_WIDTH = 10
        BUTTON_BORDER = 2
        COLUMN = 0
        PADY = 4

        self.upButton = Button(self.frame, text="Move Up", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.messageMakerPartFrame.listFrame.moveSelectedUp())
        self.upButton.grid(row=ROW_UP, column=COLUMN, pady=(1, 4))

        self.downButton = Button(self.frame, text="Move Down", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.messageMakerPartFrame.listFrame.moveSelectedDown())
        self.downButton.grid(row=ROW_DOWN, column=COLUMN, pady=PADY)

        self.editButton = Button(self.frame, text="Edit", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.messageMakerPartFrame.listFrame.getMessageComponentWindow(True))
        self.editButton.grid(row=ROW_COPY, column=COLUMN, pady=PADY)

        self.deleteButton = Button(self.frame, text="Delete", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.messageMakerPartFrame.listFrame.deleteSelected())
        self.deleteButton.grid(row=ROW_DELETE, column=COLUMN, pady=PADY)

        self.addButton = Button(self.frame, text="New", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.messageMakerPartFrame.listFrame.getMessageComponentWindow(False))
        self.addButton.grid(row=ROW_ADD, column=COLUMN, pady=PADY)
