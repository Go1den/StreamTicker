from tkinter import messagebox

from settingsGUIFields import SettingsGUIFields

def validate(fields: SettingsGUIFields, window) -> bool:
    if not fields.VAR_WINDOW_WIDTH.get().isnumeric() or int(fields.VAR_WINDOW_WIDTH.get()) < 200 or int(fields.VAR_WINDOW_WIDTH.get()) > 1920:
        messagebox.showerror("Error", "Width must be a whole number between 200 and 1920 pixels.", parent=window)
        return False
    if not fields.VAR_WINDOW_HEIGHT.get().isnumeric() or int(fields.VAR_WINDOW_HEIGHT.get()) < 20 or int(fields.VAR_WINDOW_HEIGHT.get()) > 1080:
        messagebox.showerror("Error", "Height must be a whole number between 20 and 1080 pixels.", parent=window)
        return False
    return True
