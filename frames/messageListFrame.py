from tkinter import Frame, Listbox, Scrollbar, NS, VERTICAL

class MessageListFrame:
    def __init__(self, master):
        self.frame = Frame(master)

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listBox = Listbox(self.frame, activestyle="none", width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listBox.yview)
        self.scrollbar.grid(row=0, column=1, sticky=NS)

        self.listBox.insert(1, "Test 1")
        self.listBox.insert(2, "Test 2")
        self.listBox.insert(3, "Test 3")
        self.listBox.insert(4, "Test 4")
        self.listBox.insert(5, "Test 5")
        self.listBox.insert(6, "Test 6")
        self.listBox.insert(7, "Test 7")
        self.listBox.insert(8, "Test 8")
        self.listBox.insert(9, "Test 9")
        self.listBox.insert(10, "Test 10")
        self.listBox.insert(11, "Test 11")
        self.listBox.insert(12, "Test 12")
        self.listBox.insert(13, "Test 13")

        self.listBox.grid(row=0, column=0)

    def moveSelectedUp(self):
        idx = self.listBox.curselection()
        if idx and idx[0] != 0:
            text = self.listBox.get(idx[0])
            self.listBox.delete(idx[0])
            self.listBox.insert(idx[0] - 1, text)
            self.listBox.selection_set(idx[0] - 1)
            self.listBox.see(idx[0] - 2)

    def moveSelectedDown(self):
        idx = self.listBox.curselection()
        if idx and idx[0] != self.listBox.size() - 1:
            text = self.listBox.get(idx[0])
            self.listBox.delete(idx[0])
            self.listBox.insert(idx[0] + 1, text)
            self.listBox.selection_set(idx[0] + 1)
            self.listBox.see(idx[0] + 2)

    def deleteSelected(self):
        idx = self.listBox.curselection()
        if idx:
            self.listBox.delete(idx)
            self.listBox.selection_set(idx)
            self.listBox.see(idx)
