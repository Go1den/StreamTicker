import json
from collections import OrderedDict
from tkinter import *
from tkinter import messagebox, colorchooser, filedialog, font, ttk

import helperMethods
import validateDepartureSettings
import validateFontSettings
import validateMessageSettings
import validateWindowSettings
from createToolTip import CreateToolTip
from settingsGUIFields import SettingsGUIFields

CURRENTLY_LOADED_FILE = None

def updateXScales():
    SCALE_2.configure(to=SCALE.get(), tickinterval=SCALE.get())
    SCALE_5.configure(to=SCALE.get(), tickinterval=SCALE.get())
    SCALE_4.configure(to=SCALE.get(), tickinterval=SCALE.get())

def updateYScales():
    SCALE_6.configure(to=SCALE_3.get(), tickinterval=SCALE_3.get())

def loadFile(fields, messageLabel, windowLabel, path):
    global CURRENTLY_LOADED_FILE
    # fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select layout file", filetypes=[("json files", "*.json")])
    if path:
        fileToLoad = path
    else:
        fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select layout file", filetypes=[("StreamTicker Settings", "*.sts")])
    if fileToLoad is None:
        return
    if fields.loadJson(fileToLoad, messageLabel, windowLabel):
        CURRENTLY_LOADED_FILE = fileToLoad

def saveAsFile(fields, overwriteLastLoadedOrSavedFile):
    if validateBeforeSaving(fields):
        if not overwriteLastLoadedOrSavedFile:
            # saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("json files", "*.json")], defaultextension='.json')
            saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("StreamTicker Settings", "*.sts")], defaultextension='.json')
        else:
            saveFile = CURRENTLY_LOADED_FILE
        if saveFile is None:
            return
        saveJsonToFile(fields, saveFile)

def selectImageFile(fields):
    filename = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select image file", filetypes=[("png files", "*.png")])
    fields.VAR_DISPLAY_WINDOW_BG_IMAGE.set(helperMethods.getFileNameFromPath(filename))
    fields.VAR_PATH_WINDOW_BG_IMAGE.set(filename)

def updateMessageColor(label, fields):
    color = colorchooser.askcolor(title="Select color")
    fields.VAR_LABEL_MESSAGE_COLOR_TEXT.set(color[1])
    fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND = color[1]
    label.configure(foreground=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)

def updateWindowColor(label, fields):
    color = colorchooser.askcolor(title="Select color")
    fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.set(color[1])
    fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND = color[1]
    label.configure(background=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)

def colorChooser(label, isForeground):
    color = colorchooser.askcolor(title="Select color")
    if isForeground:
        label.configure(text=color[1], foreground=color[1])
    else:
        label.configure(text=color[1], background=color[1])

def setCheckState(bool, checkbox):
    if bool:
        checkbox.select()

def validateBeforeSaving(fields):
    return validateDepartureSettings.validate(fields) \
           and validateWindowSettings.validate(fields) \
           and validateMessageSettings.validate(fields) \
           and validateFontSettings.validate(fields)

