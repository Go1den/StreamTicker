from tkinter import Toplevel, E, NSEW

from frames.settingsMessageFrame import MessageFrame
from frames.messageMakerFrame import MessageMakerFrame
from frames.messageMakerOkCancelFrame import MessageMakerOkCancelFrame
from frames.overrideFrame import OverrideFrame
from settings.globalMessageSettings import GlobalMessageSettings

class MessageMakerWindow:
    def __init__(self, listFrame, message):
        self.master = Toplevel(listFrame.window.master)
        self.master.withdraw()
        self.listFrame = listFrame
        self.parent = listFrame.window.master
        self.message = message
        self.isNewMessage = message is None
        self.master.geometry('+{x}+{y}'.format(x=self.parent.winfo_x() + 10, y=self.parent.winfo_y() + 10))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Maker")
        self.master.iconbitmap("stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.master.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        print("Message list from the list frame:")
        print(self.listFrame.window.messages)
        print("Global settings can be found at:")
        print(self.listFrame.window.window.settings)

        self.fields = GlobalMessageSettings()
        self.setGlobalMessageSettings()

        self.mmFrame = MessageMakerFrame(self.master, self.message)
        self.mmFrame.frame.grid(row=0, column=0, sticky=NSEW, columnspan=2, padx=4, pady=4)

        self.globalMessageSettingsFrame = MessageFrame(self.master, self.fields)
        self.globalMessageSettingsFrame.frame.grid(row=1, column=1, sticky=NSEW, padx=(0, 4), pady=4)

        self.overrideFrame = OverrideFrame(self.master, self.globalMessageSettingsFrame, self.listFrame.window.window.settings)
        self.overrideFrame.frame.grid(row=1, column=0, sticky=NSEW, padx=4, pady=4)

        self.disableGlobalMessageFields()

        self.okCancelFrame = MessageMakerOkCancelFrame(self)
        self.okCancelFrame.frame.grid(row=2, column=0, columnspan=2, padx=4, pady=4, sticky=E)

        self.master.deiconify()
        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parent.lift()
        self.parent.wm_attributes("-topmost", 1)
        self.parent.grab_set()

    def setGlobalMessageSettings(self):
        gmSettings = self.listFrame.window.window.settings.get("message")
        wSettings = self.listFrame.window.window.settings.get("window")
        print(gmSettings)
        print(wSettings)
        self.fields.VAR_ENTRY_MESSAGE_DURATION.set(gmSettings.get("MESSAGE_DURATION"))
        self.fields.VAR_ENTRY_MESSAGE_INTERMISSION.set(gmSettings.get("MESSAGE_INTERMISSION"))
        self.fields.VAR_FONT_COMBO_BOX.set(gmSettings.get("MESSAGE_FONT_FACE"))
        self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = gmSettings.get("MESSAGE_COLOR")
        self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(gmSettings.get("MESSAGE_COLOR"))
        self.fields.VAR_ENTRY_NORMAL_FONT_SIZE.set(gmSettings.get("NORMAL_FONT_SIZE"))
        self.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(wSettings.get("MOVE_ALL_ON_LINE_DELAY"))
        self.fields.VAR_ARRIVAL.set(gmSettings.get("ARRIVAL"))
        self.fields.VAR_DEPARTURE.set(gmSettings.get("DEPARTURE"))

    def disableGlobalMessageFields(self):
        for child in self.globalMessageSettingsFrame.frame.winfo_children():
            if child.winfo_class() in ('Entry', 'Button', 'TCombobox'):
                child.configure(state='disable')
            if child.winfo_class() == 'Frame':
                for grandchild in child.winfo_children():
                    if grandchild.winfo_class() in ('Entry', 'Button', 'TCombobox'):
                        grandchild.configure(state='disable')

    # Todo: Enable fields if the message has the corresponding overrides already stored on it
    # Todo: Add the OK button functionality to return the message and update the parent window appropriately
    # Todo: Account for the differences between a new message and an edited one
