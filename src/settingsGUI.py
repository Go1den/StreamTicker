import json
from tkinter import *
from tkinter import messagebox, colorchooser, filedialog, font, ttk

from src.CreateToolTip import CreateToolTip
from src.settings import Settings

def getDefaultSettings():
    global WINDOW_BG_IMAGE, CHECK_SLIDING_RIGHT, CHECK_SLIDING_DOWN, CHECK_SLIDING_LEFT, CHECK_SLIDING_UP, CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER, \
        CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT, CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT
    d = settings.data['departure'][0]
    d['ENABLE_DEPARTING_BY_SLIDING_RIGHT'] = True
    CHECK_SLIDING_RIGHT = True
    d['ENABLE_DEPARTING_BY_SLIDING_LEFT'] = True
    CHECK_SLIDING_LEFT = True
    d['ENABLE_DEPARTING_BY_SLIDING_UP'] = True
    CHECK_SLIDING_UP = True
    d['ENABLE_DEPARTING_BY_SLIDING_DOWN'] = True
    CHECK_SLIDING_DOWN = True
    d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT'] = True
    CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = True
    d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT'] = True
    CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = True
    d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER'] = True
    CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = True
    # d['ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES'] = CHECK_COVERING_WITH_RECTANGLES.get()
    m = settings.data['message'][0]
    m['MESSAGE_DURATION'] = "5"
    ENTRY_MESSAGE_DURATION.configure(text="5")
    m['MESSAGE_INTERMISSION'] = "0.5"
    ENTRY_MESSAGE_INTERMISSION.configure(text="0.5")
    m['MESSAGE_COLOR'] = "#ffffff"
    LABEL_MESSAGE_COLOR.configure(text="#ffffff", foreground="#ffffff")
    # m['MESSAGE_STYLE'] = ENTRY_MESSAGE_STYLE.get()
    m['MESSAGE_FONT_FACE'] = "Courier New"
    FONT_COMBO_BOX.set("Courier New")
    m['MAX_LENGTH_FOR_NORMAL_FONT_SIZE'] = "16"
    ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.configure(text="16")
    m['NORMAL_FONT_SIZE'] = "26"
    ENTRY_NORMAL_FONT_SIZE.configure(text="26")
    m['NORMAL_FONT_SIZE_GAP'] = "20"
    ENTRY_NORMAL_FONT_SIZE_GAP.configure(text="20")
    m['NORMAL_FONT_SIZE_GAP_FOR_SPACES'] = "4"
    ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.configure(text="4")
    m['SMALLER_FONT_SIZE'] = "22"
    ENTRY_SMALLER_FONT_SIZE.configure(text="22")
    m['SMALLER_FONT_SIZE_GAP'] = "16"
    ENTRY_SMALLER_FONT_SIZE_GAP.configure(text="16")
    m['SMALLER_FONT_SIZE_GAP_FOR_SPACES'] = "6"
    ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.configure(text="6")
    w = settings.data['window'][0]
    w['MESSAGE_X_POS'] = "60"
    ENTRY_MESSAGE_X_POS.configure(text="60")
    w['IMAGE_X_POS'] = "22"
    ENTRY_IMAGE_X_POS.configure(text="22")
    w['WINDOW_WIDTH'] = "400"
    ENTRY_WINDOW_WIDTH.configure(text="400")
    w['WINDOW_HEIGHT'] = "44"
    ENTRY_WINDOW_HEIGHT.configure(text="44")
    w['WINDOW_BG_COLOR'] = "#000000"
    LABEL_WINDOW_BG_COLOR.configure(background="#000000", text="#000000")
    w['WINDOW_BG_IMAGE'] = "imagefiles/background.png"
    WINDOW_BG_IMAGE = "imagefiles/background.png"
    w['BACKGROUND_X_POS'] = "202"
    ENTRY_BACKGROUND_X_POS.configure(text="202")
    w['BACKGROUND_Y_POS'] = "24"
    ENTRY_BACKGROUND_Y_POS.configure(text="44")
    w['MOVE_ALL_ON_LINE_DELAY'] = ".004"
    ENTRY_MOVE_ALL_ON_LINE_DELAY.configure(text=".004")
    with open("settings.json", 'w') as f:
        json.dump(settings.data, f, indent=4)
    messagebox.showinfo("Success", "Default settings restored!")
    return

