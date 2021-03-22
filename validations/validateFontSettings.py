from tkinter import messagebox

from settings.globalMessageSettings import GlobalMessageSettings
from settingsGUIFields import SettingsGUIFields

def validate(fields: SettingsGUIFields, window) -> bool:
    if not fields.VAR_ENTRY_NORMAL_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) < 8 or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) > 256:
        messagebox.showerror("Error", "Font size must be a whole number between 8 and 256.", parent=window)
        return False
    return True

def validateFontsMessageMaker(fields: GlobalMessageSettings, window) -> bool:
    if not fields.VAR_ENTRY_NORMAL_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) < 8 or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) > 256:
        messagebox.showerror("Error", "Font size must be a whole number between 8 and 256.", parent=window)
        return False
    return True
