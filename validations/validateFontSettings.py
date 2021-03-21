from tkinter import messagebox

from settingsGUIFields import SettingsGUIFields

def validate(fields: SettingsGUIFields) -> bool:
    if not fields.VAR_ENTRY_NORMAL_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) < 8 or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) > 256:
        messagebox.showerror("Error", "Font size must be a whole number between 8 and 256.")
        return False
    # add validation on message style whenever that gets added to the settings menu
    return True
