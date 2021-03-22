from copy import deepcopy
from tkinter import Toplevel, NSEW, E

from frames.messageComponentFrame import MessageComponentFrame
from frames.messageComponentOkCancelFrame import MessageComponentOkCancelFrame
from objects.messagePart import MessagePart
from validations.validateMessageComponent import validate

class MessageComponentWindow:
    def __init__(self, parent, messagePart: MessagePart, index: int):
        self.parent = parent
        self.parentWindow = parent.window.master
        self.master = Toplevel(self.parentWindow)
        self.master.withdraw()
        self.existingMessagePart = messagePart
        self.messagePart = deepcopy(messagePart)
        self.index = index
        self.master.geometry('+{x}+{y}'.format(x=self.parentWindow.winfo_x() + 10, y=self.parentWindow.winfo_y() + 10))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Component")
        self.master.iconbitmap("imagefiles/stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.master.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        self.componentFrame = MessageComponentFrame(self)
        self.componentFrame.frame.grid(row=0, sticky=NSEW, padx=4, pady=4)

        self.okCancelFrame = MessageComponentOkCancelFrame(self)
        self.okCancelFrame.frame.grid(row=2, column=0, padx=4, pady=4, sticky=E)

        self.master.deiconify()
        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parentWindow.lift()
        self.parentWindow.wm_attributes("-topmost", 1)
        self.parentWindow.grab_set()

    def returnMessageComponent(self):
        if validate(self.componentFrame, self.master):
            if self.existingMessagePart:
                self.parent.messageMakerPartFrame.parent.message.parts[self.index] = MessagePart(self.componentFrame.componentType.get(), self.index, self.componentFrame.getValue())
            else:
                self.existingMessagePart = MessagePart(self.componentFrame.componentType.get(), self.index, self.componentFrame.getValue())
                self.parent.messageMakerPartFrame.parent.message.parts.append(self.existingMessagePart)
            self.parent.populateListbox(self.parent.messageMakerPartFrame.parent.message.parts)
            self.deleteWindow()
