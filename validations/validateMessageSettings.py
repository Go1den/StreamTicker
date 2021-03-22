from tkinter import messagebox

from settings.globalMessageSettings import GlobalMessageSettings
from objects.settingsGUIFields import SettingsGUIFields
from utils import helperMethods

def validate(fields: SettingsGUIFields, window) -> bool:
    if not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_DURATION.get()) or float(fields.VAR_ENTRY_MESSAGE_DURATION.get()) <= 0:
        messagebox.showerror("Error", "Value for Show Each Message For must be greater than 0.", parent=window)
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) or float(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showerror("Error", "Time Between Messages must be greater than 0.", parent=window)
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) or float(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) < 1 or float(
            fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) > 100:
        messagebox.showerror("Error", "Message Scroll Speed must be a number between 1 and 100.", parent=window)
        return False
    return True

def validateMessageMessageMaker(fields: GlobalMessageSettings, window) -> bool:
    if not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_DURATION.get()) or float(fields.VAR_ENTRY_MESSAGE_DURATION.get()) <= 0:
        messagebox.showerror("Error", "Value for Show Each Message For must be greater than 0.", parent=window)
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) or float(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showerror("Error", "Time Between Messages must be greater than 0.", parent=window)
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) or float(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) < 1 or float(
            fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) > 100:
        messagebox.showerror("Error", "Message Scroll Speed must be a number between 1 and 100.", parent=window)
        return False
    return True
