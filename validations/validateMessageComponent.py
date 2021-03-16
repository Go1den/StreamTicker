from tkinter import messagebox

from frames.messageComponentFrame import MessageComponentFrame

def validate(componentFrame: MessageComponentFrame) -> bool:
    if componentFrame.componentType.get() == "Text":
        if not componentFrame.textValue.get():
            messagebox.showerror("Error", "Text component cannot be added without text.")
            return False
    if componentFrame.componentType.get() == "Image":
        if not componentFrame.imagePath.get():
            messagebox.showerror("Error", "Image component requires a file to be selected.")
            return False
    if componentFrame.componentType.get() == "Text From File":
        if not componentFrame.filePath.get():
            messagebox.showerror("Error", "Text From File component requires a file to be selected.")
            return False
    if componentFrame.componentType.get() == "Pixel Gap":
        if not componentFrame.gapValue.get() or not componentFrame.gapValue.get().isnumeric():
            messagebox.showerror("Error", "Pixel Gap requires a number of pixels.")
            return False
    return True