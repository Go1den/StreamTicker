import json
import sys

from departure import *
from graphics import *
from mover import moveAllOnLine, rollMessageIntoWindow
from slide import Slide
from slideshow import Slideshow

def getSlides():
    slides = []
    with open("messages.json") as f:
        data = json.loads(f.read())
        for slide in data['slides']:
            print(slide)
            slides.append(Slide(slide['image'],
                                slide['text'],
                                slide['filePath'],
                                slide['prefixText'],
                                slide['suffixText'],
                                True if slide['isBitMessage'] == "True" else False,
                                slide['nickname']))
    return slides

def generateCharacterObjects(slideshow, characters, messageList):
    oddOrEven = False
    xPos = slideshow.settings.MESSAGE_X_POS
    for charac in characters:
        if oddOrEven:  # Spawn the next letter BELOW the window, so it will rise up
            yPos = FLOOR_YPOS
        else:  # Spawn the next letter ABOVE the window, so it will fall down
            yPos = CEILING_YPOS
        message = Text(Point(xPos, yPos), charac)
        message.setTextColor(slideshow.settings.MESSAGE_COLOR)
        message.setStyle(slideshow.settings.MESSAGE_STYLE)
        message.setFace(slideshow.settings.MESSAGE_FONT_FACE)
        message.setSize(slideshow.settings.SMALLER_FONT_SIZE) if len(characters) > slideshow.settings.MAX_LENGTH_FOR_NORMAL_FONT_SIZE else message.setSize(
            slideshow.settings.NORMAL_FONT_SIZE)
        message.draw(slideshow.window)
        messageList.append(message)
        oddOrEven = not oddOrEven
        if charac == " ":
            xPos -= slideshow.settings.SMALLER_FONT_SIZE_GAP_FOR_SPACES if len(
                characters) > slideshow.settings.MAX_LENGTH_FOR_NORMAL_FONT_SIZE else slideshow.settings.NORMAL_FONT_SIZE_GAP_FOR_SPACES
        xPos += slideshow.settings.SMALLER_FONT_SIZE_GAP if len(characters) > slideshow.settings.MAX_LENGTH_FOR_NORMAL_FONT_SIZE else slideshow.settings.NORMAL_FONT_SIZE_GAP

def incrementIndex(idx, slideshow):
    idx += 1
    if idx >= len(slideshow.slides):
        idx = 0
    return idx

def main(slideshow):
    try:
        idx = 0
        repetitions = math.floor(slideshow.settings.WINDOW_HEIGHT / 4)
        while True:
            currentSlideImage = Image(Point(slideshow.settings.IMAGE_X_POS, FLOOR_YPOS), slideshow.slides[idx].image)
            currentSlideImage.draw(slideshow.window)
            moveAllOnLine([currentSlideImage], 0, -1, slideshow.settings.WINDOW_HEIGHT, slideshow.settings.MOVE_ALL_ON_LINE_DELAY)
            characters = list(slideshow.slides[idx].getMessageText())
            messageList = [currentSlideImage]
            generateCharacterObjects(slideshow, characters, messageList)
            rollMessageIntoWindow(slideshow.settings, messageList, repetitions)
            time.sleep(slideshow.settings.MESSAGE_DURATION)
            chooseDepartureMethodAndDepartFromWindow(slideshow.settings, messageList, repetitions, ENABLED_DEPARTURE_METHODS)
            slideshow.window.delete('all')
            slideshow.drawBackground()
            time.sleep(slideshow.settings.MESSAGE_INTERMISSION)
            idx = incrementIndex(idx, slideshow)
    except:
        sys.exit(1)

myShow = Slideshow(getSlides())
myShow.drawBackground()
FLOOR_YPOS = math.ceil(myShow.settings.WINDOW_HEIGHT * 1.5)
CEILING_YPOS = math.ceil(myShow.settings.WINDOW_HEIGHT * -.5)
ENABLED_DEPARTURE_METHODS = getEnabledDepartureMethods(myShow.settings)
main(myShow)
