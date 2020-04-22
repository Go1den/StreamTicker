from tkinter import Toplevel, NSEW, E

from frames.backgroundFrame import BackgroundFrame
from frames.departureFrame import DepartureFrame
from frames.messageFrame import MessageFrame
from frames.okCancelFrame import OkCancelFrame
from frames.slidingFrame import SlidingFrame
from settingsGUIFields import SettingsGUIFields

def getSettingsWindow(parent):
    master = Toplevel(parent)
    master.wm_attributes("-topmost", 1)
    master.wm_title("StreamTicker Settings")
    master.iconbitmap("stIcon.ico")
    master.resizable(False, False)
    master.grab_set()

    fields = SettingsGUIFields()

    dFrame = DepartureFrame(master, fields)
    dFrame.frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4)

    bgFrame = BackgroundFrame(master, fields)
    bgFrame.frame.grid(row=0, column=1, sticky=NSEW, padx=4, pady=4)

    mFrame = MessageFrame(master, fields)
    mFrame.frame.grid(row=0, column=2, sticky=NSEW, padx=4, pady=4)

    sFrame = SlidingFrame(master, fields)
    sFrame.frame.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=4, pady=4)

    okFrame = OkCancelFrame(master, fields)
    okFrame.frame.grid(row=2, column=2, sticky=E, padx=4, pady=4)

    master.mainloop()
