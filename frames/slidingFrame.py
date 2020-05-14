from tkinter import Frame, GROOVE, Label, Scale, W, HORIZONTAL

class SlidingFrame:
    def __init__(self, master, fields):

        SCALE_LENGTH = 530

        self.frame = Frame(master, bd=2, relief=GROOVE)

        self.LABEL_WINDOW_SETTINGS = Label(self.frame, text="Window Settings")
        self.LABEL_WINDOW_SETTINGS.grid(row=0, sticky=W)
        self.SCALE_WINDOW_WIDTH = Scale(self.frame, variable=fields.VAR_ENTRY_WINDOW_WIDTH, from_=400, to=1920, tickinterval=1520, orient=HORIZONTAL, resolution=4, length=SCALE_LENGTH,
                                        command=lambda x: self.updateXScales(), label="Window Width in Pixels:")
        self.SCALE_WINDOW_WIDTH.grid(row=1)

        self.SCALE_IMAGE_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_IMAGE_X_POS, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=1, length=SCALE_LENGTH,
                                       label="Image X Coordinate (location of image center)")
        self.SCALE_IMAGE_X_POS.grid(row=4)

        self.SCALE_MESSAGE_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_MESSAGE_X_POS, from_=0, to=400, tickinterval=40, orient=HORIZONTAL, resolution=1, length=SCALE_LENGTH,
                                         label="Message X Coordinate (location of message start)")
        self.SCALE_MESSAGE_X_POS.grid(row=2)

        self.SCALE_BG_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_BACKGROUND_X_POS, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=1, length=SCALE_LENGTH,
                                    label="Background X Coordinate (location of BG center)")
        self.SCALE_BG_X_POS.grid(row=5)

        self.SCALE_WINDOW_HEIGHT = Scale(self.frame, variable=fields.VAR_ENTRY_WINDOW_HEIGHT, from_=40, to=1080, tickinterval=1040, orient=HORIZONTAL, resolution=4, length=SCALE_LENGTH,
                                         command=lambda x: self.updateYScales(), label="Window Height in Pixels:")
        self.SCALE_WINDOW_HEIGHT.grid(row=3)

        self.SCALE_BG_Y_POS = Scale(self.frame, variable=fields.VAR_ENTRY_BACKGROUND_Y_POS, from_=0, to=40, tickinterval=40, orient=HORIZONTAL, resolution=1, length=SCALE_LENGTH,
                                    label="Background Y Coordinate (location of BG center)")
        self.SCALE_BG_Y_POS.grid(row=6)

    def updateXScales(self):
        self.SCALE_IMAGE_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())
        self.SCALE_BG_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())
        self.SCALE_MESSAGE_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())

    def updateYScales(self):
        self.SCALE_BG_Y_POS.configure(to=self.SCALE_WINDOW_HEIGHT.get(), tickinterval=self.SCALE_WINDOW_HEIGHT.get())
