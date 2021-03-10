from tkinter import messagebox

from settingsGUIFields import SettingsGUIFields
from utils import helperMethods

def validate(fields: SettingsGUIFields) -> bool:
    if not fields.VAR_ENTRY_MESSAGE_DURATION.get().isnumeric() or int(fields.VAR_ENTRY_MESSAGE_DURATION.get()) <= 0:
        messagebox.showinfo("Error", "Message duration must be a whole number greater than 0.")
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) or float(fields.VAR_ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showinfo("Error", "Message intermission must be greater than 0.")
        return False
    return True
