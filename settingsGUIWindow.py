from tkinter import Tk

from backgroundFrame import BackgroundFrame
from departureFrame import DepartureFrame
from menubar import Menubar
from messageFrame import MessageFrame
from settingsGUIFields import SettingsGUIFields
from slidingFrame import SlidingFrame

class SettingsGUIWindow:
    def __init__(self):
        self.master = Tk()
        self.master.wm_title("StreamTicker Settings")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        
        self.fields = SettingsGUIFields()
        self.dFrame = DepartureFrame(self.master, self.fields)
        self.sFrame = SlidingFrame(self.master, self.fields)
        self.bgFrame = BackgroundFrame(self.master, self.fields)
        self.mFrame = MessageFrame(self.master, self.fields)
        self.menubar = Menubar(self.master, self.fields, self.sFrame, self.bgFrame, self.mFrame)
        self.master.mainloop()