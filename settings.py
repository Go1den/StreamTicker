# This is the duration in seconds of each message
MESSAGE_DURATION = 5

# This is the duration in seconds of the pause between the previous message disappearing and the next message appearing
MESSAGE_INTERMISSION = .5

# This is the default color of the text. Plain color words are accepted.
MESSAGE_COLOR = 'white'

# Allows a modifier on the font, such as bold or italic.
MESSAGE_STYLE = 'bold'

# This is the name of the font. STRONG PREFERENCE FOR MONOSPACED FONTS. If it can't find the font you list here, it will attempt to use a (bad) default.
MESSAGE_FONT_FACE = 'PT Mono'

# This is the maximum number of characters in a message before it will attempt to shrink the font. If you set this too high, your messages could trail outside of the window
MAX_LENGTH_FOR_NORMAL_FONT_SIZE = 16

# This is the normal font size of a message
NORMAL_FONT_SIZE = 26

# This is the horizontal gap in pixels between each character for a message that uses NORMAL_FONT_SIZE
NORMAL_FONT_SIZE_GAP = 20

# Okay this is confusing to explain. This is the number of pixels to be subtracted from the usual gap between characters for a message that uses NORMAL_FONT_SIZE
# if the character is a space (e.g. " ").
# In other words, we don't want to waste a bunch of space in the window separating words. Set this to a higher number to move words closer together, or a lower number
# to move them farther apart.
NORMAL_FONT_SIZE_GAP_FOR_SPACES = 4

# This is the smaller font size used when a message exceeds the length of MAX_LENGTH_FOR_NORMAL_FONT_SIZE
SMALLER_FONT_SIZE = 22

# This is the horizontal gap in pixels between each character for a message that uses SMALLER_FONT_SIZE
SMALLER_FONT_SIZE_GAP = 16

# Okay this is confusing to explain. This is the number of pixels to be subtracted from the usual gap between characters for a message that uses SMALLER_FONT_SIZE
# if the character is a space (e.g. " ").
# In other words, we don't want to waste a bunch of space in the window separating words. Set this to a higher number to move words closer together, or a lower number
# to move them farther apart.
SMALLER_FONT_SIZE_GAP_FOR_SPACES = 6

# This is the X coordinate where the message will begin to be displayed in the window. Increase this to move messages to the right. Decrease to move them to the left.
MESSAGE_X_POS = 60

# Width of the window in pixels. For the program to work properly, it is highly recommended to use a multiple of 4.
WINDOW_WIDTH = 400

# Height of the window in pixels. For the program to work properly, it is highly recommended to use a multiple of 4.
WINDOW_HEIGHT = 44

# Default window background color. Plain color words are accepted.
WINDOW_BG_COLOR = 'black'

# This is the location of the background image. If no image is provided or the filepath is bad, the background color above will be used.
WINDOW_BG_IMAGE = "imagefiles/background.png"

# This is the delay in seconds between each move action. This simulates fluid movement of an object off the screen.
MOVE_ALL_ON_LINE_DELAY = .004

# Departure Settings
# All of these impact which methods of departure can be taken by a message leaving the window. Enable or disable them by setting them to True or False (Capitalization matters)
# Each departure method has an equal chance of being selected for any given message. Disable all the ones you don't like, or leave them all on for more variety.

ENABLE_DEPARTING_BY_SLIDING_RIGHT = True
ENABLE_DEPARTING_BY_SLIDING_LEFT = True
ENABLE_DEPARTING_BY_SLIDING_UP = True
ENABLE_DEPARTING_BY_SLIDING_DOWN = True
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT = True
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT = True
ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER = True
ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES = True
