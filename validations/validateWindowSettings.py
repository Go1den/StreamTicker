from tkinter import messagebox

def validate(fields):
    if int(fields.VAR_ENTRY_IMAGE_X_POS.get()) >= int(fields.VAR_ENTRY_MESSAGE_X_POS.get()):
        messagebox.showinfo("Error", "Image X coordinate must be less than Message X coordinate.")
        return False
    return True
