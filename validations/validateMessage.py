from tkinter import messagebox

def validate(messageMakerWindow) -> bool:
    if not messageMakerWindow.mmFrame.nickname.get() or messageMakerWindow.mmFrame.nickname.get().isspace():
        messagebox.showerror("Error", "A nickname is required for this message.", parent=messageMakerWindow.master)
        return False
    if len(messageMakerWindow.message.parts) < 1:
        messagebox.showerror("Error", "A message must contain at least one component.", parent=messageMakerWindow.master)
        return False
    return True