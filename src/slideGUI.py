import json
import random
from tkinter import *
from tkinter import messagebox, filedialog

from PIL import Image as ImagePIL
from PIL import ImageTk

from src.settings import DEFAULT_IMAGE

FILE_CONTENTS = ""

def selectTextFile():
    filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select text file", filetypes=[("All files", "*")])
    print(filename)
    filepath.configure(text=filename)
    tryReadingTextFile()

def selectImageFile():
    filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
    print(filename)
    imagepath.configure(text=filename)
    tryReadingImageFile()

def writeJSON():
    with open("messages.json") as f:
        existingJSON = json.load(f)
        slides = existingJSON['slides']
        newSlide = constructJSON(len(slides) + 1)
        slides.append(newSlide)
    with open("messages.json", 'w') as f:
        json.dump(existingJSON, f, indent=4)

def constructJSON(sortOrder):
    slide = {
        "image": imagepath.cget("text"),
        "text": text.get(),
        "filePath": filepath.cget("text"),
        "prefixText": prefix.get(),
        "suffixText": suffix.get(),
        "isBitMessage": "False",
        "nickname": nickname.get().upper() + "_" + str(random.randint(0, 999999)),
        "sortOrder": str(sortOrder)
    }
    return slide

def clearAllFields():
    global FILE_CONTENTS
    nickname.delete(0, END)
    prefix.delete(0, END)
    text.delete(0, END)
    suffix.delete(0, END)
    filepath.configure(text="")
    imagepath.configure(text="")
    FILE_CONTENTS = ""
    changeImage(defaultRender)
    previewMessage()

def addMessage():
    if validateMessage(False):
        try:
            writeJSON()
            messagebox.showinfo("Success", "Message added successfully!")
            addMessageButton.configure(state=DISABLED)
            clearAllFields()
        except:
            messagebox.showinfo("Error", "Unable to write to messages.json!")

def addNewSlide():
    print("%s%s%s%s" % (prefix.get(), text.get(), FILE_CONTENTS, suffix.get()))

def previewMessage():
    preview.configure(text=prefix.get() + text.get() + FILE_CONTENTS + suffix.get())

def validateMessage(showResult=True):
    previewMessage()
    if hasNickname() and atLeastOneFieldPopulated() and tryReadingImageFile() and tryReadingTextFile():
        if showResult:
            messagebox.showinfo("Success", "Message is valid and ready to be added!")
        addMessageButton.configure(state=ACTIVE)
        return True
    else:
        addMessageButton.configure(state=DISABLED)
        return False

def hasNickname():
    if not nickname.get():
        messagebox.showinfo("Error", "Please provide a nickname for this message.")
        return False
    else:
        if not nickname.get().isalpha():
            messagebox.showinfo("Error", "Nickname must consist of only letters.")
            return False
    return True

def atLeastOneFieldPopulated():
    result = prefix.get() or text.get() or suffix.get() or filepath.cget("text") or imagepath.cget("text")
    if not result:
        messagebox.showinfo("Error", "You can't add a blank message!")
    return result

def changeImage(img):
    imageDisplay.configure(image=img)
    imageDisplay.image = img

def tryReadingImageFile():
    if not imagepath.cget("text"):
        changeImage(defaultRender)
        return True
    try:
        load = ImagePIL.open(imagepath.cget("text"))
        render = ImageTk.PhotoImage(load)
        changeImage(render)
        return True
    except:
        changeImage(defaultRender)
        messagebox.showinfo("Error", "Invalid filepath or image file.")
        return False

def tryReadingTextFile():
    global FILE_CONTENTS
    if not filepath.cget("text"):
        FILE_CONTENTS = ""
        previewMessage()
        return True
    try:
        with open(filepath.cget("text")) as f:
            FILE_CONTENTS = f.read()
            previewMessage()
            return True
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid filepath or text file.")
        FILE_CONTENTS = ""
        previewMessage()
        return False

master = Tk()
master.wm_title("StreamTicker MessageMaker")
Label(master, text="Create a new message:").grid(row=0, column=1)
Label(master, text="Nickname this message:").grid(row=1, column=0, sticky=E)
Label(master, text="Message Prefix").grid(row=2, column=0, sticky=E)
Label(master, text="Message Text").grid(row=3, column=0, sticky=E)
Label(master, text="Message Suffix").grid(row=4, column=0, sticky=E)
# Label(master, text="Use Twitch Bit icons").grid(row=5, sticky=E)
Label(master, text="Text filepath:").grid(row=8, column=0, sticky=E)
Label(master, text="Image Preview").grid(row=97, column=0, sticky=E)
Label(master, text="Message Preview").grid(row=97, column=1, sticky=E)

nickname = Entry(master)
prefix = Entry(master)
text = Entry(master)
suffix = Entry(master)
preview = Label(master)
# bits = Checkbutton(master)
filepath = Label(master)
imagepath = Label(master)
imageDisplay = Label(master)

nickname.insert(0, "")
prefix.insert(0, "")
text.insert(0, "")
suffix.insert(0, "")

nickname.grid(row=1, column=1)
prefix.grid(row=2, column=1)
text.grid(row=3, column=1)
suffix.grid(row=4, column=1)
preview.grid(row=98, column=1, columnspan=2, sticky=W)
# bits.grid(row=5, column=1)
filepath.grid(row=8, column=1, columnspan=2)
imagepath.grid(row=10, column=1, columnspan=2)
imageDisplay.grid(row=98, column=0, sticky=E)
load = ImagePIL.open(DEFAULT_IMAGE)
defaultRender = ImageTk.PhotoImage(load)
changeImage(defaultRender)
Button(master, text='Preview', command=previewMessage).grid(row=4, column=2, sticky=W, pady=4, padx=4)
Button(master, text='(Optional) Select Text File', command=selectTextFile).grid(row=8, column=0, sticky=E, pady=4)
Button(master, text='(Optional) Select Image', command=selectImageFile).grid(row=10, column=0, sticky=E, pady=4)
Button(master, text='Validate Message', command=validateMessage).grid(row=99, column=0, pady=4, padx=4, sticky=W)
addMessageButton = Button(master, state=DISABLED, text='Add Message', command=addMessage)
addMessageButton.grid(row=99, column=1, pady=4, padx=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=99, column=2, pady=4, padx=4, sticky=E)
master.mainloop()
mainloop()