def selectImageFile(label):
    global WINDOW_BG_IMAGE
    filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
    print(filename)
    label.configure(text=getFileNameFromPath(filename))
    WINDOW_BG_IMAGE = filename

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

def getFileNameFromPath(path):
    try:
        x = path.split('/')[-1]
        y = path.split('\\')[-1]
        return x if len(x) <= len(y) else y
    except:
        return path

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
    elif int(ENTRY_WINDOW_HEIGHT.get()) % 4 != 0:
        messagebox.showinfo("Error", "Window height must be divisible by 4. This is because of how the math is performed for rolling letters onto the screen. Sorry!")
        return False
    elif not ENTRY_BACKGROUND_X_POS.get().isnumeric() or int(ENTRY_BACKGROUND_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()) or int(ENTRY_BACKGROUND_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Background X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not ENTRY_BACKGROUND_Y_POS.get().isnumeric() or int(ENTRY_BACKGROUND_Y_POS.get()) > int(ENTRY_WINDOW_HEIGHT.get()) or int(ENTRY_BACKGROUND_Y_POS.get()) < 0:
        messagebox.showinfo("Error", "Background Y coordinate must be a whole number between 0 and your chosen window height.")
        return False
    elif not ENTRY_IMAGE_X_POS.get().isnumeric() or int(ENTRY_IMAGE_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()) or int(ENTRY_IMAGE_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Image X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif not ENTRY_MESSAGE_X_POS.get().isnumeric() or int(ENTRY_MESSAGE_X_POS.get()) > int(ENTRY_WINDOW_WIDTH.get()) or int(ENTRY_MESSAGE_X_POS.get()) < 0:
        messagebox.showinfo("Error", "Message X coordinate must be a whole number between 0 and your chosen window width.")
        return False
    elif int(ENTRY_IMAGE_X_POS.get()) >= int(ENTRY_MESSAGE_X_POS.get()):
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
    elif not isFloat(ENTRY_MESSAGE_INTERMISSION.get()) or float(ENTRY_MESSAGE_INTERMISSION.get()) <= 0:
        messagebox.showinfo("Error", "Message intermission must be a decimal value greater than 0.")
        return False
    return True

def validateFontSettings():
    if not ENTRY_NORMAL_FONT_SIZE.get().isnumeric() or int(ENTRY_NORMAL_FONT_SIZE.get()) < 8:
        messagebox.showinfo("Error", "Normal message font size must be a whole number greater than or equal to 8.")
        return False
    elif not ENTRY_SMALLER_FONT_SIZE.get().isnumeric() or int(ENTRY_SMALLER_FONT_SIZE.get()) < 8:
        messagebox.showinfo("Error", "Long message font size must be a whole number greater than or equal to 8.")
        return False
    elif int(ENTRY_NORMAL_FONT_SIZE.get()) < int(ENTRY_SMALLER_FONT_SIZE.get()):
        messagebox.showinfo("Error", "Normal message font size cannot be less than long message font size.")
        return False
    elif not ENTRY_NORMAL_FONT_SIZE_GAP.get().isnumeric():
        messagebox.showinfo("Error", "Normal message font gap size must be a whole number.")
        return False
    elif not ENTRY_SMALLER_FONT_SIZE_GAP.get().isnumeric():
        messagebox.showinfo("Error", "Long message font gap size must be a whole number.")
        return False
    elif not ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.get().isnumeric():
        messagebox.showinfo("Error", "Normal message penalty for spaces must be a whole number.")
        return False
    elif not ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.get().isnumeric():
        messagebox.showinfo("Error", "Long message penalty for spaces must be a whole number.")
        return False
    elif not ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get().isnumeric() or int(ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get()) < 1:
        messagebox.showinfo("Error", "Max length for normal messages must be a positive whole number.")
        return False
    return True

def updateSettingsJSON():
    if validateDepartureSettings() and validateWindowSettings() and validateMessageSettings() and validateFontSettings():
        d = settings.data['departure'][0]
        d['ENABLE_DEPARTING_BY_SLIDING_RIGHT'] = CHECK_SLIDING_RIGHT.get()
        d['ENABLE_DEPARTING_BY_SLIDING_LEFT'] = CHECK_SLIDING_LEFT.get()
        d['ENABLE_DEPARTING_BY_SLIDING_UP'] = CHECK_SLIDING_UP.get()
        d['ENABLE_DEPARTING_BY_SLIDING_DOWN'] = CHECK_SLIDING_DOWN.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT'] = CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT'] = CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.get()
        d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER'] = CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.get()
        # d['ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES'] = CHECK_COVERING_WITH_RECTANGLES.get()
        m = settings.data['message'][0]
        m['MESSAGE_DURATION'] = ENTRY_MESSAGE_DURATION.get()
        m['MESSAGE_INTERMISSION'] = ENTRY_MESSAGE_INTERMISSION.get()
        m['MESSAGE_COLOR'] = LABEL_MESSAGE_COLOR.cget("text")
        # m['MESSAGE_STYLE'] = ENTRY_MESSAGE_STYLE.get()
        m['MESSAGE_FONT_FACE'] = FONT_COMBO_BOX.get()
        m['MAX_LENGTH_FOR_NORMAL_FONT_SIZE'] = ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get()
        m['NORMAL_FONT_SIZE'] = ENTRY_NORMAL_FONT_SIZE.get()
        m['NORMAL_FONT_SIZE_GAP'] = ENTRY_NORMAL_FONT_SIZE_GAP.get()
        m['NORMAL_FONT_SIZE_GAP_FOR_SPACES'] = ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.get()
        m['SMALLER_FONT_SIZE'] = ENTRY_SMALLER_FONT_SIZE.get()
        m['SMALLER_FONT_SIZE_GAP'] = ENTRY_SMALLER_FONT_SIZE_GAP.get()
        m['SMALLER_FONT_SIZE_GAP_FOR_SPACES'] = ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.get()
        w = settings.data['window'][0]
        w['MESSAGE_X_POS'] = ENTRY_MESSAGE_X_POS.get()
        w['IMAGE_X_POS'] = ENTRY_IMAGE_X_POS.get()
        w['WINDOW_WIDTH'] = ENTRY_WINDOW_WIDTH.get()
        w['WINDOW_HEIGHT'] = ENTRY_WINDOW_HEIGHT.get()
        w['WINDOW_BG_COLOR'] = LABEL_WINDOW_BG_COLOR.cget("text")
        w['WINDOW_BG_IMAGE'] = WINDOW_BG_IMAGE
        w['BACKGROUND_X_POS'] = ENTRY_BACKGROUND_X_POS.get()
        w['BACKGROUND_Y_POS'] = ENTRY_BACKGROUND_Y_POS.get()
        w['MOVE_ALL_ON_LINE_DELAY'] = ENTRY_MOVE_ALL_ON_LINE_DELAY.get()
        with open("settings.json", 'w') as f:
            json.dump(settings.data, f, indent=4)
        messagebox.showinfo("Success", "Settings updated!")

settings = Settings()
WINDOW_BG_IMAGE = settings.WINDOW_BG_IMAGE

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
LABEL_WINDOW_WIDTH = Label(master, text="Window Width:")
TOOLTOP_WINDOW_WIDTH = CreateToolTip(LABEL_WINDOW_WIDTH, "Width of the window in pixels.\nValid values are between 400 and 1920.")
LABEL_WINDOW_WIDTH.grid(row=1, column=2, sticky=E)
ENTRY_WINDOW_WIDTH = Entry(master)
ENTRY_WINDOW_WIDTH.insert(0, settings.WINDOW_WIDTH)
ENTRY_WINDOW_WIDTH.grid(row=1, column=3, sticky=W)
LABEL_WINDOW_HEIGHT = Label(master, text="Window Height:")
TOOLTOP_WINDOW_HEIGHT = CreateToolTip(LABEL_WINDOW_HEIGHT, "Height of the window in pixels.\nValid values are multiples of 4 between 44 and 1080.")
LABEL_WINDOW_HEIGHT.grid(row=2, column=2, sticky=E)
ENTRY_WINDOW_HEIGHT = Entry(master)
ENTRY_WINDOW_HEIGHT.insert(0, settings.WINDOW_HEIGHT)
ENTRY_WINDOW_HEIGHT.grid(row=2, column=3, sticky=W)
LABEL_BACKGROUND_X_POS = Label(master, text="BG X Coord:")
TOOLTOP_BACKGROUND_X_POS = CreateToolTip(LABEL_BACKGROUND_X_POS, "X coordinate of the CENTER of the background image.\nIncrease to move background right, decrease to move left.")
LABEL_BACKGROUND_X_POS.grid(row=3, column=2, sticky=E)
ENTRY_BACKGROUND_X_POS = Entry(master)
ENTRY_BACKGROUND_X_POS.insert(0, settings.BACKGROUND_X_POS)
ENTRY_BACKGROUND_X_POS.grid(row=3, column=3, sticky=W)
LABEL_BACKGROUND_Y_POS = Label(master, text="BG Y Coord:")
TOOLTOP_BACKGROUND_Y_POS = CreateToolTip(LABEL_BACKGROUND_Y_POS, "Y coordinate of the CENTER of the background image.\nIncrease to move background down, decrease to move up.")
LABEL_BACKGROUND_Y_POS.grid(row=4, column=2, sticky=E)
ENTRY_BACKGROUND_Y_POS = Entry(master)
ENTRY_BACKGROUND_Y_POS.insert(0, settings.BACKGROUND_Y_POS)
ENTRY_BACKGROUND_Y_POS.grid(row=4, column=3, sticky=W)
LABEL_IMAGE_X_POS = Label(master, text="Image X Coord:")
TOOLTIP_IMAGE_X_POS = CreateToolTip(LABEL_IMAGE_X_POS, "X coordinate of the CENTER of each message's associated image.\nIncrease to move images right, decrease to move left.")
LABEL_IMAGE_X_POS.grid(row=5, column=2, sticky=E)
ENTRY_IMAGE_X_POS = Entry(master)
ENTRY_IMAGE_X_POS.insert(0, settings.IMAGE_X_POS)
ENTRY_IMAGE_X_POS.grid(row=5, column=3, sticky=W)
LABEL_MESSAGE_X_POS = Label(master, text="Message X Coord:")
TOOLTIP_MESSAGE_X_POS = CreateToolTip(LABEL_MESSAGE_X_POS, "X coordinate of the START of each message.\nIncrease to move text right, decrease to move left.")
LABEL_MESSAGE_X_POS.grid(row=6, column=2, sticky=E)
ENTRY_MESSAGE_X_POS = Entry(master)
ENTRY_MESSAGE_X_POS.insert(0, settings.MESSAGE_X_POS)
ENTRY_MESSAGE_X_POS.grid(row=6, column=3, sticky=W)
LABEL_WINDOW_BG_COLOR = Label(master)
BUTTON_WINDOW_BG_COLOR = Button(master, text='Window BG Color:', command=lambda: colorChooser(LABEL_WINDOW_BG_COLOR, False))
TOOLTIP_WINDOW_BG_COLOR = CreateToolTip(BUTTON_WINDOW_BG_COLOR,
                                        "The background color of the window will show if no background image exists,\nor if the background image does not cover the entire window.")
BUTTON_WINDOW_BG_COLOR.grid(row=7, column=2, sticky=E, padx=4)
LABEL_WINDOW_BG_COLOR.configure(text=settings.WINDOW_BG_COLOR, background=settings.WINDOW_BG_COLOR)
LABEL_WINDOW_BG_COLOR.grid(row=7, column=3, sticky=W)
LABEL_WINDOW_BG_IMAGE = Label(master)
BUTTON_WINDOW_BG_IMAGE = Button(master, text='Window BG Image:', command=lambda: selectImageFile(LABEL_WINDOW_BG_IMAGE))
TOOLTIP_WINDOW_BG_IMAGE = CreateToolTip(BUTTON_WINDOW_BG_IMAGE, "The background image will persist during all messages.\nSet its coordinates with BG X Coord and BG Y Coord.")
BUTTON_WINDOW_BG_IMAGE.grid(row=8, column=2, sticky=E, padx=4, pady=4)
LABEL_WINDOW_BG_IMAGE.configure(text=getFileNameFromPath(settings.WINDOW_BG_IMAGE))
LABEL_WINDOW_BG_IMAGE.grid(row=8, column=3, sticky=W)

Label(master, text="Message Settings").grid(row=0, column=4, columnspan=3, sticky=W)
LABEL_MESSAGE_DURATION = Label(master, text="Message Duration:")
TOOLTIP_MESSAGE_DURATION = CreateToolTip(LABEL_MESSAGE_DURATION, "How long each message will be displayed in seconds.")
LABEL_MESSAGE_DURATION.grid(row=1, column=4, sticky=E)
ENTRY_MESSAGE_DURATION = Entry(master)
ENTRY_MESSAGE_DURATION.insert(0, settings.MESSAGE_DURATION)
ENTRY_MESSAGE_DURATION.grid(row=1, column=5, sticky=W)
LABEL_MESSAGE_FONT_FACE = Label(master, text="Message Font:")
TOOLTIP_MESSAGE_FONT_FACE = CreateToolTip(LABEL_MESSAGE_FONT_FACE,
                                          "The font to be used for all messages.\nDue to the way this program operates, it is STRONGLY recommended that you select a monospaced font.")
LABEL_MESSAGE_FONT_FACE.grid(row=2, column=4, sticky=E)
FONT_FAMILIES = sorted([f for f in font.families()])
FONT_COMBO_BOX = ttk.Combobox()
FONT_COMBO_BOX.configure(values=FONT_FAMILIES)
FONT_COMBO_BOX.set(settings.MESSAGE_FONT_FACE)
FONT_COMBO_BOX.grid(row=2, column=5, sticky=W)
LABEL_MESSAGE_COLOR = Label(master)
BUTTON_MESSAGE_COLOR = Button(master, text='Message Color:', command=lambda: colorChooser(LABEL_MESSAGE_COLOR, True))
TOOLTIP_MESSAGE_COLOR = CreateToolTip(BUTTON_MESSAGE_COLOR, "Color of the font used to display each message.")
BUTTON_MESSAGE_COLOR.grid(row=3, column=4, sticky=E, padx=4)
LABEL_MESSAGE_COLOR.configure(text=settings.MESSAGE_COLOR, foreground=settings.MESSAGE_COLOR)
LABEL_MESSAGE_COLOR.grid(row=3, column=5, sticky=W)
Label(master, text="Normal Message Font Settings").grid(row=4, column=4, sticky=W)
LABEL_NORMAL_FONT_SIZE = Label(master, text="Font Size:")
TOOLTIP_NORMAL_FONT_SIZE = CreateToolTip(LABEL_NORMAL_FONT_SIZE, "Font size for messages of standard length.")
LABEL_NORMAL_FONT_SIZE.grid(row=5, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE = Entry(master)
ENTRY_NORMAL_FONT_SIZE.insert(0, settings.NORMAL_FONT_SIZE)
ENTRY_NORMAL_FONT_SIZE.grid(row=5, column=5, sticky=W)
LABEL_NORMAL_FONT_SIZE_GAP = Label(master, text="Font Gap Size:")
TOOLTIP_NORMAL_FONT_SIZE_GAP = CreateToolTip(LABEL_NORMAL_FONT_SIZE_GAP,
                                             "This is the number of pixels between each character in a message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
LABEL_NORMAL_FONT_SIZE_GAP.grid(row=6, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP = Entry(master)
ENTRY_NORMAL_FONT_SIZE_GAP.insert(0, settings.NORMAL_FONT_SIZE_GAP)
ENTRY_NORMAL_FONT_SIZE_GAP.grid(row=6, column=5, sticky=W)
LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Label(master, text="Penalty For Spaces:")
TOOLTIP_NORMAL_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES,
                                                        "This determines how large the gaps are between words in each message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Entry(master)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.insert(0, settings.NORMAL_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=5, sticky=W)
LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Label(master, text="Max Length for Normal Message:")
TOOLTIP_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = CreateToolTip(LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE,
                                                        "When a message is longer than this many characters,\n it becomes a 'Smaller Font Message' and those settings apply.")
LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=8, column=4, sticky=E)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Entry(master)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.insert(0, settings.MAX_LENGTH_FOR_NORMAL_FONT_SIZE)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=8, column=5, sticky=W)

LABEL_MESSAGE_INTERMISSION = Label(master, text="Message Intermission:")
TOOLTIP_MESSAGE_INTERMISSION = CreateToolTip(LABEL_MESSAGE_INTERMISSION,
                                             "The amount of time between when the previous message disappears\nand the next message appears, in seconds. This can be a decimal value.")
LABEL_MESSAGE_INTERMISSION.grid(row=1, column=6, sticky=E)
ENTRY_MESSAGE_INTERMISSION = Entry(master)
ENTRY_MESSAGE_INTERMISSION.insert(0, settings.MESSAGE_INTERMISSION)
ENTRY_MESSAGE_INTERMISSION.grid(row=1, column=7, sticky=W)
# Label(master, text="Message Style:").grid(row=2, column=6, sticky=E)
# ENTRY_MESSAGE_STYLE = Entry(master)
# ENTRY_MESSAGE_STYLE.insert(0, settings.MESSAGE_STYLE)
# ENTRY_MESSAGE_STYLE.grid(row=2, column=7, sticky=W)
LABEL_MOVE_ALL_ON_LINE_DELAY = Label(master, text="Scroll Speed:")
TOOLTIP_MOVE_ALL_ON_LINE_DELAY = CreateToolTip(LABEL_MOVE_ALL_ON_LINE_DELAY,
                                               "This controls the general pace of the app.\nSetting this higher will significantly slow it down.\nValid values are 0 < x < 0.5.")
LABEL_MOVE_ALL_ON_LINE_DELAY.grid(row=2, column=6, sticky=E)
ENTRY_MOVE_ALL_ON_LINE_DELAY = Entry(master)
ENTRY_MOVE_ALL_ON_LINE_DELAY.insert(0, settings.MOVE_ALL_ON_LINE_DELAY)
ENTRY_MOVE_ALL_ON_LINE_DELAY.grid(row=2, column=7, sticky=W)
Label(master, text="Long Message Font Settings").grid(row=4, column=6, sticky=W)
LABEL_SMALLER_FONT_SIZE = Label(master, text="Font Size:")
TOOLTIP_SMALLER_FONT_SIZE = CreateToolTip(LABEL_SMALLER_FONT_SIZE, "Font size for messages of greater than standard length.")
LABEL_SMALLER_FONT_SIZE.grid(row=5, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE = Entry(master)
ENTRY_SMALLER_FONT_SIZE.insert(0, settings.SMALLER_FONT_SIZE)
ENTRY_SMALLER_FONT_SIZE.grid(row=5, column=7, sticky=W)
LABEL_SMALLER_FONT_SIZE_GAP = Label(master, text="Font Gap Size:")
TOOLTIP_SMALLER_FONT_SIZE_GAP = CreateToolTip(LABEL_SMALLER_FONT_SIZE_GAP,
                                              "This is the number of pixels between each character in a long message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
LABEL_SMALLER_FONT_SIZE_GAP.grid(row=6, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP = Entry(master)
ENTRY_SMALLER_FONT_SIZE_GAP.insert(0, settings.SMALLER_FONT_SIZE_GAP)
ENTRY_SMALLER_FONT_SIZE_GAP.grid(row=6, column=7, sticky=W)
LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Label(master, text="Penalty For Spaces:")
TOOLTIP_SMALLER_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES,
                                                         "This determines how large the gaps are between words in each long message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Entry(master)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.insert(0, settings.SMALLER_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=7, sticky=W)

Button(master, text='Restore Defaults', command=getDefaultSettings).grid(row=9, column=6, pady=4, padx=4, sticky=E)
Button(master, text='Save Settings', command=updateSettingsJSON).grid(row=9, column=7, pady=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=9, column=7, padx=4, pady=4, sticky=E)
master.mainloop()
mainloop()
