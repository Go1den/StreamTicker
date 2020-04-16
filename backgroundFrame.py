import sys
from tkinter import Frame, GROOVE, Label, Button, W, E, NSEW, colorchooser, filedialog

import helperMethods
from createToolTip import CreateToolTip

class BackgroundFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        self.LABEL_WINDOW_BG_COLOR = Label(self.frame, textvariable=fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT, background=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)
        Label(self.frame, text="Background Settings").grid(row=0, column=0, sticky=W)
        self.BUTTON_WINDOW_BG_COLOR = Button(self.frame, text='Background Color:', command=lambda: self.updateWindowColor(self.LABEL_WINDOW_BG_COLOR, fields))
        self.TOOLTIP_WINDOW_BG_COLOR = CreateToolTip(self.BUTTON_WINDOW_BG_COLOR,
                                                     "The background color of the window will show if no background image exists,\nor if the background image does not cover the entire window.")
        self.BUTTON_WINDOW_BG_COLOR.grid(row=1, column=0, sticky=E, padx=4)
        self.LABEL_WINDOW_BG_COLOR.grid(row=1, column=1, sticky=W)
        self.LABEL_WINDOW_BG_IMAGE = Label(self.frame, textvariable=fields.VAR_DISPLAY_WINDOW_BG_IMAGE)
        self.BUTTON_WINDOW_BG_IMAGE = Button(self.frame, text='Background Image:', command=lambda: self.selectImageFile(fields))
        self.TOOLTIP_WINDOW_BG_IMAGE = CreateToolTip(self.BUTTON_WINDOW_BG_IMAGE,
                                                     "The background image will persist during all messages.\nSet its coordinates with BG X Coord and BG Y Coord.")
        self.BUTTON_WINDOW_BG_IMAGE.grid(row=2, column=0, sticky=E, padx=4, pady=4)
        self.LABEL_WINDOW_BG_IMAGE.grid(row=2, column=1, sticky=W)
        self.frame.grid(row=0, column=1, sticky=NSEW, padx=4, pady=4)

    def updateWindowColor(self, label, fields):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(color[1])
            fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = color[1]
            label.configure(background=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)

    def selectImageFile(self, fields):
        filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
        fields.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(filename))
        fields.VAR_PATH_WINDOW_BG_IMAGE.set(filename)
