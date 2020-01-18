import json
from tkinter import *

from PIL import Image as ImagePIL
from PIL import ImageTk

from src.settings import DEFAULT_IMAGE

def readFile(file):
    try:
        with open(file, "r") as f:
            contents = f.read()
        return contents
    except:
        return ""

def getAllCheckboxStates():
    idx = 0
    for checkbox in checkboxes:
        if checkbox.get():
            print(idx)
        idx += 1
        print(checkbox.get())

def writeJSON(checkboxes):
    with open("messages.json") as f:
        existingJSON = json.load(f)
    print(existingJSON)
    slides = existingJSON['slides']
    idx = 1
    for slide in slides:
        chkValue = BooleanVar()
        chkValue.set(False)
        chk = Checkbutton(master, var=chkValue)
        checkboxes.append(chkValue)
        chk.grid(row=idx, column=0)
        try:
            load = ImagePIL.open(slide['image'])
            render = ImageTk.PhotoImage(load)
            print("SUCCESS")
        except:
            print("Error")
            load = ImagePIL.open(DEFAULT_IMAGE)
            render = ImageTk.PhotoImage(load)
        newLabel = Label(master, image=render)
        newLabel.image = render
        newLabel.grid(row=idx, column=1, sticky=W)
        Label(master, text=slide['prefixText'] + slide['text'] + readFile(slide['filePath']) + slide['suffixText']).grid(row=idx, column=2, columnspan=2, sticky=W)
        idx += 1
    return idx

master = Tk()
master.geometry("600x400")
master.wm_title("StreamTicker MessageManager")
Label(master, text="Here are your existing messages:").grid(row=0, column=0, columnspan=4, sticky=W)
checkboxes = []
idx = writeJSON(checkboxes)

Button(master,
       text='Delete Selected Messages',
       command=getAllCheckboxStates).grid(row=idx,
                                          column=0,
                                          columnspan=3,
                                          pady=4, padx=4)

Button(master,
       text='Quit',
       command=master.quit).grid(row=idx,
                                 column=3,
                                 pady=4, padx=4)

master.mainloop()
mainloop()
