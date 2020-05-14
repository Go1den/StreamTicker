from tkinter import Toplevel, NSEW, E

from frames.backgroundFrame import BackgroundFrame
from frames.messageFrame import MessageFrame
from frames.okCancelFrame import OkCancelFrame
from frames.slidingFrame import SlidingFrame
from settingsGUIFields import SettingsGUIFields

class SettingsGUIWindow:
    def __init__(self, parent):
        self.master = Toplevel(parent)
        self.master.withdraw()
        self.master.geometry('+{x}+80'.format(x=parent.winfo_x()))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Settings")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()

        self.fields = SettingsGUIFields()

        self.mFrame = MessageFrame(self.master, self.fields)
        self.mFrame.frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4)

        self.bgFrame = BackgroundFrame(self.master, self.fields)
        self.bgFrame.frame.grid(row=0, column=1, sticky=NSEW, padx=4, pady=4)

        self.sFrame = SlidingFrame(self.master, self.fields)
        self.sFrame.frame.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=4, pady=4)

        self.okFrame = OkCancelFrame(self.master, self.fields)
        self.okFrame.frame.grid(row=2, column=1, sticky=E, padx=4, pady=4)

        self.master.deiconify()
        self.master.mainloop()
