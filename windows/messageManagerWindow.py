from copy import deepcopy
from tkinter import Toplevel, E

from frames.messageManagerButtonFrame import MessageButtonFrame
from frames.messageManagerListFrame import MessageManagerListFrame
from frames.messageOkCancelFrame import MessageOkCancelFrame

class MessageManagerWindow:
    def __init__(self, parent):
        self.master = Toplevel(parent)
        self.master.withdraw()
        self.master.geometry('+{x}+80'.format(x=parent.winfo_x()))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Manager")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()

        self.window = parent

        self.cancelMessages = deepcopy(self.window.messages)
        self.messages = sorted(self.window.messages, key=lambda x: x.sortOrder)

        self.mlFrame = MessageManagerListFrame(self)
        self.mlFrame.frame.grid(row=0, column=1, padx=(4, 4), pady=4)

        self.mbFrame = MessageButtonFrame(self)
        self.mbFrame.frame.grid(row=0, column=0, padx=(4, 0), pady=4)

        self.okFrame = MessageOkCancelFrame(self)
        self.okFrame.frame.grid(row=1, column=1, padx=4, pady=4, sticky=E)

        self.master.deiconify()
        self.master.mainloop()
