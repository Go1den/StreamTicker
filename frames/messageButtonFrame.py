from tkinter import Frame, GROOVE, Button

from messageMakerWindow import MessageMakerWindow

class MessageButtonFrame:
    def __init__(self, master, listFrame):
        self.frame = Frame(master)
        self.parent = master

        ROW_UP = 0
        ROW_DOWN = 1
        ROW_COPY = 2
        ROW_DELETE = 3
        ROW_ADD = 4
        BUTTON_WIDTH = 10

        self.upButton = Button(self.frame, text="Move Up", width=BUTTON_WIDTH, bd=2, relief=GROOVE, command=lambda: listFrame.moveSelectedUp())
        self.upButton.grid(row=ROW_UP, column=0, pady=4)

        self.downButton = Button(self.frame, text="Move Down", width=BUTTON_WIDTH, bd=2, relief=GROOVE, command=lambda: listFrame.moveSelectedDown())
        self.downButton.grid(row=ROW_DOWN, column=0, pady=4)

        self.editButton = Button(self.frame, text="Edit", width=BUTTON_WIDTH, bd=2, relief=GROOVE, command=lambda: listFrame.getMessageMakerWindow(True))
        self.editButton.grid(row=ROW_COPY, column=0, pady=4)

        self.deleteButton = Button(self.frame, text="Delete", width=BUTTON_WIDTH, bd=2, relief=GROOVE, command=lambda: listFrame.deleteSelected())
        self.deleteButton.grid(row=ROW_DELETE, column=0, pady=4)

        self.addButton = Button(self.frame, text="New", width=BUTTON_WIDTH, bd=2, relief=GROOVE, command=lambda: listFrame.getMessageMakerWindow(False))
        self.addButton.grid(row=ROW_ADD, column=0, pady=4)

    def getMessageMakerWindowForSelected(self, currentSelection):
        # TODO: Get the current index's record from the json and send values into the message maker window

        MessageMakerWindow(self.parent, None)
