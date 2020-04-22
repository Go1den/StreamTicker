from tkinter import Frame, Button, E, GROOVE

from validations import validateDepartureSettings, validateWindowSettings, validateMessageSettings, validateFontSettings

class OkCancelFrame:
    def __init__(self, master, fields):
        self.frame = Frame(master)

        self.okButton = Button(self.frame, text="OK", width=10, bd=2, relief=GROOVE, command=lambda: self.updateCurrentSettings(master, fields))
        self.okButton.grid(row=0, column=0, sticky=E, padx=10)

        self.cancelButton = Button(self.frame, text="Cancel", width=10, bd=2, relief=GROOVE, command=lambda: master.destroy())
        self.cancelButton.grid(row=0, column=1, sticky=E)

    def validateBeforeSaving(self, fields):
        return validateDepartureSettings.validate(fields) \
               and validateWindowSettings.validate(fields) \
               and validateMessageSettings.validate(fields) \
               and validateFontSettings.validate(fields)

    def updateCurrentSettings(self, master, fields):
        if self.validateBeforeSaving(fields):
            print("Valid!")
            #Todo: we need to have this update the main window's settings variable instead of saving it anywhere else
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
                                  # 'MESSAGE_COLOR': mFrame.LABEL_MESSAGE_COLOR.cget("text"), #TODO: How???
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
            master.destroy()
