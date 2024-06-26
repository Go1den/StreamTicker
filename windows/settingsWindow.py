from tkinter import Toplevel, NSEW, SE

from frames.okCancelFrame import OkCancelFrame
from frames.settingsBackgroundFrame import SettingsBackgroundFrame
from frames.settingsMessageFrame import SettingsMessageFrame
from frames.settingsWindowFrame import SettingsWindowFrame
from frames.template.templateMakerPartFrame import TemplateMakerPartFrame
from objects.message import Message
from objects.settingsGUIFields import SettingsGUIFields

class SettingsWindow:
    def __init__(self, parent):
        self.master = Toplevel(parent)
        self.master.withdraw()
        self.master.geometry('+{x}+{y}'.format(x=parent.winfo_x(), y=parent.winfo_y()))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Settings")
        self.master.iconbitmap("imagefiles/stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.parent = parent
        self.message = Message()
        if parent.settings.defaultTemplate is not None:
            self.message.parts = parent.settings.defaultTemplate.get("parts")

        self.fields = SettingsGUIFields()

        self.mFrame = SettingsMessageFrame(self.master, self.fields)
        self.mFrame.frame.grid(row=0, column=0, rowspan=3, sticky=NSEW, padx=4, pady=4)

        self.bgFrame = SettingsBackgroundFrame(self, self.fields)
        self.bgFrame.frame.grid(row=0, column=1, sticky=NSEW, padx=4, pady=4)

        self.sFrame = SettingsWindowFrame(self.master, self.fields)
        self.sFrame.frame.grid(row=1, column=1, sticky=NSEW, padx=4, pady=4)

        self.tFrame = TemplateMakerPartFrame(self)
        self.tFrame.frame.grid(row=2, column=1, sticky=NSEW, padx=4, pady=4)

        self.okFrame = OkCancelFrame(self)
        self.okFrame.frame.grid(row=3, column=1, sticky=SE, padx=4, pady=4)

        self.fields.loadSettings(self.master, self.parent, self.mFrame, self.bgFrame)

        self.master.deiconify()
        self.master.mainloop()
