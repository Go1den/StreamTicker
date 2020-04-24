from tkinter import Toplevel

from frames.messageMakerFrame import MessageMakerFrame

def getMessageMakerWindow(parent, values):
    master = Toplevel(parent)
    master.wm_attributes("-topmost", 1)
    master.focus_force()
    master.wm_title("StreamTicker Message Maker")
    master.iconbitmap("stIcon.ico")
    master.resizable(False, False)
    master.grab_set()

    def _delete_window():
        master.destroy()
        parent.lift()
        parent.wm_attributes("-topmost", 1)
        parent.grab_set()

    master.protocol("WM_DELETE_WINDOW", _delete_window)

    mmFrame = MessageMakerFrame(master, values)
    mmFrame.frame.grid(row=0, column=0)
