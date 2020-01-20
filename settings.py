import json

class Settings:
    def __init__(self):
        with open("settings.json") as f:
            self.data = json.loads(f.read())

        # Departure settings
        d = self.data['departure'][0]
        self.ENABLE_DEPARTING_BY_SLIDING_RIGHT = bool(d['ENABLE_DEPARTING_BY_SLIDING_RIGHT'] or False)
        self.ENABLE_DEPARTING_BY_SLIDING_LEFT = bool(d['ENABLE_DEPARTING_BY_SLIDING_LEFT'] or False)
        self.ENABLE_DEPARTING_BY_SLIDING_UP = bool(d['ENABLE_DEPARTING_BY_SLIDING_UP'] or False)
        self.ENABLE_DEPARTING_BY_SLIDING_DOWN = bool(d['ENABLE_DEPARTING_BY_SLIDING_DOWN'] or False)
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = bool(d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT'] or False)
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = bool(d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT'] or False)
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = bool(d['ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER'] or False)
        self.ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES = bool(d['ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES'] or False)

        # Message settings
        m = self.data['message'][0]
        self.MESSAGE_DURATION = int(m['MESSAGE_DURATION'] or 5)
        self.MESSAGE_INTERMISSION = float(m['MESSAGE_INTERMISSION'] or .5)
        self.MESSAGE_COLOR = str(m['MESSAGE_COLOR'] or "white")
        self.MESSAGE_STYLE = str(m['MESSAGE_STYLE'] or "bold")
        self.MESSAGE_FONT_FACE = str(m['MESSAGE_FONT_FACE'] or "Courier New")
        self.MAX_LENGTH_FOR_NORMAL_FONT_SIZE = int(m['MAX_LENGTH_FOR_NORMAL_FONT_SIZE'] or 16)
        self.NORMAL_FONT_SIZE = int(m['NORMAL_FONT_SIZE'] or 26)
        self.NORMAL_FONT_SIZE_GAP = int(m['NORMAL_FONT_SIZE_GAP'] or 20)
        self.NORMAL_FONT_SIZE_GAP_FOR_SPACES = int(m['NORMAL_FONT_SIZE_GAP_FOR_SPACES'] or 4)
        self.SMALLER_FONT_SIZE = int(m['SMALLER_FONT_SIZE'] or 22)
        self.SMALLER_FONT_SIZE_GAP = int(m['SMALLER_FONT_SIZE_GAP'] or 16)
        self.SMALLER_FONT_SIZE_GAP_FOR_SPACES = int(m['SMALLER_FONT_SIZE_GAP_FOR_SPACES'] or 6)
        self.DEFAULT_IMAGE = str(m['DEFAULT_IMAGE'] or "imagefiles/stLogo28.png")

        # Window settings
        w = self.data['window'][0]
        self.MESSAGE_X_POS = int(w['MESSAGE_X_POS'] or 60)
        self.IMAGE_X_POS = int(w['IMAGE_X_POS'] or 21)
        self.WINDOW_WIDTH = int(w['WINDOW_WIDTH'] or 400)
        self.WINDOW_HEIGHT = int(w['WINDOW_HEIGHT'] or 44)
        self.WINDOW_BG_COLOR = str(w['WINDOW_BG_COLOR'] or "black")
        self.WINDOW_BG_IMAGE = str(w['WINDOW_BG_IMAGE'] or "imagefiles/background.png")
        self.BACKGROUND_X_POS = int(w['BACKGROUND_X_POS'] or 202)
        self.BACKGROUND_Y_POS = int(w['BACKGROUND_Y_POS'] or 24)
        self.MOVE_ALL_ON_LINE_DELAY = float(w['MOVE_ALL_ON_LINE_DELAY'] or .004)
