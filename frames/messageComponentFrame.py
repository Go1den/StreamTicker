import sys
from tkinter import Frame, GROOVE, Label, W, StringVar, E, Entry, filedialog, Button
from tkinter.ttk import Combobox

from utils import helperMethods

class MessageComponentFrame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent.master, bd=2, relief=GROOVE)

        self.textValue = StringVar()
        self.imageValue = StringVar()
        self.imagePath = StringVar()
        self.fileValue = StringVar()
        self.filePath = StringVar()
        self.gapValue = StringVar()
        self.componentType = StringVar()
        self.componentTypes = ["Text", "Image", "Text From File", "Pixel Gap"]

        labelMessageSettings = Label(self.frame, text="Component Settings")
        labelMessageSettings.grid(row=0, column=0, sticky=W, columnspan=3, padx=1, pady=1)

        labelComponentType = Label(self.frame, text="Component Type:")
        labelComponentType.grid(row=1, column=0, sticky=E, padx=4, pady=4)
        self.comboboxComponentType = Combobox(self.frame, values=self.componentTypes, textvariable=self.componentType, state="readonly")

        self.comboboxComponentType.grid(row=1, column=1, columnspan=2, sticky=W, padx=4, pady=4)

        self.labelTextToDisplay = Label(self.frame, text="Text to Display:")
        self.labelTextToDisplay.grid(row=2, column=0, sticky=E, padx=4, pady=4)
        self.inputTextToDisplay = Entry(self.frame, textvariable=self.textValue, width=40)
        self.inputTextToDisplay.grid(row=2, column=1, columnspan=2, sticky=W, padx=4, pady=4)

        self.labelImage = Label(self.frame, textvariable=self.imagePath, anchor=W)
        self.buttonImage = Button(self.frame, text='Select File', command=lambda: self.selectImageFile(), width=12)
        self.buttonImage.grid(row=3, column=0, sticky=E, padx=4, pady=4)
        self.labelImage.grid(row=3, column=1, columnspan=2, sticky=W)

        self.labelFile = Label(self.frame, textvariable=self.filePath, anchor=W)
        self.buttonFile = Button(self.frame, text='Select File', command=lambda: self.selectTextFile(), width=12)
        self.buttonFile.grid(row=4, column=0, sticky=E, padx=4, pady=4)
        self.labelFile.grid(row=4, column=1, columnspan=2, sticky=W)

        self.labelGap = Label(self.frame, text="Width of Gap:")
        self.labelGap.grid(row=5, column=0, sticky=E, padx=4, pady=(4, 0))
        self.gapFrame = Frame(self.frame)
        self.inputGap = Entry(self.gapFrame, textvariable=self.gapValue, width=4)
        self.inputGap.grid(row=0, column=0, sticky=W, pady=4)
        self.labelGapPixels = Label(self.gapFrame, text="pixels")
        self.labelGapPixels.grid(row=0, column=1, padx=2, sticky=W)
        self.gapFrame.grid(row=5, column=1, columnspan=2, sticky=W, padx=4, pady=4)

        self.comboboxComponentType.bind("<<ComboboxSelected>>", self.updateGrid)
        self.setFields()
        self.updateGrid(None)

    def setFields(self):
        mp = self.parent.messagePart
        if mp:
            self.comboboxComponentType.set(mp.partType)
            if mp.partType == "Text":
                self.textValue.set(mp.value)
            elif mp.partType == "Image":
                self.imagePath.set(helperMethods.getFileNameFromPath(mp.value))
                self.imageValue.set(mp.value)
            elif mp.partType == "Text From File":
                self.filePath.set(helperMethods.getFileNameFromPath(mp.value))
                self.fileValue.set(mp.value)
            elif mp.partType == "Pixel Gap":
                self.gapValue.set(mp.value)

    def hideAllDropdownDependentFields(self):
        self.labelTextToDisplay.grid_remove()
        self.inputTextToDisplay.grid_remove()
        self.labelImage.grid_remove()
        self.buttonImage.grid_remove()
        self.labelFile.grid_remove()
        self.buttonFile.grid_remove()
        self.labelGap.grid_remove()
        self.gapFrame.grid_remove()

    def displayCurrentComponentTypeDependencies(self):
        if self.componentType.get() == "Text":
            self.labelTextToDisplay.grid()
            self.inputTextToDisplay.grid()
        elif self.componentType.get() == "Image":
            self.labelImage.grid()
            self.buttonImage.grid()
        elif self.componentType.get() == "Text From File":
            self.labelFile.grid()
            self.buttonFile.grid()
        elif self.componentType.get() == "Pixel Gap":
            self.labelGap.grid()
            self.gapFrame.grid()

    def updateGrid(self, e):
        self.hideAllDropdownDependentFields()
        self.displayCurrentComponentTypeDependencies()

    def selectImageFile(self):
        filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
        if filename:
            self.imagePath.set(helperMethods.getFileNameFromPath(filename))
            self.imageValue.set(filename)

    def selectTextFile(self):
        filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select text file", filetypes=[("txt files", "*.txt")])
        if filename:
            self.filePath.set(helperMethods.getFileNameFromPath(filename))
            self.fileValue.set(filename)