def saveJsonToFile(fields, saveFile):
    global CURRENTLY_LOADED_FILE
    result = {'departure': {'ENABLE_DEPARTING_BY_SLIDING_RIGHT': fields.VAR_CHECK_SLIDING_RIGHT.get(),
                            'ENABLE_DEPARTING_BY_SLIDING_LEFT': fields.VAR_CHECK_SLIDING_LEFT.get(),
                            'ENABLE_DEPARTING_BY_SLIDING_UP': fields.VAR_CHECK_SLIDING_UP.get(),
                            'ENABLE_DEPARTING_BY_SLIDING_DOWN': fields.VAR_CHECK_SLIDING_DOWN.get(),
                            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT': fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.get(),
                            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT': fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.get(),
                            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER': fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.get(),
                            'ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES': fields.VAR_CHECK_COVERING_WITH_RECTANGLES.get()},
              'message': {'DEFAULT_IMAGE': fields.VAR_DEFAULT_IMAGE.get(),
                          'MESSAGE_STYLE': fields.VAR_MESSAGE_STYLE.get(),
                          'MESSAGE_DURATION': fields.VAR_ENTRY_MESSAGE_DURATION.get(),
                          'MESSAGE_INTERMISSION': fields.VAR_ENTRY_MESSAGE_INTERMISSION.get(),
                          'MESSAGE_COLOR': LABEL_MESSAGE_COLOR.cget("text"),
                          'MESSAGE_FONT_FACE': fields.VAR_FONT_COMBO_BOX.get(),
                          'MAX_LENGTH_FOR_NORMAL_FONT_SIZE': fields.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.get(),
                          'NORMAL_FONT_SIZE': fields.VAR_ENTRY_NORMAL_FONT_SIZE.get(),
                          'NORMAL_FONT_SIZE_GAP': fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP.get(),
                          'NORMAL_FONT_SIZE_GAP_FOR_SPACES': fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.get(),
                          'SMALLER_FONT_SIZE': fields.VAR_ENTRY_SMALLER_FONT_SIZE.get(),
                          'SMALLER_FONT_SIZE_GAP': fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP.get(),
                          'SMALLER_FONT_SIZE_GAP_FOR_SPACES': fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.get()},
              'window': {'MESSAGE_X_POS': fields.VAR_ENTRY_MESSAGE_X_POS.get(),
                         'IMAGE_X_POS': fields.VAR_ENTRY_IMAGE_X_POS.get(),
                         'WINDOW_WIDTH': fields.VAR_ENTRY_WINDOW_WIDTH.get(),
                         'WINDOW_HEIGHT': fields.VAR_ENTRY_WINDOW_HEIGHT.get(),
                         'WINDOW_BG_COLOR': fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT.get(),
                         'WINDOW_BG_IMAGE': fields.VAR_PATH_WINDOW_BG_IMAGE.get(),
                         'BACKGROUND_X_POS': fields.VAR_ENTRY_BACKGROUND_X_POS.get(),
                         'BACKGROUND_Y_POS': fields.VAR_ENTRY_BACKGROUND_Y_POS.get(),
                         'MOVE_ALL_ON_LINE_DELAY': fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get()}}
    with open(saveFile, 'w') as f:
        json.dump(result, f, indent=4)
    CURRENTLY_LOADED_FILE = saveFile
    messagebox.showinfo("Success", "Settings saved!")

master = Tk()
master.wm_title("StreamTicker Settings")
master.iconbitmap("stIcon.ico")

fields = SettingsGUIFields()

dFrame = Frame(master)
dFrame.grid(row=0, column=0, columnspan=2)
wFrame = Frame(master)
wFrame.grid(row=0, column=2, columnspan=2)
mFrame = Frame(master)
mFrame.grid(row=0, column=4, columnspan=4)

LABEL_MESSAGE_COLOR = Label(mFrame, textvariable=fields.VAR_LABEL_MESSAGE_COLOR_TEXT, foreground=fields.VAR_LABEL_MESSAGE_COLOR_FOREGROUND)
LABEL_WINDOW_BG_COLOR = Label(wFrame, textvariable=fields.VAR_LABEL_WINDOW_BG_COLOR_TEXT, background=fields.VAR_LABEL_WINDOW_BG_COLOR_BACKGROUND)

menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Settings", command=lambda: fields.getDefaultValues(True, LABEL_MESSAGE_COLOR, LABEL_WINDOW_BG_COLOR))
filemenu.add_command(label="Load Settings", command=lambda: loadFile(fields, LABEL_MESSAGE_COLOR, LABEL_WINDOW_BG_COLOR, None))
filemenu.add_command(label="Save Settings", command=lambda: saveAsFile(fields, True))
filemenu.add_command(label="Save Settings as...", command=lambda: saveAsFile(fields, False))
filemenu.insert_separator(4)
filemenu.add_command(label="Quit", command=lambda: exit(1))
menubar.add_cascade(label="File", menu=filemenu)
master.config(menu=menubar)

Label(dFrame, text="Departure Settings").grid(row=0, column=0, columnspan=3, sticky=W)
Label(dFrame, text="Allow messages to leave the screen by:").grid(row=1, column=0, columnspan=3, sticky=W)

CBOX_SLIDING_RIGHT = Checkbutton(dFrame, variable=fields.VAR_CHECK_SLIDING_RIGHT)
CBOX_SLIDING_RIGHT.grid(row=2, column=0, sticky=E)
Label(dFrame, text="Sliding right").grid(row=2, column=1, sticky=W)

