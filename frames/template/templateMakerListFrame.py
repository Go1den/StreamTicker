from copy import deepcopy
from tkinter import Frame, Listbox, Scrollbar, NS, VERTICAL, END

from windows.templateComponentWindow import TemplateComponentWindow

class TemplateMakerListFrame:
    def __init__(self, templateMakerPartFrame):
        self.frame = Frame(templateMakerPartFrame.frame)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listBox = Listbox(self.frame, activestyle="none", width=40, height=12, yscrollcommand=self.scrollbar.set)
        self.listBox.bind('<<ListboxSelect>>', self.onSelect)
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=NS)
        self.populateListbox(templateMakerPartFrame.messageParts)
        self.window = templateMakerPartFrame.parent
        self.templateMakerPartFrame = templateMakerPartFrame

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
            self.templateMakerPartFrame.messageParts[index], self.templateMakerPartFrame.messageParts[index - 1] = self.templateMakerPartFrame.messageParts[index - 1], self.templateMakerPartFrame.messageParts[index]

    def moveSelectedDown(self):
        current = self.listBox.curselection()
        if current and current[0] != self.listBox.size() - 1:
            index = current[0]
            text = self.listBox.get(index)
            self.listBox.delete(index)
            self.listBox.insert(index + 1, text)
            self.listBox.selection_set(index + 1)
            self.listBox.see(index + 2)
            self.templateMakerPartFrame.messageParts[index], self.templateMakerPartFrame.messageParts[index + 1] = self.templateMakerPartFrame.messageParts[index + 1], self.templateMakerPartFrame.messageParts[index]

    def deleteSelected(self):
        current = self.listBox.curselection()
        if current:
            index = current[0]
            self.listBox.delete(index)
            self.listBox.selection_set(index)
            self.listBox.see(index)
            del self.templateMakerPartFrame.messageParts[index]
            for part in self.templateMakerPartFrame.messageParts:
                part.sortOrder = self.templateMakerPartFrame.messageParts.index(part) + 1
        self.onSelect(None)

    def copySelected(self):
        current = self.listBox.curselection()
        if current:
            index = current[0]
            copiedPart = deepcopy(self.templateMakerPartFrame.messageParts[index])
            copiedPart.sortOrder = len(self.templateMakerPartFrame.messageParts)
            self.templateMakerPartFrame.messageParts.append(copiedPart)
            self.listBox.select_clear(0, END)
            self.listBox.insert(END, copiedPart.partType + ": " + copiedPart.value)
            self.listBox.selection_set(END)
            self.listBox.see(END)
        self.onSelect(None)

    def populateListbox(self, parts):
        self.listBox.delete(0, END)
        index = 1
        for part in parts:
            try:
                if part.partType == "Streamed Text Line From File":
                    self.listBox.insert(index, part.partType)
                else:
                    self.listBox.insert(index, part.partType + ": " + part.value)
                index += 1
            except:
                continue

    def getMessageComponentWindow(self, isEditButton):
        if isEditButton:
            current = self.listBox.curselection()
            if current:
                index = current[0]
                TemplateComponentWindow(self, self.templateMakerPartFrame.messageParts[index], index)
            else:
                return
        else:
            TemplateComponentWindow(self, None, len(self.templateMakerPartFrame.messageParts) + 1)

    def onSelect(self, event):
        try:
            current = self.listBox.curselection()
            if self.templateMakerPartFrame.messageParts[current[0]].partType == "Streamed Text Line From File":
                self.templateMakerPartFrame.buttonFrame.disableButtonsForStreamedText()
            else:
                self.templateMakerPartFrame.buttonFrame.enableButtonsForStreamedText()
        except IndexError:
            self.templateMakerPartFrame.buttonFrame.enableButtonsForStreamedText()
            return
