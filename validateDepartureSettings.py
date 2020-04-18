from tkinter import messagebox

def validate(fields):
    if (not fields.VAR_CHECK_SLIDING_RIGHT.get()
            and not fields.VAR_CHECK_SLIDING_LEFT.get()
            and not fields.VAR_CHECK_SLIDING_UP.get()
            and not fields.VAR_CHECK_SLIDING_DOWN.get()
            and not fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.get()
            and not fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.get()
            and not fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.get()):
        messagebox.showinfo("Error", "At least one of the checkboxes in Departure Settings must be selected.")
        return False
    return True
