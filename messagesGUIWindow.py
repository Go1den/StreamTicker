from tkinter import Toplevel, E

from frames.messageButtonFrame import MessageButtonFrame
from frames.messageListFrame import MessageListFrame
from frames.messageOkCancelFrame import MessageOkCancelFrame

def getMessagesWindow(parent):
    master = Toplevel(parent)
    master.wm_attributes("-topmost", 1)
    master.wm_title("StreamTicker Message Manager")
    master.iconbitmap("stIcon.ico")
    master.resizable(False, False)
    master.grab_set()

    mlFrame = MessageListFrame(master)
    mlFrame.frame.grid(row=0, column=1, padx=(4, 4), pady=4)

    mbFrame = MessageButtonFrame(master, mlFrame)
    mbFrame.frame.grid(row=0, column=0, padx=(4, 0), pady=4)

    okFrame = MessageOkCancelFrame(master)
    okFrame.frame.grid(row=1, column=1, padx=4, pady=4, sticky=E)

    master.mainloop()
