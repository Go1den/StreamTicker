from tkinter import *

from PIL import Image as ImagePIL
from PIL import ImageTk

FILE_CONTENTS = ""

def clearAllFields():
    nickname.delete(0, END)
    prefix.delete(0, END)
    text.delete(0, END)
    suffix.delete(0, END)
    filepath.delete(0, END)
    imagepath.delete(0, END)

def addMessage():
    if validateMessage():
        try:
            with open("messages.txt", "a") as f:
                f.write("Test")
            currentStatus.configure(text="Message added!")
            addMessageButton.configure(state=DISABLED)
            clearAllFields()
        except FileNotFoundError:
            currentStatus.configure(text="Unable to write to messages.txt!")

def addNewSlide():
    print("%s%s%s%s" % (prefix.get(), text.get(), FILE_CONTENTS, suffix.get()))

def previewMessage():
    preview.configure(text=prefix.get() + text.get() + FILE_CONTENTS + suffix.get())

def validateMessage():
    if not filepath.get():
        previewMessage()
    if hasNickname() and atLeastOneFieldPopulated() and testReadingImageFile() and testReadingTextFile():
        currentStatus.configure(text="Message is valid and ready to be added!")
        addMessageButton.configure(state=ACTIVE)
        return True
    else:
        addMessageButton.configure(state=DISABLED)
        return False

def hasNickname():
    if not nickname.get():
        currentStatus.configure(text="Please provide a nickname for this message.")
        return False
    return True

def atLeastOneFieldPopulated():
    result = prefix.get() or text.get() or suffix.get() or filepath.get() or imagepath.get()
    if not result:
        currentStatus.configure(text="You can't add a blank message!")
    return result

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
Label(master, text="Nickname this message:").grid(row=1, column=1, sticky=E)
Label(master, text="Message Prefix").grid(row=2, column=1, sticky=E)
Label(master, text="Message Text").grid(row=3, column=1, sticky=E)
Label(master, text="Message Suffix").grid(row=4, column=1, sticky=E)
Label(master, text="Message Preview: ").grid(row=98, column=0, sticky=E)
# Label(master, text="Use Twitch Bit icons").grid(row=5, sticky=E)
Label(master, text="Text filepath:").grid(row=8, column=1, sticky=E)
Label(master, text="Image filepath:").grid(row=10, column=1, sticky=E)
Label(master, text="Current status:").grid(row=97, column=0, sticky=E)

nickname = Entry(master)
prefix = Entry(master)
text = Entry(master)
suffix = Entry(master)
preview = Label(master)
# bits = Checkbutton(master)
filepath = Entry(master)
imagepath = Entry(master)
newLabel = Label(master)
currentStatus = Label(master)

nickname.insert(0, "")
prefix.insert(0, "")
text.insert(0, "")
suffix.insert(0, "")
filepath.insert(0, "")
imagepath.insert(0, "")

nickname.grid(row=1, column=2)
prefix.grid(row=2, column=2)
text.grid(row=3, column=2)
suffix.grid(row=4, column=2)
preview.grid(row=98, column=2, columnspan=2, sticky=W)
# bits.grid(row=5, column=2)
filepath.grid(row=8, column=2)
imagepath.grid(row=10, column=2)
currentStatus.grid(row=97, column=1, columnspan=3, sticky=W)
newLabel.grid(row=98, column=1)

Button(master,
       text='Preview',
       command=previewMessage).grid(row=4,
                                    column=3,
                                    sticky=W,
                                    pady=4, padx=4)

Button(master,
       text='Validate filepath',
       command=testReadingTextFile).grid(row=8,
                                         column=3,
                                         sticky=W,
                                         pady=4, padx=4)

Button(master,
       text='Validate filepath',
       command=testReadingImageFile).grid(row=10,
                                          column=3,
                                          sticky=W,
                                          pady=4, padx=4)

Button(master,
       text='Validate Message',
       command=validateMessage).grid(row=99,
                                     column=0,
                                     pady=4, padx=4)

addMessageButton = Button(master,
                          state=DISABLED,
                          text='Add Message',
                          command=addMessage)
addMessageButton.grid(row=99,
                      column=1,
                      pady=4, padx=4)

Button(master,
       text='Quit',
       command=master.quit).grid(row=99,
                                 column=3,
                                 pady=4, padx=4)

master.mainloop()
mainloop()
