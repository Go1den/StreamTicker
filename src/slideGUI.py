from tkinter import *

from PIL import ImageTk
from PIL import Image as ImagePIL

MESSAGE_STRING_EXPLANATION = "If a filepath is provided, the entire message will be joined in this order:\nprefix, message, file's contents, suffix.\nIf no filepath is provided, the entire message will be prefix, message, suffix."
FILE_CONTENTS = ""

def addNewSlide():
    print("%s%s%s%s" % (prefix.get(), text.get(), FILE_CONTENTS, suffix.get()))

def previewMessage():
    preview.configure(text=prefix.get() + text.get() + FILE_CONTENTS + suffix.get())

def testReadingImageFile():
    global newLabel
    if not imagepath.get():
        return True
    try:
        load = ImagePIL.open(imagepath.get())
        render = ImageTk.PhotoImage(load)
        currentStatus.configure(text="Image has a valid filepath!")
        newLabel = Label(master, image=render)
        newLabel.image = render
        newLabel.grid(row=98, column=1, sticky=E)
        return True
    except:
        currentStatus.configure(text="Invalid filepath or image file.")
        newLabel.grid_forget()
        return False

def testReadingTextFile():
    global FILE_CONTENTS
    if not filepath.get():
        return True
    try:
        with open(filepath.get()) as f:
            FILE_CONTENTS = f.read()
            currentStatus.configure(text="Valid filepath for text!")
            previewMessage()
            return True
    except FileNotFoundError:
        currentStatus.configure(text="Invalid filepath for text.")
        FILE_CONTENTS = ""
        return False

master = Tk()
master.wm_title("StreamTicker MessageMaker")
Label(master, text="Create a new message:").grid(row=0, sticky=W)
Label(master, text="Message Prefix").grid(row=1, column=1, sticky=E)
Label(master, text="Message Text").grid(row=2, column=1, sticky=E)
Label(master, text="Message Suffix").grid(row=3, column=1, sticky=E)
Label(master, text="Message Preview: ").grid(row=98, column=0, sticky=E)
# Label(master, text="Use Twitch Bit icons").grid(row=5, sticky=E)
Label(master, text="Text filepath:").grid(row=7, column=1, sticky=E)
Label(master, text="Image filepath:").grid(row=9, column=1, sticky=E)
Label(master, text="Current status:").grid(row=97, column=0, sticky=E)

prefix = Entry(master)
text = Entry(master)
suffix = Entry(master)
preview = Label(master)
# bits = Checkbutton(master)
filepath = Entry(master)
imagepath = Entry(master)
newLabel = Label(master)
currentStatus = Label(master)

prefix.insert(0, "")
text.insert(0, "")
suffix.insert(0, "")
filepath.insert(0, "")
imagepath.insert(0, "")

prefix.grid(row=1, column=2)
text.grid(row=2, column=2)
suffix.grid(row=3, column=2)
preview.grid(row=98, column=2, sticky=W)
# bits.grid(row=5, column=2)
filepath.grid(row=7, column=2)
imagepath.grid(row=9, column=2)
currentStatus.grid(row=97, column=1, columnspan=3, sticky=W)
newLabel.grid(row=98, column=1)

Button(master,
       text='Quit',
       command=master.quit).grid(row=99,
                                 column=1,
                                 sticky=W,
                                 pady=4)

Button(master,
       text='Preview',
       command=previewMessage).grid(row=3,
                                    column=3,
                                    sticky=W,
                                    pady=4)

Button(master,
       text='Validate filepath',
       command=testReadingTextFile).grid(row=7,
                                     column=3,
                                     sticky=W,
                                     pady=4)

Button(master,
       text='Validate filepath',
       command=testReadingImageFile).grid(row=9,
                                     column=3,
                                     sticky=W,
                                     pady=4)

master.mainloop()
mainloop()
