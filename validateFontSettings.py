from tkinter import messagebox

def validate(fields):
    if not fields.VAR_ENTRY_NORMAL_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) < 8 or int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) > 256:
        messagebox.showinfo("Error", "Normal message font size must be a whole number between 8 and 256.")
        return False
    elif not fields.VAR_ENTRY_SMALLER_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_SMALLER_FONT_SIZE.get()) < 8 or int(fields.VAR_ENTRY_SMALLER_FONT_SIZE.get()) > 256:
        messagebox.showinfo("Error", "Long message font size must be a whole number between 8 and 256.")
        return False
    elif int(fields.VAR_ENTRY_NORMAL_FONT_SIZE.get()) < int(fields.VAR_ENTRY_SMALLER_FONT_SIZE.get()):
        messagebox.showinfo("Error", "Normal message font size cannot be less than long message font size.")
        return False
    elif not fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP.get().isnumeric():
        messagebox.showinfo("Error", "Normal message font gap size must be a whole number.")
        return False
    elif not fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP.get().isnumeric():
        messagebox.showinfo("Error", "Long message font gap size must be a whole number.")
        return False
    elif not fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.get().isnumeric():
        messagebox.showinfo("Error", "Normal message penalty for spaces must be a whole number.")
        return False
    elif not fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.get().isnumeric():
        messagebox.showinfo("Error", "Long message penalty for spaces must be a whole number.")
        return False
    elif not fields.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get().isnumeric() or int(fields.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get()) < 1:
        messagebox.showinfo("Error", "Max length for normal messages must be a positive whole number.")
        return False
    # add validation on message style whenever that gets added to the settings menu
    return True