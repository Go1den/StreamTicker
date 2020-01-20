import json
from tkinter import *
from tkinter import messagebox

from PIL import Image as ImagePIL
from PIL import ImageTk

from settings import Settings

def getExistingJSON():
    with open("messages.json") as f:
        existingJSON = json.load(f)
    return existingJSON

def writeJSON(existingJSON):
    with open("messages.json", 'w') as f:
        json.dump(existingJSON, f, indent=4)

def writeUpdatedSlidesToJSON():
    existingJSON = getExistingJSON()
    slides = sorted(existingJSON['slides'], key=lambda x: int(x.get('sortOrder')))
    idx = 0
    for checkbox in checkboxes:
        if checkbox.get():
            slides.pop(idx)
        else:
            idx += 1
    existingJSON['slides'] = updateSortOrderNumbersAfterDelete(slides)
    writeJSON(existingJSON)
    messagebox.showinfo("Success", "The selected messages were deleted. The program will now close.")
    sys.exit(1)

def updateSortOrderNumbersAfterDelete(slides):
    idx = 1
    for slide in slides:
        slide['sortOrder'] = str(idx)
        idx += 1
    return slides

def updateSortOrderNumbersOnReorder(existingJSON, newSortOrderNumbers):
    slides = sorted(existingJSON['slides'], key=lambda x: int(x.get('sortOrder')))
    existingSortNumbers = [slide['sortOrder'] for slide in slides]
    dictionary = dict(zip(existingSortNumbers, newSortOrderNumbers))
    print(dictionary)
    for slide in slides:
        slide['sortOrder'] = str(dictionary.get(slide['sortOrder']))
    return sorted(slides, key=lambda x: int(x.get('sortOrder')))

def reorderSlidesToJSON():
    if orderEntries is not []:
        expectedNumbers = list(range(1, len(orderEntries) + 1))
        newSortOrderNumbers = []
        for orderEntry in orderEntries:
            newSortOrderNumbers.append(int(orderEntry.get()))
        if sorted(newSortOrderNumbers) == expectedNumbers:
            existingJSON = getExistingJSON()
            slides = updateSortOrderNumbersOnReorder(existingJSON, newSortOrderNumbers)
            existingJSON['slides'] = slides
            writeJSON(existingJSON)
            messagebox.showinfo("Success", "Messages were reordered successfully. You can confirm this by opening this program again. The program will now close.")
            sys.exit(1)
        else:
            messagebox.showinfo("Error", "Please make sure all numbers between 1 and " + str(len(orderEntries)) + " are present.")
            print("NO MATCH")

def readFile(file):
    try:
        with open(file, "r") as f:
            contents = f.readline().rstrip()
        return contents
    except:
        return ""

def populateTableRows(checkboxes, orderEntries):
    existingJSON = getExistingJSON()
    slides = sorted(existingJSON['slides'], key=lambda x: int(x.get('sortOrder')))
    if len(slides) == 0:
        messagebox.showinfo("Error", "No messages have been created yet. This program will now close.")
        sys.exit(1)
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
        except:
            load = ImagePIL.open(settings.DEFAULT_IMAGE)
            render = ImageTk.PhotoImage(load)
        newLabel = Label(master, image=render)
        newLabel.image = render
        newLabel.grid(row=idx, column=1, sticky=W)
        Label(master, text=slide['prefixText'] + slide['text'] + readFile(slide['filePath']) + slide['suffixText']).grid(row=idx, column=2, columnspan=3, sticky=W)
        orderEntry = Entry(master)
        orderEntries.append(orderEntry)
        orderEntry.insert(0, str(idx))
        orderEntry.grid(row=idx, column=5, columnspan=2)
        idx += 1
    return idx

settings = Settings()
master = Tk()
master.wm_title("StreamTicker MessageManager")
master.iconbitmap("stIcon.ico")
Label(master, text="Here are your existing messages:").grid(row=0, column=0, columnspan=3, sticky=W)
Label(master, text="Message Order").grid(row=0, column=5, columnspan=2)
checkboxes = []
orderEntries = []
idx = populateTableRows(checkboxes, orderEntries)
Button(master, text='Delete Selected + Quit', command=writeUpdatedSlidesToJSON, width=18).grid(row=idx, column=0, columnspan=3, pady=4, padx=4, sticky=W)
Button(master, text='Reorder + Quit', command=reorderSlidesToJSON, width=18).grid(row=idx, column=4, columnspan=2, pady=4, padx=2, sticky=W)
Button(master, text='Quit', command=master.quit, width=5).grid(row=idx, column=6, pady=4, padx=2, sticky=E)
master.mainloop()
mainloop()
