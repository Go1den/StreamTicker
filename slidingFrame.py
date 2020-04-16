from tkinter import Frame, GROOVE, Label, Scale, W, HORIZONTAL, NSEW

class SlidingFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        self.LABEL_WINDOW_SETTINGS = Label(self.frame, text="Window Settings")
        self.LABEL_WINDOW_SETTINGS.grid(row=0, column=1, sticky=W)
        self.SCALE_WINDOW_WIDTH = Scale(self.frame, variable=fields.VAR_ENTRY_WINDOW_WIDTH, from_=400, to=1920, tickinterval=1520, orient=HORIZONTAL, resolution=4, length=500,
                                        command=lambda x: self.updateXScales(), label="Window Width in Pixels:")
        self.SCALE_WINDOW_WIDTH.grid(row=1, column=1, sticky=W)

        self.SCALE_IMAGE_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_IMAGE_X_POS, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=1, length=500,
                                       label="Image X Coordinate (location of image center)")
        self.SCALE_IMAGE_X_POS.grid(row=1, column=3, sticky=W)

        self.SCALE_MESSAGE_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_MESSAGE_X_POS, from_=0, to=400, tickinterval=40, orient=HORIZONTAL, resolution=1, length=500,
                                         label="Message X Coordinate (location of message start)")
        self.SCALE_MESSAGE_X_POS.grid(row=2, column=1, sticky=W)

        self.SCALE_BG_X_POS = Scale(self.frame, variable=fields.VAR_ENTRY_BACKGROUND_X_POS, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=1, length=500,
                                    label="Background X Coordinate (location of BG center)")
        self.SCALE_BG_X_POS.grid(row=2, column=3, sticky=W)

        self.SCALE_WINDOW_HEIGHT = Scale(self.frame, variable=fields.VAR_ENTRY_WINDOW_HEIGHT, from_=40, to=1080, tickinterval=1040, orient=HORIZONTAL, resolution=4, length=500,
                                         command=lambda x: self.updateYScales(), label="Window Height in Pixels:")
        self.SCALE_WINDOW_HEIGHT.grid(row=3, column=1, sticky=W)

        self.SCALE_BG_Y_POS = Scale(self.frame, variable=fields.VAR_ENTRY_BACKGROUND_Y_POS, from_=0, to=40, tickinterval=40, orient=HORIZONTAL, resolution=1, length=500,
                                    label="Background Y Coordinate (location of BG center)")
        self.SCALE_BG_Y_POS.grid(row=3, column=3, sticky=W)
        self.frame.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=4, pady=4)

    def updateXScales(self):
        self.SCALE_IMAGE_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())
        self.SCALE_BG_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())
        self.SCALE_MESSAGE_X_POS.configure(to=self.SCALE_WINDOW_WIDTH.get(), tickinterval=self.SCALE_WINDOW_WIDTH.get())

    def updateYScales(self):
        self.SCALE_BG_Y_POS.configure(to=self.SCALE_WINDOW_HEIGHT.get(), tickinterval=self.SCALE_WINDOW_HEIGHT.get())
