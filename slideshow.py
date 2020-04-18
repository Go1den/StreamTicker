import json
from os import path

from utils.graphics import GraphWin, Point, Image
from settings import Settings
from slide import Slide

class Slideshow:

    def __init__(self, data=None):
        self.settings = Settings(data)
        self.slides = self.getSlides()
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

    def getSlides(self):
        slides = []
        with open("messages.json") as f:
            data = json.loads(f.read())
            for slide in data['slides']:
                print(slide)
                slides.append(Slide(slide['image'] if path.exists(slide['image']) else self.settings.DEFAULT_IMAGE,
                                    slide['text'],
                                    slide['filePath'] if path.exists(slide['filePath']) else "",
                                    slide['prefixText'],
                                    slide['suffixText'],
                                    True if slide['isBitMessage'] == "True" else False,
                                    slide['nickname']))
        return slides
