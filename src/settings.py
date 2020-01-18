import configparser

WINDOWSETTINGS_FILE = "settings/windowSettings.txt"
MESSAGESETTINGS_FILE = "settings/messageSettings.txt"
DEPARTURE_SETTINGS_FILE = "settings/departureSettings.txt"

messageConfig = configparser.ConfigParser()
messageConfig.read(MESSAGESETTINGS_FILE)
messageSettings = messageConfig['MessageSettings']

MESSAGE_DURATION = int(messageSettings.get('MESSAGE_DURATION', 5))
MESSAGE_INTERMISSION = float(messageSettings.get('MESSAGE_INTERMISSION', .5))
MESSAGE_COLOR = str(messageSettings.get('MESSAGE_COLOR', 'white'))
MESSAGE_STYLE = str(messageSettings.get('MESSAGE_STYLE', 'bold'))
MESSAGE_FONT_FACE = str(messageSettings.get('MESSAGE_FONT_FACE', 'Courier New'))
MAX_LENGTH_FOR_NORMAL_FONT_SIZE = int(messageSettings.get('MAX_LENGTH_FOR_NORMAL_FONT_SIZE', 16))
NORMAL_FONT_SIZE = int(messageSettings.get('NORMAL_FONT_SIZE', 26))
NORMAL_FONT_SIZE_GAP = int(messageSettings.get('NORMAL_FONT_SIZE_GAP', 20))
NORMAL_FONT_SIZE_GAP_FOR_SPACES = int(messageSettings.get('NORMAL_FONT_SIZE_GAP_FOR_SPACES', 4))
SMALLER_FONT_SIZE = int(messageSettings.get('SMALLER_FONT_SIZE', 22))
SMALLER_FONT_SIZE_GAP = int(messageSettings.get('SMALLER_FONT_SIZE_GAP', 16))
SMALLER_FONT_SIZE_GAP_FOR_SPACES = int(messageSettings.get('SMALLER_FONT_SIZE_GAP_FOR_SPACES', 6))
DEFAULT_IMAGE = str(messageSettings.get('DEFAULT_IMAGE', 'imagefiles/stLogo28.png'))

windowConfig = configparser.ConfigParser()
windowConfig.read(WINDOWSETTINGS_FILE)
windowSettings = windowConfig['WindowSettings']

MESSAGE_X_POS = int(windowSettings.get('MESSAGE_X_POS', 60))
IMAGE_X_POS = int(windowSettings.get('IMAGE_X_POS', 21))
WINDOW_WIDTH = int(windowSettings.get('WINDOW_WIDTH', 400))
WINDOW_HEIGHT = int(windowSettings.get('WINDOW_HEIGHT', 44))
WINDOW_BG_COLOR = str(windowSettings.get('WINDOW_BG_COLOR', 'black'))
WINDOW_BG_IMAGE = str(windowSettings.get('WINDOW_BG_IMAGE', "imagefiles/background.png"))
BACKGROUND_X_POS = int(windowSettings.get('BACKGROUND_X_POS', 202))
BACKGROUND_Y_POS = int(windowSettings.get('BACKGROUND_Y_POS', 24))
MOVE_ALL_ON_LINE_DELAY = float(windowSettings.get('MOVE_ALL_ON_LINE_DELAY', .004))

departureConfig = configparser.ConfigParser()
departureConfig.read(DEPARTURE_SETTINGS_FILE)
departureSettings = departureConfig['DepartureSettings']

ENABLE_DEPARTING_BY_SLIDING_RIGHT = bool(departureSettings.get('ENABLE_DEPARTING_BY_SLIDING_RIGHT', True))
ENABLE_DEPARTING_BY_SLIDING_LEFT = bool(departureSettings.get('ENABLE_DEPARTING_BY_SLIDING_LEFT', True))
ENABLE_DEPARTING_BY_SLIDING_UP = bool(departureSettings.get('ENABLE_DEPARTING_BY_SLIDING_UP', True))
ENABLE_DEPARTING_BY_SLIDING_DOWN = bool(departureSettings.get('ENABLE_DEPARTING_BY_SLIDING_DOWN', True))
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = bool(departureSettings.get('ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT', True))
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = bool(departureSettings.get('ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT', True))
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = bool(departureSettings.get('ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER', True))
ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES = bool(departureSettings.get('ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES', True))