CBOX_SLIDING_LEFT = Checkbutton(dFrame, var=fields.VAR_CHECK_SLIDING_LEFT)
CBOX_SLIDING_LEFT.grid(row=3, column=0, sticky=E)
Label(dFrame, text="Sliding left").grid(row=3, column=1, sticky=W)

CBOX_SLIDING_UP = Checkbutton(dFrame, var=fields.VAR_CHECK_SLIDING_UP)
CBOX_SLIDING_UP.grid(row=4, column=0, sticky=E)
Label(dFrame, text="Sliding up").grid(row=4, column=1, sticky=W)

CBOX_SLIDING_DOWN = Checkbutton(dFrame, var=fields.VAR_CHECK_SLIDING_DOWN)
CBOX_SLIDING_DOWN.grid(row=5, column=0, sticky=E)
Label(dFrame, text="Sliding down").grid(row=5, column=1, sticky=W)

CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = Checkbutton(dFrame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT.grid(row=6, column=0, sticky=E)
Label(dFrame, text="Alternating up/down working backwards").grid(row=6, column=1, sticky=W)

CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = Checkbutton(dFrame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT)
CBOX_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT.grid(row=7, column=0, sticky=E)
Label(dFrame, text="Alternating up/down working forwards").grid(row=7, column=1, sticky=W)

CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = Checkbutton(dFrame, var=fields.VAR_CHECK_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER)
CBOX_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER.grid(row=8, column=0, sticky=E)
Label(dFrame, text="Alternating up/down, random order").grid(row=8, column=1, sticky=W)

# CBOX_COVERING_WITH_RECTANGLES = Checkbutton(dFrame, var=fields.VAR_CHECK_COVERING_WITH_RECTANGLES)
# CBOX_COVERING_WITH_RECTANGLES.grid(row=8, column=0)
# Label(dFrame, text="Covering with rectangles").grid(row=8, column=1)

Label(wFrame, text="Background Settings").grid(row=0, column=2, sticky=W, padx=40)
LABEL_WINDOW_WIDTH = Label(wFrame, text="Window Width:")
TOOLTOP_WINDOW_WIDTH = CreateToolTip(LABEL_WINDOW_WIDTH, "Width of the window in pixels.\nValid values are between 400 and 1920.")
LABEL_WINDOW_WIDTH.grid(row=1, column=2, sticky=E)
ENTRY_WINDOW_WIDTH = Entry(wFrame, textvariable=fields.VAR_ENTRY_WINDOW_WIDTH)
ENTRY_WINDOW_WIDTH.grid(row=1, column=3, sticky=W)
LABEL_WINDOW_HEIGHT = Label(wFrame, text="Window Height:")
TOOLTOP_WINDOW_HEIGHT = CreateToolTip(LABEL_WINDOW_HEIGHT, "Height of the window in pixels.\nValid values are multiples of 4 between 44 and 1080.")
LABEL_WINDOW_HEIGHT.grid(row=2, column=2, sticky=E)
ENTRY_WINDOW_HEIGHT = Entry(wFrame, textvariable=fields.VAR_ENTRY_WINDOW_HEIGHT)
ENTRY_WINDOW_HEIGHT.grid(row=2, column=3, sticky=W)
LABEL_BACKGROUND_X_POS = Label(wFrame, text="BG X Coord:")
TOOLTOP_BACKGROUND_X_POS = CreateToolTip(LABEL_BACKGROUND_X_POS, "X coordinate of the CENTER of the background image.\nIncrease to move background right, decrease to move left.")
LABEL_BACKGROUND_X_POS.grid(row=3, column=2, sticky=E)
ENTRY_BACKGROUND_X_POS = Entry(wFrame, textvariable=fields.VAR_ENTRY_BACKGROUND_X_POS)
ENTRY_BACKGROUND_X_POS.grid(row=3, column=3, sticky=W)
LABEL_BACKGROUND_Y_POS = Label(wFrame, text="BG Y Coord:")
TOOLTOP_BACKGROUND_Y_POS = CreateToolTip(LABEL_BACKGROUND_Y_POS, "Y coordinate of the CENTER of the background image.\nIncrease to move background down, decrease to move up.")
LABEL_BACKGROUND_Y_POS.grid(row=4, column=2, sticky=E)
ENTRY_BACKGROUND_Y_POS = Entry(wFrame, textvariable=fields.VAR_ENTRY_BACKGROUND_Y_POS)
ENTRY_BACKGROUND_Y_POS.grid(row=4, column=3, sticky=W)
LABEL_IMAGE_X_POS = Label(wFrame, text="Image X Coord:")
TOOLTIP_IMAGE_X_POS = CreateToolTip(LABEL_IMAGE_X_POS, "X coordinate of the CENTER of each message's associated image.\nIncrease to move images right, decrease to move left.")
LABEL_IMAGE_X_POS.grid(row=5, column=2, sticky=E)
ENTRY_IMAGE_X_POS = Entry(wFrame, textvariable=fields.VAR_ENTRY_IMAGE_X_POS)
ENTRY_IMAGE_X_POS.grid(row=5, column=3, sticky=W)
LABEL_MESSAGE_X_POS = Label(wFrame, text="Message X Coord:")
TOOLTIP_MESSAGE_X_POS = CreateToolTip(LABEL_MESSAGE_X_POS, "X coordinate of the START of each message.\nIncrease to move text right, decrease to move left.")
LABEL_MESSAGE_X_POS.grid(row=6, column=2, sticky=E)
ENTRY_MESSAGE_X_POS = Entry(wFrame, textvariable=fields.VAR_ENTRY_MESSAGE_X_POS)
ENTRY_MESSAGE_X_POS.grid(row=6, column=3, sticky=W)

BUTTON_WINDOW_BG_COLOR = Button(wFrame, text='Window BG Color:', command=lambda: updateWindowColor(LABEL_WINDOW_BG_COLOR, fields))
TOOLTIP_WINDOW_BG_COLOR = CreateToolTip(BUTTON_WINDOW_BG_COLOR,
                                        "The background color of the window will show if no background image exists,\nor if the background image does not cover the entire window.")
BUTTON_WINDOW_BG_COLOR.grid(row=7, column=2, sticky=E, padx=4)
LABEL_WINDOW_BG_COLOR.grid(row=7, column=3, sticky=W)
LABEL_WINDOW_BG_IMAGE = Label(wFrame, textvariable=fields.VAR_DISPLAY_WINDOW_BG_IMAGE)
BUTTON_WINDOW_BG_IMAGE = Button(wFrame, text='Window BG Image:', command=lambda: selectImageFile(fields))
TOOLTIP_WINDOW_BG_IMAGE = CreateToolTip(BUTTON_WINDOW_BG_IMAGE, "The background image will persist during all messages.\nSet its coordinates with BG X Coord and BG Y Coord.")
BUTTON_WINDOW_BG_IMAGE.grid(row=8, column=2, sticky=E, padx=4, pady=4)
LABEL_WINDOW_BG_IMAGE.grid(row=8, column=3, sticky=W)

Label(mFrame, text="Message Settings").grid(row=0, column=4, columnspan=3, sticky=W)
LABEL_MESSAGE_DURATION = Label(mFrame, text="Message Duration:")
TOOLTIP_MESSAGE_DURATION = CreateToolTip(LABEL_MESSAGE_DURATION, "How long each message will be displayed in seconds.")
LABEL_MESSAGE_DURATION.grid(row=1, column=4, sticky=E)
ENTRY_MESSAGE_DURATION = Entry(mFrame, textvariable=fields.VAR_ENTRY_MESSAGE_DURATION)
ENTRY_MESSAGE_DURATION.grid(row=1, column=5, sticky=W)
LABEL_MESSAGE_FONT_FACE = Label(mFrame, text="Message Font:")
TOOLTIP_MESSAGE_FONT_FACE = CreateToolTip(LABEL_MESSAGE_FONT_FACE,
                                          "The font to be used for all messages.\nDue to the way this program operates, it is STRONGLY recommended that you select a monospaced font.")
LABEL_MESSAGE_FONT_FACE.grid(row=2, column=4, sticky=E)
FONT_FAMILIES = sorted([f for f in font.families()])
FONT_COMBO_BOX = ttk.Combobox(mFrame, values=FONT_FAMILIES, textvariable=fields.VAR_FONT_COMBO_BOX, state="readonly")
FONT_COMBO_BOX.grid(row=2, column=5, sticky=W)

BUTTON_MESSAGE_COLOR = Button(mFrame, text='Message Color:', command=lambda: updateMessageColor(LABEL_MESSAGE_COLOR, fields))
TOOLTIP_MESSAGE_COLOR = CreateToolTip(BUTTON_MESSAGE_COLOR, "Color of the font used to display each message.")
BUTTON_MESSAGE_COLOR.grid(row=3, column=4, sticky=E, padx=4)
LABEL_MESSAGE_COLOR.grid(row=3, column=5, sticky=W)
Label(mFrame, text="Normal Message Font Settings").grid(row=4, column=4, sticky=W)
LABEL_NORMAL_FONT_SIZE = Label(mFrame, text="Font Size:")
TOOLTIP_NORMAL_FONT_SIZE = CreateToolTip(LABEL_NORMAL_FONT_SIZE, "Font size for messages of standard length.")
LABEL_NORMAL_FONT_SIZE.grid(row=5, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE = Entry(mFrame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE)
ENTRY_NORMAL_FONT_SIZE.grid(row=5, column=5, sticky=W)
LABEL_NORMAL_FONT_SIZE_GAP = Label(mFrame, text="Font Gap Size:")
TOOLTIP_NORMAL_FONT_SIZE_GAP = CreateToolTip(LABEL_NORMAL_FONT_SIZE_GAP,
                                             "This is the number of pixels between each character in a message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
LABEL_NORMAL_FONT_SIZE_GAP.grid(row=6, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP = Entry(mFrame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP)
ENTRY_NORMAL_FONT_SIZE_GAP.grid(row=6, column=5, sticky=W)
LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Label(mFrame, text="Penalty For Spaces:")
TOOLTIP_NORMAL_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES,
                                                        "This determines how large the gaps are between words in each message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
LABEL_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=4, sticky=E)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES = Entry(mFrame, textvariable=fields.VAR_ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_NORMAL_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=5, sticky=W)
LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Label(mFrame, text="Max Length for Normal Message:")
TOOLTIP_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = CreateToolTip(LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE,
                                                        "When a message is longer than this many characters,\nit becomes a 'Long Message' and those settings apply.")
LABEL_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=8, column=4, sticky=E)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE = Entry(mFrame, textvariable=fields.VAR_ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE)
ENTRY_MAX_LENGTH_FOR_NORMAL_FONT_SIZE.grid(row=8, column=5, sticky=W)

LABEL_MESSAGE_INTERMISSION = Label(mFrame, text="Message Intermission:")
TOOLTIP_MESSAGE_INTERMISSION = CreateToolTip(LABEL_MESSAGE_INTERMISSION,
                                             "The amount of time between when the previous message disappears\nand the next message appears, in seconds. This can be a decimal value.")
LABEL_MESSAGE_INTERMISSION.grid(row=1, column=6, sticky=E)
ENTRY_MESSAGE_INTERMISSION = Entry(mFrame, textvariable=fields.VAR_ENTRY_MESSAGE_INTERMISSION)
ENTRY_MESSAGE_INTERMISSION.grid(row=1, column=7, sticky=W)
# Label(mFrame, text="Message Style:").grid(row=2, column=6, sticky=E)
# ENTRY_MESSAGE_STYLE = Entry(mFrame)
# ENTRY_MESSAGE_STYLE.insert(0, settings.MESSAGE_STYLE)
# ENTRY_MESSAGE_STYLE.grid(row=2, column=7, sticky=W)
LABEL_MOVE_ALL_ON_LINE_DELAY = Label(mFrame, text="Scroll Speed:")
TOOLTIP_MOVE_ALL_ON_LINE_DELAY = CreateToolTip(LABEL_MOVE_ALL_ON_LINE_DELAY,
                                               "This controls the general pace of the app.\nSetting this higher will significantly slow it down.\nValid values are 0 < x < 0.5.")
LABEL_MOVE_ALL_ON_LINE_DELAY.grid(row=2, column=6, sticky=E)
ENTRY_MOVE_ALL_ON_LINE_DELAY = Entry(mFrame, textvariable=fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY)
ENTRY_MOVE_ALL_ON_LINE_DELAY.grid(row=2, column=7, sticky=W)
Label(mFrame, text="Long Message Font Settings").grid(row=4, column=6, sticky=W)
LABEL_SMALLER_FONT_SIZE = Label(mFrame, text="Font Size:")
TOOLTIP_SMALLER_FONT_SIZE = CreateToolTip(LABEL_SMALLER_FONT_SIZE, "Font size for messages of greater than standard length.")
LABEL_SMALLER_FONT_SIZE.grid(row=5, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE = Entry(mFrame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE)
ENTRY_SMALLER_FONT_SIZE.grid(row=5, column=7, sticky=W)
LABEL_SMALLER_FONT_SIZE_GAP = Label(mFrame, text="Font Gap Size:")
TOOLTIP_SMALLER_FONT_SIZE_GAP = CreateToolTip(LABEL_SMALLER_FONT_SIZE_GAP,
                                              "This is the number of pixels between each character in a long message.\nIf your messages seem squished, raise this value.\nIf they seem stretched, lower it.")
LABEL_SMALLER_FONT_SIZE_GAP.grid(row=6, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP = Entry(mFrame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP)
ENTRY_SMALLER_FONT_SIZE_GAP.grid(row=6, column=7, sticky=W)
LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Label(mFrame, text="Penalty For Spaces:")
TOOLTIP_SMALLER_FONT_SIZE_GAP_FOR_SPACES = CreateToolTip(LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES,
                                                         "This determines how large the gaps are between words in each long message.\nIncreasing it will move words closer together.\nDecreasing it will move words farther apart.")
LABEL_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=6, sticky=E)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES = Entry(mFrame, textvariable=fields.VAR_ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES)
ENTRY_SMALLER_FONT_SIZE_GAP_FOR_SPACES.grid(row=7, column=7, sticky=W)

sliderFrame = Frame(master)
sliderFrame.grid(row=9, column=0, columnspan=10)

LABEL_SCALE = Label(sliderFrame)
LABEL_SCALE.grid(row=1, column=0, sticky=W)
SCALE = Scale(sliderFrame, from_=400, to=1920, tickinterval=1520, orient=HORIZONTAL, resolution=4, length=500, command=lambda x: updateXScales(), label="Window Width in Pixels:")
SCALE.set(400)
SCALE.grid(row=1, column=1, sticky=W)

LABEL_SCALE_2 = Label(sliderFrame)
LABEL_SCALE_2.grid(row=1, column=2, sticky=W)
SCALE_2 = Scale(sliderFrame, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=4, length=500, label="Image X Coordinate (location of image center)")
SCALE_2.set(400)
SCALE_2.grid(row=1, column=3, sticky=W)

LABEL_SCALE_4 = Label(sliderFrame)
LABEL_SCALE_4.grid(row=2, column=0, sticky=W)
SCALE_4 = Scale(sliderFrame, from_=0, to=400, tickinterval=40, orient=HORIZONTAL, resolution=4, length=500, label="Message X Coordinate (location of message start)")
SCALE_4.set(400)
SCALE_4.grid(row=2, column=1, sticky=W)

LABEL_SCALE_5 = Label(sliderFrame)
LABEL_SCALE_5.grid(row=2, column=2, sticky=W)
SCALE_5 = Scale(sliderFrame, from_=0, to=400, tickinterval=400, orient=HORIZONTAL, resolution=4, length=500, label="Background X Coordinate (location of BG center)")
SCALE_5.set(400)
SCALE_5.grid(row=2, column=3, sticky=W)

LABEL_SCALE_3 = Label(sliderFrame)
LABEL_SCALE_3.grid(row=3, column=0, sticky=W)
SCALE_3 = Scale(sliderFrame, from_=40, to=1080, tickinterval=1040, orient=HORIZONTAL, resolution=4, length=500, command=lambda x: updateYScales(), label="Window Height in Pixels:")
SCALE_3.set(40)
SCALE_3.grid(row=3, column=1, sticky=W)

LABEL_SCALE_6 = Label(sliderFrame)
LABEL_SCALE_6.grid(row=3, column=2, sticky=W)
SCALE_6 = Scale(sliderFrame, from_=0, to=40, tickinterval=40, orient=HORIZONTAL, resolution=4, length=500, label="Background Y Coordinate (location of BG center)")
SCALE_6.set(40)
SCALE_6.grid(row=3, column=3, sticky=W)

master.mainloop()
mainloop()
