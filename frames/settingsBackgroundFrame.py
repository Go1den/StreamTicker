from os import getcwd
from tkinter import Frame, GROOVE, Label, W, E, colorchooser, filedialog, Canvas, Checkbutton, BooleanVar, NORMAL, DISABLED, SE

from PIL import Image

from objects.settingsGUIFields import SettingsGUIFields
from utils import helperMethods
from utils.hoverButton import HoverButton

class SettingsBackgroundFrame:
    def __init__(self, parent, fields: SettingsGUIFields):
        self.frame = Frame(parent.master, bd=2, relief=GROOVE)
        self.parent = parent
        self.fields = fields

        self.dimensionCheckbutton = BooleanVar()
        self.doNotUseBgCheckbutton = BooleanVar()

        if self.fields.VAR_PATH_WINDOW_BG_IMAGE == "":
            self.doNotUseBgCheckbutton.set(True)

        ROW_BG_SETTINGS = 0
        ROW_BG_COLOR = 1
        ROW_BG_IMAGE = 2
        ROW_SET_DIMENSIONS = 3
        ROW_DO_NOT_USE_BG = 4

        bgColorFrame = Frame(self.frame)

        self.LABEL_WINDOW_BG_COLOR = Label(bgColorFrame, textvariable=fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT)
        Label(self.frame, text="Background Settings").grid(row=ROW_BG_SETTINGS, column=0, sticky=W)

        self.BUTTON_WINDOW_BG_COLOR = HoverButton(self.frame, text='Background Color:', width=15, command=lambda: self.updateWindowColor(fields))
        self.BUTTON_WINDOW_BG_COLOR.grid(row=ROW_BG_COLOR, column=0, sticky=E, padx=4)

        self.LABEL_WINDOW_BG_COLOR.grid(row=0, column=1, sticky=W)

        self.LABEL_WINDOW_BG_IMAGE = Label(self.frame, textvariable=fields.VAR_DISPLAY_WINDOW_BG_IMAGE, width=20, anchor=W)

        self.BUTTON_WINDOW_BG_IMAGE = HoverButton(self.frame, text='Background Image:', width=15, command=lambda: self.selectImageFile(fields))
        self.BUTTON_WINDOW_BG_IMAGE.grid(row=ROW_BG_IMAGE, column=0, sticky=E, padx=4, pady=4)

        self.LABEL_WINDOW_BG_IMAGE.grid(row=ROW_BG_IMAGE, column=1, sticky=W)

        self.CANVAS_WINDOW_BG_IMAGE = Canvas(bgColorFrame, width=80, height=30)

        self.RECTANGLE_WINDOW_BG_IMAGE = self.CANVAS_WINDOW_BG_IMAGE.create_rectangle(80, 4, 0, 30, fill=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND, outline="")

        self.fitWindowFrame = Frame(self.frame)
        self.checkbuttonSetDimensions = Checkbutton(self.fitWindowFrame, text="Fit window to background image", variable=self.dimensionCheckbutton,
                                                    command=lambda: self.updateWindowDimensions())
        self.checkbuttonSetDimensions.grid(row=0, column=0, sticky=W)
        self.fitWindowFrame.grid(row=ROW_SET_DIMENSIONS, column=0, columnspan=2, padx=4, pady=4, sticky=W)

        self.buttonClearImage = HoverButton(self.frame, text='Remove Image', width=15, command=lambda: self.updateBackgroundImage())
        self.buttonClearImage.grid(row=ROW_DO_NOT_USE_BG, column=0, columnspan=3, sticky=SE, padx=4, pady=(0, 4))

        self.CANVAS_WINDOW_BG_IMAGE.grid(row=0, column=0, sticky=W)
        bgColorFrame.grid(row=ROW_BG_COLOR, column=1, sticky=W)

    def updateBackgroundImage(self):
        self.fields.VAR_DISPLAY_WINDOW_BG_IMAGE.set("")
        self.fields.VAR_PATH_WINDOW_BG_IMAGE.set("")

    def updateWindowDimensions(self):
        if self.dimensionCheckbutton.get():
            try:
                filename = self.fields.VAR_PATH_WINDOW_BG_IMAGE.get()
                img = Image.open(filename)
                self.fields.VAR_WINDOW_WIDTH.set(img.size[0])
                self.fields.VAR_WINDOW_HEIGHT.set(img.size[1])

            except Exception:
                self.fields.VAR_WINDOW_WIDTH.set(0)
                self.fields.VAR_WINDOW_HEIGHT.set(0)
            self.parent.sFrame.ENTRY_WINDOW_WIDTH.configure(state=DISABLED)
            self.parent.sFrame.ENTRY_WINDOW_HEIGHT.configure(state=DISABLED)
        else:
            self.parent.sFrame.ENTRY_WINDOW_WIDTH.configure(state=NORMAL)
            self.parent.sFrame.ENTRY_WINDOW_HEIGHT.configure(state=NORMAL)

    def updateWindowColor(self, fields):
        color = colorchooser.askcolor(title="Select color")
        if color[1]:
            fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(color[1])
            fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = color[1]
            self.CANVAS_WINDOW_BG_IMAGE.itemconfig(self.RECTANGLE_WINDOW_BG_IMAGE, fill=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)

    def selectImageFile(self, fields):
        filename = filedialog.askopenfilename(initialdir=getcwd() + "/imagefiles", title="Select image file",
                                              filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg; *.jpeg; *.jpe; *.jfif")])
        if filename:
            fields.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(filename))
            fields.VAR_PATH_WINDOW_BG_IMAGE.set(filename)
            self.updateWindowDimensions()
