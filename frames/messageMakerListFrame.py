from tkinter import Frame, Listbox, Scrollbar, NS, VERTICAL, END

from windows.messageComponentWindow import MessageComponentWindow

class MessageMakerListFrame:
    def __init__(self, messageMakerPartFrame):
        self.frame = Frame(messageMakerPartFrame.frame)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listBox = Listbox(self.frame, activestyle="none", width=40, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=NS)
        self.populateListbox(messageMakerPartFrame.parent.message.parts)
        self.window = messageMakerPartFrame.parent
        self.messageMakerPartFrame = messageMakerPartFrame

        self.listBox.grid(row=0, column=0)

    def moveSelectedUp(self):
        current = self.listBox.curselection()
        if current and current[0] != 0:
            index = current[0]
            text = self.listBox.get(index)
            self.listBox.delete(index)
            self.listBox.insert(index - 1, text)
            self.listBox.selection_set(index - 1)
            self.listBox.see(index - 2)
            self.window.message.parts[index], self.window.message.parts[index - 1] = self.window.message.parts[index - 1], self.window.message.parts[index]

    def moveSelectedDown(self):
        current = self.listBox.curselection()
        if current and current[0] != self.listBox.size() - 1:
            index = current[0]
            text = self.listBox.get(index)
            self.listBox.delete(index)
            self.listBox.insert(index + 1, text)
            self.listBox.selection_set(index + 1)
            self.listBox.see(index + 2)
            self.window.message.parts[index], self.window.message.parts[index + 1] = self.window.message.parts[index + 1], self.window.message.parts[index]

    def deleteSelected(self):
        current = self.listBox.curselection()
        if current:
            index = current[0]
            self.listBox.delete(index)
            self.listBox.selection_set(index)
            self.listBox.see(index)
            del self.window.message.parts[index]
            for part in self.window.message.parts:
                part.sortOrder = self.window.message.parts.index(part) + 1

    def populateListbox(self, parts):
        self.listBox.delete(0, END)
        index = 1
        for part in parts:
            self.listBox.insert(index, part.partType + ": " + part.value)
            index += 1

    def getMessageComponentWindow(self, isEditButton):
        if isEditButton:
            current = self.listBox.curselection()
            if current:
                index = current[0]
                print(self.window.message.parts[index])
                MessageComponentWindow(self, self.window.message.parts[index], index)
            else:
                return
        else:
            MessageComponentWindow(self, None, len(self.window.message.parts) + 1)
            # we should probably store the result somewhere

