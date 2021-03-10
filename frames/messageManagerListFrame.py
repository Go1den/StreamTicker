from tkinter import Frame, Listbox, Scrollbar, NS, VERTICAL

from windows.messageMakerWindow import MessageMakerWindow

class MessageManagerListFrame:
    def __init__(self, messagesGUIWindow):
        self.frame = Frame(messagesGUIWindow.master)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listBox = Listbox(self.frame, activestyle="none", width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=NS)
        self.populateListbox(messagesGUIWindow.messages)
        self.window = messagesGUIWindow

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
                message["sortOrder"] = self.window.messages.index(message) + 1

    def populateListbox(self, messages):
        index = 1
        for message in messages:
            self.listBox.insert(index, message.get("nickname"))
            index += 1

    def getMessageMakerWindow(self, isEditButton):
        if isEditButton:
            current = self.listBox.curselection()
            if current:
                index = current[0]
                print(self.window.messages[index])
                MessageMakerWindow(self, self.window.messages[index])
            else:
                return
        else:
            MessageMakerWindow(self, None)
            # we should probably store the result somewhere

