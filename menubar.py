import json
import sys
from tkinter import Menu, filedialog, messagebox

import validateDepartureSettings
import validateFontSettings
import validateMessageSettings
import validateWindowSettings

class Menubar:
    def __init__(self, master, fields, sFrame, mFrame, bgFrame):
        self.menubar = Menu(master)
        self.currentlyLoadedFile = None
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New Settings", command=lambda: self.loadDefault(sFrame, mFrame, bgFrame, fields))
        self.filemenu.add_command(label="Load Settings", command=lambda: self.loadFile(fields, mFrame, bgFrame, None))
        self.filemenu.add_command(label="Save Settings", command=lambda: self.saveAsFile(mFrame, fields, True))
        self.filemenu.add_command(label="Save Settings as...", command=lambda: self.saveAsFile(mFrame, fields, False))
        self.filemenu.insert_separator(4)
        self.filemenu.add_command(label="Quit", command=lambda: exit(1))
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Preview with current settings")
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        master.config(menu=self.menubar)

    def saveAsFile(self, mFrame, fields, overwriteLastLoadedOrSavedFile):
        if self.validateBeforeSaving(fields):
            if not overwriteLastLoadedOrSavedFile:
                saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("StreamTicker Settings", "*.sts")], defaultextension='.json')
            else:
                saveFile = self.currentlyLoadedFile
                if saveFile is None:
                    saveFile = filedialog.asksaveasfilename(initialdir=sys.argv[0], title="Save as...", filetypes=[("StreamTicker Settings", "*.sts")], defaultextension='.json')
            if not saveFile or saveFile is None:
                return
            self.saveJsonToFile(mFrame, fields, saveFile)

    def loadDefault(self, sFrame, mFrame, bgFrame, fields):
        fields.getDefaultValues(True, mFrame, bgFrame)
        sFrame.updateXScales()
        sFrame.updateYScales()

    def loadFile(self, fields, mFrame, bgFrame, path):
        if path:
            fileToLoad = path
        else:
            fileToLoad = filedialog.askopenfilename(initialdir=sys.argv[0], title="Select layout file", filetypes=[("StreamTicker Settings", "*.sts")])
        if not fileToLoad or fileToLoad is None:
            return
        if fields.loadJson(fileToLoad, mFrame, bgFrame):
            self.currentlyLoadedFile = fileToLoad

    def saveJsonToFile(self, mFrame, fields, saveFile):
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
                              'MESSAGE_COLOR': mFrame.LABEL_MESSAGE_COLOR.cget("text"),
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
                             'MOVE_ALL_ON_LINE_DELAY': fields.convertDelayNameToValue(fields.VAR_ENTRY_MOVE_ALL_ON_LINE_DELAY.get())}}
        with open(saveFile, 'w') as f:
            json.dump(result, f, indent=4)
        self.currentlyLoadedFile = saveFile
        messagebox.showinfo("Success", "Settings saved!")

    def validateBeforeSaving(self, fields):
        return validateDepartureSettings.validate(fields) \
               and validateWindowSettings.validate(fields) \
               and validateMessageSettings.validate(fields) \
               and validateFontSettings.validate(fields)
