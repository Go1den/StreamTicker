from tkinter import Label, GROOVE, Frame, PhotoImage, W

class PreviewFrame:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window.master, bd=2, relief=GROOVE)

        self.messagePreviewLabel = Label(self.frame, text="Message Preview")
        self.messagePreviewLabel.grid(row=0, column=0, columnspan=2, sticky=W)

        self.image = PhotoImage(file=self.window.mmFrame.imagePath)

        self.imageLabel = Label(self.frame, image=self.image)
        self.imageLabel.grid(row=1, column=0)

        self.font = (self.window.fields.VAR_FONT_COMBO_BOX.get(), self.window.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get())

        self.messageLabel = Label(self.frame, textvariable=self.window.mmFrame.fullMessage, font=self.font)
        self.messageLabel.grid(row=1, column=1)