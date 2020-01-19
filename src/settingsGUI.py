import json
from tkinter import *
from tkinter import messagebox

from src.settings import Settings

def validateDepartures():
    if (not CHECK_SLIDING_RIGHT.get()
            and not CHECK_SLIDING_LEFT.get()
            and not CHECK_SLIDING_UP.get()
            and not CHECK_SLIDING_DOWN.get()
            and not CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.get()
            and not CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.get()
            and not CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.get()):
        messagebox.showinfo("Error", "At least one of the checkboxes in Departure Settings must be selected.")
        return False
    return True

def updateSettingsJSON():
    if validateDepartures():
        d = settings.data['departure'][0]
        d['ENABLE_DEPARTING_BY_SLIDING_RIGHT'] = CHECK_SLIDING_RIGHT.get()
        d['ENABLE_DEPARTING_BY_SLIDING_LEFT'] = CHECK_SLIDING_LEFT.get()
        d['ENABLE_DEPARTING_BY_SLIDING_UP'] = CHECK_SLIDING_UP.get()
        d['ENABLE_DEPARTING_BY_SLIDING_DOWN'] = CHECK_SLIDING_DOWN.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT'] = CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT'] = CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER'] = CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.get()
        # d['ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES'] = CHECK_COVERING_WITH_RECTANGLES.get()
        with open("settings.json", 'w') as f:
            json.dump(settings.data, f, indent=4)
        messagebox.showinfo("Success", "Settings updated!")

settings = Settings()

master = Tk()
master.wm_title("StreamTicker Settings")
Label(master, text="Departure Settings").grid(row=0, column=0, columnspan=3, sticky=W)
Label(master, text="Allow messages to leave the screen by:").grid(row=1, column=0, columnspan=3, sticky=W)

CHECK_SLIDING_RIGHT = BooleanVar()
CHECK_SLIDING_RIGHT.set(settings.ENABLE_DEPARTING_BY_SLIDING_RIGHT)
CBOX_SLIDING_RIGHT = Checkbutton(master, var=CHECK_SLIDING_RIGHT)
CBOX_SLIDING_RIGHT.grid(row=2, column=0, sticky=E)
Label(master, text="Sliding right").grid(row=2, column=1, sticky=W)

CHECK_SLIDING_LEFT = BooleanVar()
CHECK_SLIDING_LEFT.set(settings.ENABLE_DEPARTING_BY_SLIDING_LEFT)
CBOX_SLIDING_LEFT = Checkbutton(master, var=CHECK_SLIDING_LEFT)
CBOX_SLIDING_LEFT.grid(row=3, column=0, sticky=E)
Label(master, text="Sliding left").grid(row=3, column=1, sticky=W)

CHECK_SLIDING_UP = BooleanVar()
CHECK_SLIDING_UP.set(settings.ENABLE_DEPARTING_BY_SLIDING_UP)
CBOX_SLIDING_UP = Checkbutton(master, var=CHECK_SLIDING_UP)
CBOX_SLIDING_UP.grid(row=4, column=0, sticky=E)
Label(master, text="Sliding up").grid(row=4, column=1, sticky=W)

CHECK_SLIDING_DOWN = BooleanVar()
CHECK_SLIDING_DOWN.set(settings.ENABLE_DEPARTING_BY_SLIDING_DOWN)
CBOX_SLIDING_DOWN = Checkbutton(master, var=CHECK_SLIDING_DOWN)
CBOX_SLIDING_DOWN.grid(row=5, column=0, sticky=E)
Label(master, text="Sliding down").grid(row=5, column=1, sticky=W)

CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = BooleanVar()
CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.set(settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = Checkbutton(master, var=CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.grid(row=6, column=0, sticky=E)
Label(master, text="Alternating up/down working backwards").grid(row=6, column=1, sticky=W)

CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = BooleanVar()
CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.set(settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = Checkbutton(master, var=CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.grid(row=7, column=0, sticky=E)
Label(master, text="Alternating up/down working forwards").grid(row=7, column=1, sticky=W)

CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = BooleanVar()
CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.set(settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = Checkbutton(master, var=CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.grid(row=8, column=0, sticky=E)
Label(master, text="Alternating up/down, random order").grid(row=8, column=1, sticky=W)

# CHECK_COVERING_WITH_RECTANGLES = BooleanVar()
# CHECK_COVERING_WITH_RECTANGLES.set(settings.ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES)
# CBOX_COVERING_WITH_RECTANGLES = Checkbutton(master, var=CHECK_COVERING_WITH_RECTANGLES)
# CBOX_COVERING_WITH_RECTANGLES.grid(row=8, column=0)
# Label(master, text="Covering with rectangles").grid(row=8, column=1)

Button(master, text='Save Settings', command=updateSettingsJSON).grid(row=99, column=0, columnspan=2, pady=4, padx=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=99, column=1, pady=4, padx=4, sticky=E)
master.mainloop()
mainloop()
