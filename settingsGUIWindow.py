from tkinter import Toplevel

from frames.backgroundFrame import BackgroundFrame
from frames.departureFrame import DepartureFrame
from frames.menubar import Menubar
from frames.messageFrame import MessageFrame
from frames.slidingFrame import SlidingFrame
from settingsGUIFields import SettingsGUIFields

def getSettingsWindow():
    master = Toplevel()
    master.wm_title("StreamTicker Settings")
    master.iconbitmap("stIcon.ico")
    master.resizable(False, False)
    master.grab_set()

    fields = SettingsGUIFields()
    dFrame = DepartureFrame(master, fields)
    sFrame = SlidingFrame(master, fields)
    bgFrame = BackgroundFrame(master, fields)
    mFrame = MessageFrame(master, fields)
    menubar = Menubar(master, fields, sFrame, mFrame, bgFrame)
    master.mainloop()
