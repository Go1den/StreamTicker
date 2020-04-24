from tkinter import Toplevel

from frames.messageMakerFrame import MessageMakerFrame

def getMessageMakerWindow(parent, values):
    master = Toplevel(parent)
    master.wm_attributes("-topmost", 1)
    master.wm_title("StreamTicker Message Maker")
    master.iconbitmap("stIcon.ico")
    master.resizable(False, False)
    master.grab_set()

    mmFrame = MessageMakerFrame(master, values)
    mmFrame.frame.grid(row=0, column=0)
