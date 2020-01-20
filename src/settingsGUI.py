import json
from tkinter import *
from tkinter import messagebox, colorchooser

from src.settings import Settings

def colorChooser(label, isForeground):
    color = colorchooser.askcolor(title="Select color")
    if isForeground:
        label.configure(text=color[1], foreground=color[1])
    else:
        label.configure(text=color[1], background=color[1])

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validateDepartureSettings():
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

def validateWindowSettings():
    if not ENTRY_WINDOW_WIDTH.get().isnumeric() or int(ENTRY_WINDOW_WIDTH.get()) > 1920 or int(ENTRY_WINDOW_WIDTH.get()) < 400:
        messagebox.showinfo("Error", "Window width must be a whole number between 400 and 1920.")
        return False
    elif not ENTRY_WINDOW_HEIGHT.get().isnumeric() or int(ENTRY_WINDOW_HEIGHT.get()) > 1080 or int(ENTRY_WINDOW_HEIGHT.get()) < 44:
        messagebox.showinfo("Error", "Window height must be a whole number between 44 and 1080.")
        return False
    elif not ENTRY_BACKGROUND_X_POS.get().isnumeric() or int(ENTRY_BACKGROUND_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()) or int(ENTRY_BACKGROUND_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Background X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not ENTRY_BACKGROUND_Y_POS.get().isnumeric() or int(ENTRY_BACKGROUND_Y_POS.get()) > int(ENTRY_WINDOW_HEIGHT.get()) or int(ENTRY_BACKGROUND_Y_POS.get()) < 0:
        messagebox.showinfo("Error", "Background Y coordinate must be a whole number between 0 and your chosen window height.")
        return False
    elif not ENTRY_IMAGE_X_POS.get().isnumeric() or int(ENTRY_IMAGE_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()):
        messagebox.showinfo("Error", "Image X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not ENTRY_MESSAGE_X_POS.get().isnumeric() or int(ENTRY_MESSAGE_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()):
        messagebox.showinfo("Error", "Message X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif ENTRY_IMAGE_X_POS.get() >= ENTRY_MESSAGE_X_POS.get():
        messagebox.showinfo("Error", "Image X coordinate must be less than Message X coordinate.")
        return False
    elif not isFloat(ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) or float(ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) > 0.5 or float(ENTRY_MOVE_ALL_ON_LINE_DELAY.get()) <= 0:
        messagebox.showinfo("Error", "Scroll speed must be a decimal value greater than 0 and less than 0.5")
        return False
    return True

def validateMessageSettings():
    if not ENTRY_MESSAGE_DURATION.get().isnumeric() or int(ENTRY_MESSAGE_DURATION.get()) <= 0:
        messagebox.showinfo("Error", "Message duration must be a whole number greater than 0.")
        return False
    if not isFloat(ENTRY_MESSAGE_INTERMISSION.get()) or float(ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showinfo("Error", "Message intermission must be a decimal value greater than 0.")
        return False
    return True

def updateSettingsJSON():
    if validateDepartureSettings() and validateWindowSettings() and validateMessageSettings():
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

Label(master, text="Window Settings").grid(row=0, column=2, sticky=W, padx=40)
Label(master, text="Window Width (pix):").grid(row=1, column=2, sticky=E)
ENTRY_WINDOW_WIDTH = Entry(master)
ENTRY_WINDOW_WIDTH.insert(0, settings.WINDOW_WIDTH)
ENTRY_WINDOW_WIDTH.grid(row=1, column=3, sticky=W)
Label(master, text="Window Height (pix):").grid(row=2, column=2, sticky=E)
ENTRY_WINDOW_HEIGHT = Entry(master)
ENTRY_WINDOW_HEIGHT.insert(0, settings.WINDOW_HEIGHT)
ENTRY_WINDOW_HEIGHT.grid(row=2, column=3, sticky=W)
Label(master, text="BG X Coord (pix):").grid(row=3, column=2, sticky=E)
ENTRY_BACKGROUND_X_POS = Entry(master)
ENTRY_BACKGROUND_X_POS.insert(0, settings.BACKGROUND_X_POS)
ENTRY_BACKGROUND_X_POS.grid(row=3, column=3, sticky=W)
Label(master, text="BG Y Coord (pix):").grid(row=4, column=2, sticky=E)
ENTRY_BACKGROUND_Y_POS = Entry(master)
ENTRY_BACKGROUND_Y_POS.insert(0, settings.BACKGROUND_Y_POS)
ENTRY_BACKGROUND_Y_POS.grid(row=4, column=3, sticky=W)
Label(master, text="Image X Coord (pix):").grid(row=5, column=2, sticky=E)
ENTRY_IMAGE_X_POS = Entry(master)
ENTRY_IMAGE_X_POS.insert(0, settings.IMAGE_X_POS)
ENTRY_IMAGE_X_POS.grid(row=5, column=3, sticky=W)
Label(master, text="Message X Coord (pix):").grid(row=6, column=2, sticky=E)
ENTRY_MESSAGE_X_POS = Entry(master)
ENTRY_MESSAGE_X_POS.insert(0, settings.MESSAGE_X_POS)
ENTRY_MESSAGE_X_POS.grid(row=6, column=3, sticky=W)

LABEL_WINDOW_BG_COLOR = Label(master)
Button(master, text='Window BG Color:', command=lambda: colorChooser(LABEL_WINDOW_BG_COLOR, False)).grid(row=7, column=2, sticky=E, padx=4)
LABEL_WINDOW_BG_COLOR.configure(text=settings.WINDOW_BG_COLOR, background=settings.WINDOW_BG_COLOR)
LABEL_WINDOW_BG_COLOR.grid(row=7, column=3, sticky=W)

Label(master, text="Window BG Image:").grid(row=8, column=2, sticky=E)
ENTRY_WINDOW_BG_IMAGE = Entry(master)
ENTRY_WINDOW_BG_IMAGE.insert(0, settings.WINDOW_BG_IMAGE)
ENTRY_WINDOW_BG_IMAGE.grid(row=8, column=3, sticky=W)
Label(master, text="Scroll Speed:").grid(row=9, column=2, sticky=E)
ENTRY_MOVE_ALL_ON_LINE_DELAY = Entry(master)
ENTRY_MOVE_ALL_ON_LINE_DELAY.insert(0, settings.MOVE_ALL_ON_LINE_DELAY)
ENTRY_MOVE_ALL_ON_LINE_DELAY.grid(row=9, column=3, sticky=W)

Label(master, text="Message Settings").grid(row=0, column=4, columnspan=3, sticky=W)
Label(master, text="Message Duration (secs)").grid(row=1, column=4, sticky=E)
ENTRY_MESSAGE_DURATION = Entry(master)
ENTRY_MESSAGE_DURATION.insert(0, settings.MESSAGE_DURATION)
ENTRY_MESSAGE_DURATION.grid(row=1, column=5, sticky=W)
Label(master, text="Message Font").grid(row=2, column=4, sticky=E)
ENTRY_MESSAGE_FONT_FACE = Entry(master)
ENTRY_MESSAGE_FONT_FACE.insert(0, settings.MESSAGE_FONT_FACE)
ENTRY_MESSAGE_FONT_FACE.grid(row=2, column=5, sticky=W)

LABEL_MESSAGE_COLOR = Label(master)
Button(master, text='Message Color:', command=lambda: colorChooser(LABEL_MESSAGE_COLOR, True)).grid(row=3, column=4, sticky=E, padx=4)
LABEL_MESSAGE_COLOR.configure(text=settings.MESSAGE_COLOR, foreground=settings.MESSAGE_COLOR)
LABEL_MESSAGE_COLOR.grid(row=3, column=5, sticky=W)

Label(master, text="Normal Font Settings").grid(row=4, column=4, sticky=W)
Label(master, text="Font Size (pix)").grid(row=5, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE = Entry(master)
ENTRY_NORMAL_FONT_SIZE.insert(0, settings.NORMAL_FONT_SIZE)
ENTRY_NORMAL_FONT_SIZE.grid(row=5, column=5, sticky=W)
Label(master, text="Font Gap Size (pix)").grid(row=6, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP = Entry(master)
ENTRY_NORMAL_FONT_SIZE_GAP.insert(0, settings.NORMAL_FONT_SIZE_GAP)
ENTRY_NORMAL_FONT_SIZE_GAP.grid(row=6, column=5, sticky=W)
Label(master, text="Font Gap Size For Spaces (pix)").grid(row=7, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Entry(master)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.insert(0, settings.NORMAL_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=5, sticky=W)
Label(master, text="Max Length for Normal Font Size").grid(row=8, column=4, sticky=E)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Entry(master)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.insert(0, settings.MAX_LENGTH_FOR_NORMAL_FONT_SIZE)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=8, column=5, sticky=W)

Label(master, text="Message Intermission (secs)").grid(row=1, column=6, sticky=E)
ENTRY_MESSAGE_INTERMISSION = Entry(master)
ENTRY_MESSAGE_INTERMISSION.insert(0, settings.MESSAGE_INTERMISSION)
ENTRY_MESSAGE_INTERMISSION.grid(row=1, column=7, sticky=W)
Label(master, text="Message Style").grid(row=2, column=6, sticky=E)
ENTRY_MESSAGE_STYLE = Entry(master)
ENTRY_MESSAGE_STYLE.insert(0, settings.MESSAGE_STYLE)
ENTRY_MESSAGE_STYLE.grid(row=2, column=7, sticky=W)
Label(master, text="Default Image").grid(row=3, column=6, sticky=E)
ENTRY_DEFAULT_IMAGE = Entry(master)
ENTRY_DEFAULT_IMAGE.insert(0, settings.DEFAULT_IMAGE)
ENTRY_DEFAULT_IMAGE.grid(row=3, column=7, sticky=W)

Label(master, text="Smaller Font Settings").grid(row=4, column=6, sticky=W)
Label(master, text="Font Size (pix)").grid(row=5, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE = Entry(master)
ENTRY_SMALLER_FONT_SIZE.insert(0, settings.SMALLER_FONT_SIZE)
ENTRY_SMALLER_FONT_SIZE.grid(row=5, column=7, sticky=W)
Label(master, text="Font Gap Size (pix)").grid(row=6, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP = Entry(master)
ENTRY_SMALLER_FONT_SIZE_GAP.insert(0, settings.SMALLER_FONT_SIZE_GAP)
ENTRY_SMALLER_FONT_SIZE_GAP.grid(row=6, column=7, sticky=W)
Label(master, text="Font Gap Size For Spaces (pix)").grid(row=7, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Entry(master)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.insert(0, settings.SMALLER_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=7, sticky=W)

Button(master, text='Save Settings', command=updateSettingsJSON).grid(row=9, column=7, pady=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=9, column=7, padx=4, pady=4, sticky=E)
master.mainloop()
mainloop()
