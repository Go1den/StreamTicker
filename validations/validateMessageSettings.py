from tkinter import messagebox

from settingsGUIFields import SettingsGUIFields
from utils import helperMethods

def validate(fields: SettingsGUIFields) -> bool:
    if not fields.VAR_ENTRY_MESSAGE_DURATION.get().isnumeric() or int(fields.VAR_ENTRY_MESSAGE_DURATION.get()) <= 0:
        messagebox.showerror("Error", "Message duration must be a whole number greater than 0.")
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) or float(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showerror("Error", "Message intermission must be greater than 0.")
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) or float(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) < 1 or float(
            fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) > 100:
        messagebox.showerror("Error", "Message scroll speed must be a number between 1 and 100.")
        return False
    return True
