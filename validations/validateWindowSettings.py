from tkinter import messagebox

from settingsGUIFields import SettingsGUIFields

def validate(fields: SettingsGUIFields) -> bool:
    if not fields.VAR_WINDOW_WIDTH.get().isnumeric() or int(fields.VAR_WINDOW_WIDTH.get()) < 200 or int(fields.VAR_WINDOW_WIDTH.get()) > 1920:
        messagebox.showinfo("Error", "Width must be a whole number between 200 and 1920 pixels.")
        return False
    if not fields.VAR_WINDOW_HEIGHT.get().isnumeric() or int(fields.VAR_WINDOW_HEIGHT.get()) < 20 or int(fields.VAR_WINDOW_HEIGHT.get()) > 1080:
        messagebox.showinfo("Error", "Height must be a whole number between 20 and 1080 pixels.")
        return False
    return True
