from copy import deepcopy
from tkinter import Toplevel, E, NSEW, NORMAL

from frames.messageMakerFrame import MessageMakerFrame
from frames.messageMakerOkCancelFrame import MessageMakerOkCancelFrame
from frames.messageMakerPartFrame import MessageMakerPartFrame
from frames.overrideFrame import OverrideFrame
from frames.settingsMessageFrame import SettingsMessageFrame
from objects.message import Message
from objects.override import Override
from settings.globalMessageSettings import GlobalMessageSettings
from validations.validateFontSettings import validateFontsMessageMaker
from validations.validateMessage import validate
from validations.validateMessageSettings import validateMessageMessageMaker

class MessageMakerWindow:
    def __init__(self, listFrame, message: Message, index: int):
        self.master = Toplevel(listFrame.window.master)
        self.master.withdraw()
        self.listFrame = listFrame
        self.parent = listFrame.window.master
        self.parentWindow = listFrame.window
        self.message = deepcopy(message)
        if not self.message:
            self.isNewMessage = True
            self.message = Message()
        else:
            self.isNewMessage = False
        self.message.sortParts()
        self.index = index
        self.master.geometry('+{x}+{y}'.format(x=self.parent.winfo_x() + 10, y=self.parent.winfo_y() + 10))
        self.master.wm_attributes("-topmost", 1)
        self.master.focus_force()
        self.master.wm_title("StreamTicker Message Maker")
        self.master.iconbitmap("imagefiles/stIcon.ico")
        self.master.resizable(False, False)
        self.master.grab_set()
        self.master.protocol("WM_DELETE_WINDOW", self.deleteWindow)

        self.fields = GlobalMessageSettings()
        self.setGlobalMessageSettings()

        self.mmFrame = MessageMakerFrame(self.master, self.message)
        self.mmFrame.frame.grid(row=0, column=0, sticky=NSEW, columnspan=2, padx=4, pady=4)

        self.partsFrame = MessageMakerPartFrame(self)
        self.partsFrame.frame.grid(row=1, column=0, sticky=NSEW, columnspan=2, padx=4, pady=4)

        self.globalMessageSettingsFrame = SettingsMessageFrame(self.master, self.fields)
        self.globalMessageSettingsFrame.frame.grid(row=2, column=1, sticky=NSEW, padx=(0, 4), pady=4)

        self.overrideFrame = OverrideFrame(self.master, self.globalMessageSettingsFrame, self.listFrame.window.window.settings)
        self.overrideFrame.frame.grid(row=2, column=0, sticky=NSEW, padx=4, pady=4)

        self.disableGlobalMessageFields()

        self.okCancelFrame = MessageMakerOkCancelFrame(self)
        self.okCancelFrame.frame.grid(row=3, column=0, columnspan=2, padx=4, pady=4, sticky=E)

        self.applyOverrides()
        self.master.deiconify()
        self.master.mainloop()

    def deleteWindow(self):
        self.master.destroy()
        self.parent.lift()
        self.parent.wm_attributes("-topmost", 1)
        self.parent.grab_set()

    def applyOverrides(self):
        overrides = self.message.overrides
        print("overrides:")
        overrides.print()
        if overrides:
            if overrides.duration:
                self.fields.VAR_ENTRY_MESSAGE_DURATION.set(overrides.duration)
                self.overrideFrame.overrideDuration.set(True)
                self.overrideFrame.gmsFrame.ENTRY_MESSAGE_DURATION.configure(state=NORMAL)
            if overrides.intermission:
                self.fields.VAR_ENTRY_MESSAGE_INTERMISSION.set(overrides.intermission)
                self.overrideFrame.overrideIntermission.set(True)
                self.overrideFrame.gmsFrame.ENTRY_MESSAGE_INTERMISSION.configure(state=NORMAL)
            if overrides.scrollSpeed:
                self.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.set(overrides.scrollSpeed)
                self.overrideFrame.overrideScrollSpeed.set(True)
                self.overrideFrame.gmsFrame.entryMoveAllOnLineDelay.configure(state=NORMAL)
            if overrides.font:
                self.fields.VAR_FONT_COMBO_BOX.set(overrides.font)
                self.overrideFrame.overrideFont.set(True)
                self.overrideFrame.gmsFrame.FONT_COMBO_BOX.configure(state="readonly")
            if overrides.fontColor:
                self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = overrides.fontColor
                self.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(overrides.fontColor)
                self.overrideFrame.overrideFontColor.set(True)
                self.overrideFrame.gmsFrame.BUTTON_MESSAGE_COLOR.config(state=NORMAL)
                self.globalMessageSettingsFrame.CANVAS_MESSAGE_COLOR.itemconfig(self.globalMessageSettingsFrame.RECTANGLE_MESSAGE_COLOR,
                                                                                fill=self.fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
            if overrides.fontSize:
                self.fields.VAR_ENTRY_NORMAL_FONT_SIZE.set(overrides.fontSize)
                self.overrideFrame.overrideFontSize.set(True)
                self.overrideFrame.gmsFrame.ENTRY_NORMAL_FONT_SIZE.configure(state=NORMAL)
            if overrides.arrival:
                self.fields.VAR_ARRIVAL.set(overrides.arrival)
                self.overrideFrame.overrideArrival.set(True)
                self.overrideFrame.gmsFrame.ARRIVAL_COMBO_BOX.config(state="readonly")
            if overrides.departure:
                self.fields.VAR_DEPARTURE.set(overrides.departure)
                self.overrideFrame.overrideDeparture.set(True)
                self.overrideFrame.gmsFrame.DEPARTURE_COMBO_BOX.config(state="readonly")
            if overrides.bold:
                self.fields.VAR_FONT_IS_BOLD.set(overrides.bold)
                self.overrideFrame.overrideFontStyle.set(True)
                self.configureFontStyleFields()
            if overrides.italic:
                self.fields.VAR_FONT_IS_ITALIC.set(overrides.italic)
                self.overrideFrame.overrideFontStyle.set(True)
                self.configureFontStyleFields()
            if overrides.overstrike:
                self.fields.VAR_FONT_IS_OVERSTRIKE.set(overrides.overstrike)
                self.overrideFrame.overrideFontStyle.set(True)
                self.configureFontStyleFields()

    def configureFontStyleFields(self):
        self.overrideFrame.gmsFrame.checkButtonBold.config(state=NORMAL)
        self.overrideFrame.gmsFrame.checkButtonItalic.config(state=NORMAL)
        self.overrideFrame.gmsFrame.checkButtonOverstrike.config(state=NORMAL)

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
        self.fields.VAR_FONT_IS_BOLD.set(gmSettings.bold)
        self.fields.VAR_FONT_IS_ITALIC.set(gmSettings.italic)
        self.fields.VAR_FONT_IS_OVERSTRIKE.set(gmSettings.overstrike)

    def disableGlobalMessageFields(self):
        for child in self.globalMessageSettingsFrame.frame.winfo_children():
            if child.winfo_class() in ('Entry', 'Button', 'TCombobox', 'Checkbutton'):
                child.configure(state='disable')
            if child.winfo_class() == 'Frame':
                for grandchild in child.winfo_children():
                    if grandchild.winfo_class() in ('Entry', 'Button', 'TCombobox', 'Checkbutton'):
                        grandchild.configure(state='disable')

    def updateMessage(self):
        if validateMessageMessageMaker(self.fields, self.master) and validateFontsMessageMaker(self.fields, self.master) and validate(self):
            override = Override()
            if self.overrideFrame.overrideDuration.get():
                override.duration = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MESSAGE_DURATION.get()
            if self.overrideFrame.overrideIntermission.get():
                override.intermission = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()
            if self.overrideFrame.overrideScrollSpeed.get():
                override.scrollSpeed = self.globalMessageSettingsFrame.fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()
            if self.overrideFrame.overrideFont.get():
                override.font = self.globalMessageSettingsFrame.fields.VAR_FONT_COMBO_BOX.get()
            if self.overrideFrame.overrideFontSize.get():
                override.fontSize = self.globalMessageSettingsFrame.fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()
            if self.overrideFrame.overrideFontColor.get():
                override.fontColor = self.globalMessageSettingsFrame.fields.VAR_LABEL_MESSAGE_COLOR_TEXT.get()
            if self.overrideFrame.overrideArrival.get():
                override.arrival = self.globalMessageSettingsFrame.fields.VAR_ARRIVAL.get()
            if self.overrideFrame.overrideDeparture.get():
                override.departure = self.globalMessageSettingsFrame.fields.VAR_DEPARTURE.get()
            if self.overrideFrame.overrideFontStyle.get():
                override.bold = self.globalMessageSettingsFrame.fields.VAR_FONT_IS_BOLD.get()
                override.italic = self.globalMessageSettingsFrame.fields.VAR_FONT_IS_ITALIC.get()
                override.overstrike = self.globalMessageSettingsFrame.fields.VAR_FONT_IS_OVERSTRIKE.get()

            for part in self.message.parts:
                part.sortOrder = self.message.parts.index(part) + 1

            newMessage = Message(self.mmFrame.nickname.get(), self.index, self.message.parts, override)
            if not self.isNewMessage:
                self.parentWindow.messages[self.index] = newMessage
            else:
                self.parentWindow.messages.append(newMessage)
            self.parentWindow.mlFrame.populateListbox(self.parentWindow.messages)
            self.master.destroy()
