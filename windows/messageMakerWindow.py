from copy import deepcopy
from tkinter import Toplevel, E, NSEW

from frames.messageMakerFrame import MessageMakerFrame
from frames.messageMakerOkCancelFrame import MessageMakerOkCancelFrame
from frames.messageMakerPartFrame import MessageMakerPartFrame
from frames.overrideFrame import OverrideFrame
from frames.settingsMessageFrame import MessageFrame
from objects.message import Message
from objects.override import Override
from settings.globalMessageSettings import GlobalMessageSettings

class MessageMakerWindow:
    def __init__(self, listFrame, message: Message, index: int):
        self.master = Toplevel(listFrame.window.master)
        self.master.withdraw()
        self.listFrame = listFrame
        self.parent = listFrame.window.master
        self.parentWindow = listFrame.window
        self.message = deepcopy(message)
        self.message.sortParts()
        self.index = index
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

        self.partsFrame = MessageMakerPartFrame(self)
        self.partsFrame.frame.grid(row=1, column=0, sticky=NSEW, columnspan=2, padx=4, pady=4)

        self.globalMessageSettingsFrame = MessageFrame(self.master, self.fields)
        self.globalMessageSettingsFrame.frame.grid(row=2, column=1, sticky=NSEW, padx=(0, 4), pady=4)

        self.overrideFrame = OverrideFrame(self.master, self.globalMessageSettingsFrame, self.listFrame.window.window.settings)
        self.overrideFrame.frame.grid(row=2, column=0, sticky=NSEW, padx=4, pady=4)

        self.disableGlobalMessageFields()

        self.okCancelFrame = MessageMakerOkCancelFrame(self)
        self.okCancelFrame.frame.grid(row=3, column=0, columnspan=2, padx=4, pady=4, sticky=E)

        self.master.deiconify()
        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parent.lift()
        self.parent.wm_attributes("-topmost", 1)
        self.parent.grab_set()

    def setGlobalMessageSettings(self):
        gmSettings = self.listFrame.window.window.settings.messageSettings
        wSettings = self.listFrame.window.window.settings.windowSettings
        gmSettings.print()
        wSettings.print()
        self.fields.VAR_ENTRY_MESSAGE_DURATION.set(gmSettings.duration)
        self.fields.VAR_ENTRY_MESSAGE_INTERMISSION.set(gmSettings.intermission)
        self.fields.VAR_FONT_COMBO_BOX.set(gmSettings.fontFace)
        self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = gmSettings.color
        self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(gmSettings.color)
        self.fields.VAR_ENTRY_NORMAL_FONT_SIZE.set(gmSettings.fontSize)
        self.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(wSettings.moveAllOnLineDelay)
        self.fields.VAR_ARRIVAL.set(gmSettings.arrival)
        self.fields.VAR_DEPARTURE.set(gmSettings.departure)

    def disableGlobalMessageFields(self):
        for child in self.globalMessageSettingsFrame.frame.winfo_children():
            if child.winfo_class() in ('Entry', 'Button', 'TCombobox'):
                child.configure(state='disable')
            if child.winfo_class() == 'Frame':
                for grandchild in child.winfo_children():
                    if grandchild.winfo_class() in ('Entry', 'Button', 'TCombobox'):
                        grandchild.configure(state='disable')

    def updateMessage(self):
        override = Override()
        if self.overrideFrame.overrideDuration.get():
            override.duration = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MESSAGE_DURATION.get()
        if self.overrideFrame.overrideIntermission.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()
        if self.overrideFrame.overrideScrollSpeed.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()
        if self.overrideFrame.overrideFont.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_FONT_COMBO_BOX.get()
        if self.overrideFrame.overrideFontSize.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()
        if self.overrideFrame.overrideFontColor.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.get()
        if self.overrideFrame.overrideArrival.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_ARRIVAL.get()
        if self.overrideFrame.overrideDeparture.get():
            override.intermission = self.globalMessageSettingsFrame.fields.VAR_DEPARTURE.get()

        for part in self.message.parts:
            part.sortOrder = self.message.parts.index(part) + 1

        newMessage = Message(self.mmFrame.nickname.get(), self.index, self.message.parts, override)
        if self.message:
            self.parentWindow.messages[self.index] = newMessage
        else:
            self.parentWindow.messages.append(newMessage)
        self.parentWindow.mlFrame.populateListbox(self.parentWindow.messages)
        self.master.destroy()

# Todo: Enable fields if the message has the corresponding overrides already stored on it
