import sys
from tkinter import Frame, GROOVE, Label, Button, W, E, colorchooser, filedialog, Canvas

from utils import helperMethods

class BackgroundFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master, bd=2, relief=GROOVE)

        ROW_BG_SETTINGS = 0
        ROW_BG_COLOR = 1
        ROW_BG_IMAGE = 2

        bgColorFrame = Frame(self.frame)
        self.LABEL_WINDOW_BG_COLOR = Label(bgColorFrame, textvariable=fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT)
        Label(self.frame, text="Background Settings").grid(row=ROW_BG_SETTINGS, column=0, sticky=W)
        self.BUTTON_WINDOW_BG_COLOR = Button(self.frame, text='Background Color:', command=lambda: self.updateWindowColor(fields))
        self.BUTTON_WINDOW_BG_COLOR.grid(row=ROW_BG_COLOR, column=0, sticky=E, padx=4)
        self.LABEL_WINDOW_BG_COLOR.grid(row=0, column=1, sticky=W)
        self.LABEL_WINDOW_BG_IMAGE = Label(self.frame, textvariable=fields.VAR_DISPLAY_WINDOW_BG_IMAGE, width=20, anchor=W)
        self.BUTTON_WINDOW_BG_IMAGE = Button(self.frame, text='Background Image:', command=lambda: self.selectImageFile(fields))
        self.BUTTON_WINDOW_BG_IMAGE.grid(row=ROW_BG_IMAGE, column=0, sticky=E, padx=4, pady=4)
        self.LABEL_WINDOW_BG_IMAGE.grid(row=ROW_BG_IMAGE, column=1, sticky=W)
        self.CANVAS_WINDOW_BG_IMAGE = Canvas(bgColorFrame, width=80, height=30)
        self.RECTANGLE_WINDOW_BG_IMAGE = self.CANVAS_WINDOW_BG_IMAGE.create_rectangle(80, 4, 0, 30, fill=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND, outline="")
        self.CANVAS_WINDOW_BG_IMAGE.grid(row=0, column=0, sticky=W)
        bgColorFrame.grid(row=ROW_BG_COLOR, column=1, sticky=W)

    def updateWindowColor(self, fields):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(color[1])
            fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = color[1]
            self.CANVAS_WINDOW_BG_IMAGE.itemconfig(self.RECTANGLE_WINDOW_BG_IMAGE, fill=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)

    def selectImageFile(self, fields):
        filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
        fields.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(filename))
        fields.VAR_PATH_WINDOW_BG_IMAGE.set(filename)
