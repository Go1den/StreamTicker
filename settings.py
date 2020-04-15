class Settings:
    def __init__(self, data):
        self.data = data
        self.ACCEPTABLE_STYLES = ['bold', 'normal', 'italic', 'bold italic', 'oblique', 'regular']
        # Departure settings
        d = self.data['departure'] if 'departure' in self.data else {}
        if isinstance(d, list):
            d = d[0]
        self.ENABLE_DEPARTING_BY_SLIDING_RIGHT = d['ENABLE_DEPARTING_BY_SLIDING_RIGHT'] if 'ENABLE_DEPARTING_BY_SLIDING_RIGHT' in d else True
        self.ENABLE_DEPARTING_BY_SLIDING_LEFT = d['ENABLE_DEPARTING_BY_SLIDING_LEFT'] if 'ENABLE_DEPARTING_BY_SLIDING_LEFT' in d else True
        self.ENABLE_DEPARTING_BY_SLIDING_UP = d['ENABLE_DEPARTING_BY_SLIDING_UP'] if 'ENABLE_DEPARTING_BY_SLIDING_UP' in d else True
        self.ENABLE_DEPARTING_BY_SLIDING_DOWN = d['ENABLE_DEPARTING_BY_SLIDING_DOWN'] if 'ENABLE_DEPARTING_BY_SLIDING_DOWN' in d else True
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = d[
            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT'] if 'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT' in d else True
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = d[
            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT'] if 'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT' in d else True
        self.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = d[
            'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER'] if 'ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER' in d else True
        self.ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES = d['ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES'] if 'ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES' in d else True

        # Message settings
        m = self.data['message'] if 'message' in self.data else {}
        if isinstance(m, list):
            m = m[0]
        self.MESSAGE_DURATION = int(m['MESSAGE_DURATION'] if 'MESSAGE_DURATION' in m else 5)
        self.MESSAGE_INTERMISSION = float(m['MESSAGE_INTERMISSION'] if 'MESSAGE_INTERMISSION' in m else .5)
        self.MESSAGE_COLOR = str(m['MESSAGE_COLOR'] if 'MESSAGE_COLOR' in m else "white")
        self.MESSAGE_STYLE = str(m['MESSAGE_STYLE'] if 'MESSAGE_STYLE' in m and m['MESSAGE_STYLE'] in self.ACCEPTABLE_STYLES else "normal")
        self.MESSAGE_FONT_FACE = str(m['MESSAGE_FONT_FACE'] if 'MESSAGE_FONT_FACE' in m else "Courier New")
        self.MAX_LENGTH_FOR_NORMAL_FONT_SIZE = int(m['MAX_LENGTH_FOR_NORMAL_FONT_SIZE'] if 'MAX_LENGTH_FOR_NORMAL_FONT_SIZE' in m else 16)
        self.NORMAL_FONT_SIZE = int(m['NORMAL_FONT_SIZE'] if 'NORMAL_FONT_SIZE' in m else 26)
        self.NORMAL_FONT_SIZE_GAP = int(m['NORMAL_FONT_SIZE_GAP'] if 'NORMAL_FONT_SIZE_GAP' in m else 20)
        self.NORMAL_FONT_SIZE_GAP_FOR_SPACES = int(m['NORMAL_FONT_SIZE_GAP_FOR_SPACES'] if 'NORMAL_FONT_SIZE_GAP_FOR_SPACES' in m else 4)
        self.SMALLER_FONT_SIZE = int(m['SMALLER_FONT_SIZE'] if 'SMALLER_FONT_SIZE' in m else 22)
        self.SMALLER_FONT_SIZE_GAP = int(m['SMALLER_FONT_SIZE_GAP'] if 'SMALLER_FONT_SIZE_GAP' in m else 16)
        self.SMALLER_FONT_SIZE_GAP_FOR_SPACES = int(m['SMALLER_FONT_SIZE_GAP_FOR_SPACES'] if 'SMALLER_FONT_SIZE_GAP_FOR_SPACES' in m else 6)
        self.DEFAULT_IMAGE = str(m['DEFAULT_IMAGE'] if 'DEFAULT_IMAGE' in m else "imagefiles/stLogo28.png")

        # Window settings
        w = self.data['window'] if 'window' in self.data else {}
        if isinstance(w, list):
            w = w[0]
        self.MESSAGE_X_POS = int(w['MESSAGE_X_POS'] if 'MESSAGE_X_POS' in w else 60)
        self.IMAGE_X_POS = int(w['IMAGE_X_POS'] if 'IMAGE_X_POS' in w else 21)
        self.WINDOW_WIDTH = int(w['WINDOW_WIDTH'] if 'WINDOW_WIDTH' in w else 400)
        self.WINDOW_HEIGHT = int(w['WINDOW_HEIGHT'] if 'WINDOW_HEIGHT' in w else 44)
        self.WINDOW_BG_COLOR = str(w['WINDOW_BG_COLOR'] if 'WINDOW_BG_COLOR' in w else "black")
        self.WINDOW_BG_IMAGE = str(w['WINDOW_BG_IMAGE'] if 'WINDOW_BG_IMAGE' in w else "imagefiles/background.png")
        self.BACKGROUND_X_POS = int(w['BACKGROUND_X_POS'] if 'BACKGROUND_X_POS' in w else 202)
        self.BACKGROUND_Y_POS = int(w['BACKGROUND_Y_POS'] if 'BACKGROUND_Y_POS' in w else 24)
        self.MOVE_ALL_ON_LINE_DELAY = float(w['MOVE_ALL_ON_LINE_DELAY'] if 'MOVE_ALL_ON_LINE_DELAY' in w else .004)
        print(self.MOVE_ALL_ON_LINE_DELAY)