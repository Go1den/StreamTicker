from tkinter import Toplevel, E

from frames.messageFrame import MessageFrame
from frames.messageMakerFrame import MessageMakerFrame
from frames.messageMakerOkCancelFrame import MessageMakerOkCancelFrame
from globalMessageSettings import GlobalMessageSettings

class MessageMakerWindow:
    def __init__(self, parent, existingMessage):
        self.master = Toplevel(parent)
        self.master.withdraw()
        self.parent = parent
        self.master.geometry('+{x}+{y}'.format(x=parent.winfo_x() + 10, y=parent.winfo_y() + 10))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Maker")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.master.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        self.fields = GlobalMessageSettings()
        self.setGlobalMessageSettings()

        self.mmFrame = MessageMakerFrame(self.master, existingMessage)
        self.mmFrame.frame.grid(row=0, column=0, padx=(4, 4), pady=4)

        self.globalMessageSettingsFrame = MessageFrame(self.master, self.fields)
        self.globalMessageSettingsFrame.frame.grid(row=1, column=0, padx=(4, 4), pady=4)

        self.okCancelFrame = MessageMakerOkCancelFrame(self)
        self.okCancelFrame.frame.grid(row=2, column=0, padx=4, pady=4, sticky=E)

        self.master.deiconify()
        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parent.lift()
        self.parent.wm_attributes("-topmost", 1)
        self.parent.grab_set()

    def setGlobalMessageSettings(self):
        self.fields.VAR_ENTRY_MESSAGE_DURATION.set("")
        self.fields.VAR_ENTRY_MESSAGE_INTERMISSION.set("")
        self.fields.VAR_FONT_COMBO_BOX.set("")
        self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND.set("")
        self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set("")
        self.fields.VAR_ENTRY_NORMAL_FONT_SIZE.set("")
        self.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set("")
