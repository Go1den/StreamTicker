from tkinter import Toplevel

from frames.messageMakerFrame import MessageMakerFrame

class MessageMakerWindow:
    def __init__(self, parent, existingMessage):
        self.master = Toplevel(parent)
        self.parent = parent
        self.master.geometry('+{x}+{y}'.format(x=parent.winfo_x() + 10, y=parent.winfo_y() + 10))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Maker")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.master.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        mmFrame = MessageMakerFrame(self.master, existingMessage)
        mmFrame.frame.grid(row=0, column=0)

        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parent.lift()
        self.parent.wm_attributes("-topmost", 1)
        self.parent.grab_set()
