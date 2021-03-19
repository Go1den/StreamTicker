from copy import deepcopy
from tkinter import Frame, Listbox, Scrollbar, NS, VERTICAL, END

from windows.messageMakerWindow import MessageMakerWindow

class MessageManagerListFrame:
    def __init__(self, messageManagerWindow):
        self.frame = Frame(messageManagerWindow.master)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listBox = Listbox(self.frame, activestyle="none", width=40, height=12, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=NS)
        self.populateListbox(messageManagerWindow.messages)
        self.window = messageManagerWindow

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
            self.window.messages[index], self.window.messages[index - 1] = self.window.messages[index - 1], self.window.messages[index]

    def moveSelectedDown(self):
        current = self.listBox.curselection()
        if current and current[0] != self.listBox.size() - 1:
            index = current[0]
            text = self.listBox.get(index)
            self.listBox.delete(index)
            self.listBox.insert(index + 1, text)
            self.listBox.selection_set(index + 1)
            self.listBox.see(index + 2)
            self.window.messages[index], self.window.messages[index + 1] = self.window.messages[index + 1], self.window.messages[index]

    def deleteSelected(self):
        current = self.listBox.curselection()
        if current:
            index = current[0]
            self.listBox.delete(index)
            self.listBox.selection_set(index)
            self.listBox.see(index)
            del self.window.messages[index]
            for message in self.window.messages:
                message.sortOrder = self.window.messages.index(message) + 1

    def copySelected(self):
        current = self.listBox.curselection()
        if current:
            index = current[0]
            copiedMessage = deepcopy(self.window.messages[index])
            copiedMessage.sortOrder = len(self.window.messages)
            self.window.messages.append(copiedMessage)
            self.listBox.select_clear(0, END)
            self.listBox.insert(END, copiedMessage.nickname)
            self.listBox.selection_set(END)
            self.listBox.see(END)

    def populateListbox(self, messages):
        self.listBox.delete(0, END)
        index = 1
        for message in messages:
            self.listBox.insert(index, message.nickname)
            index += 1

    def getMessageMakerWindow(self, isEditButton):
        if isEditButton:
            current = self.listBox.curselection()
            if current:
                index = current[0]
                print(self.window.messages[index])
                MessageMakerWindow(self, self.window.messages[index], index)
            else:
                return
        else:
            MessageMakerWindow(self, None, len(self.window.messages) + 1)
            # we should probably store the result somewhere

