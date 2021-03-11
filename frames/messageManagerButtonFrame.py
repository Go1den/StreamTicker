from tkinter import Frame, GROOVE, Button

class MessageButtonFrame:
    def __init__(self, messageManagerWindow):
        self.frame = Frame(messageManagerWindow.master)
        self.window = messageManagerWindow

        ROW_UP = 0
        ROW_DOWN = 1
        ROW_COPY = 2
        ROW_DELETE = 3
        ROW_ADD = 4
        BUTTON_WIDTH = 10
        BUTTON_BORDER = 2
        COLUMN = 0
        PADY = 4

        self.upButton = Button(self.frame, text="Move Up", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.window.mlFrame.moveSelectedUp())
        self.upButton.grid(row=ROW_UP, column=COLUMN, pady=PADY)

        self.downButton = Button(self.frame, text="Move Down", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.window.mlFrame.moveSelectedDown())
        self.downButton.grid(row=ROW_DOWN, column=COLUMN, pady=PADY)

        self.editButton = Button(self.frame, text="Edit", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.window.mlFrame.getMessageMakerWindow(True))
        self.editButton.grid(row=ROW_COPY, column=COLUMN, pady=PADY)

        self.deleteButton = Button(self.frame, text="Delete", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.window.mlFrame.deleteSelected())
        self.deleteButton.grid(row=ROW_DELETE, column=COLUMN, pady=PADY)

        self.addButton = Button(self.frame, text="New", width=BUTTON_WIDTH, bd=BUTTON_BORDER, relief=GROOVE, command=lambda: self.window.mlFrame.getMessageMakerWindow(False))
        self.addButton.grid(row=ROW_ADD, column=COLUMN, pady=PADY)