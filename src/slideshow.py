from src.graphics import GraphWin, Point, Image
from src.settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_BG_COLOR, WINDOW_BG_IMAGE, BACKGROUND_X_POS, BACKGROUND_Y_POS

def createWindow():
    win = GraphWin('StreamTicker by Go1den', WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground(WINDOW_BG_COLOR)
    return win

def drawBackground(window):
    try:
        backgroundImage = Image(Point(BACKGROUND_X_POS, BACKGROUND_Y_POS), WINDOW_BG_IMAGE)
        backgroundImage.draw(window)
    except:
        print("Unable to load background image.")

class Slideshow:

    def __init__(self, slides=None):
        self.slides = slides
        self.window = createWindow()

    def drawBackground(self):
        drawBackground(self.window)
