from tkinter import messagebox

import helperMethods

def validate(fields):
    if not fields.VAR_ENTRY_WINDOW_WIDTH.get().isnumeric() or int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) > 1920 or int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) < 400:
        messagebox.showinfo("Error", "Window width must be a whole number between 400 and 1920.")
        return False
    elif not fields.VAR_ENTRY_WINDOW_HEIGHT.get().isnumeric() or int(fields.VAR_ENTRY_WINDOW_HEIGHT.get()) > 1080 or int(fields.VAR_ENTRY_WINDOW_HEIGHT.get()) < 44:
        messagebox.showinfo("Error", "Window height must be a whole number between 44 and 1080.")
        return False
    elif int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) % 4 != 0:
        messagebox.showinfo("Error", "Window width must be divisible by 4.")
        return False
    elif int(fields.VAR_ENTRY_WINDOW_HEIGHT.get()) % 4 != 0:
        messagebox.showinfo("Error", "Window height must be divisible by 4.")
        return False
    elif not fields.VAR_ENTRY_BACKGROUND_X_POS.get().isnumeric() or int(fields.VAR_ENTRY_BACKGROUND_X_POS.get()) > int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) or int(
            fields.VAR_ENTRY_BACKGROUND_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Background X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not fields.VAR_ENTRY_BACKGROUND_Y_POS.get().isnumeric() or int(fields.VAR_ENTRY_BACKGROUND_Y_POS.get()) > int(fields.VAR_ENTRY_WINDOW_HEIGHT.get()) or int(
            fields.VAR_ENTRY_BACKGROUND_Y_POS.get()) < 0:
        messagebox.showinfo("Error", "Background Y coordinate must be a whole number between 0 and your chosen window height.")
        return False
    elif not fields.VAR_ENTRY_IMAGE_X_POS.get().isnumeric() or int(fields.VAR_ENTRY_IMAGE_X_POS.get()) > int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) or int(
            fields.VAR_ENTRY_IMAGE_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Image X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not fields.VAR_ENTRY_MESSAGE_X_POS.get().isnumeric() or int(fields.VAR_ENTRY_MESSAGE_X_POS.get()) > int(fields.VAR_ENTRY_WINDOW_WIDTH.get()) or int(
            fields.VAR_ENTRY_MESSAGE_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Message X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif int(fields.VAR_ENTRY_IMAGE_X_POS.get()) >= int(fields.VAR_ENTRY_MESSAGE_X_POS.get()):
        messagebox.showinfo("Error", "Image X coordinate must be less than Message X coordinate.")
        return False
    elif not helperMethods.isFloat(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) or float(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) > 0.5 or float(
            fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) <= 0:
        messagebox.showinfo("Error", "Scroll speed must be a decimal value greater than 0 and less than 0.5")
        return False
    return True