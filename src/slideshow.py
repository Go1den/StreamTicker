from src.graphics import GraphWin, Point, Image
from src.settings import Settings

class Slideshow:

    def __init__(self, slides=None):
        self.settings = Settings()
        self.slides = slides
        self.window = self.createWindow()

    def drawBackground(self):
        try:
            backgroundImage = Image(Point(self.settings.BACKGROUND_X_POS, self.settings.BACKGROUND_Y_POS), self.settings.WINDOW_BG_IMAGE)
            backgroundImage.draw(self.window)
        except:
            print("Unable to load background image.")

    def createWindow(self):
        win = GraphWin('StreamTicker by Go1den', self.settings.WINDOW_WIDTH, self.settings.WINDOW_HEIGHT)
        win.setBackground(self.settings.WINDOW_BG_COLOR)
        return win
