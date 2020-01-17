from src.departure import *
from src.graphics import *
from src.mover import moveAllOnLine, rollMessageIntoWindow
from src.settings import *
from src.slideConstants import MASTER_SLIDE_LIST
from src.slideshow import Slideshow

FLOOR_YPOS = math.ceil(WINDOW_HEIGHT * 1.5)
CEILING_YPOS = math.ceil(WINDOW_HEIGHT * -.5)

ENABLED_DEPARTURE_METHODS = getEnabledDepartureMethods()

def generateCharacterObjects(slideshow, characters, messageList):
    oddOrEven = False
    xPos = MESSAGE_X_POS
    for charac in characters:
        if oddOrEven:  # Spawn the next letter BELOW the window, so it will rise up
            yPos = FLOOR_YPOS
        else:  # Spawn the next letter ABOVE the window, so it will fall down
            yPos = CEILING_YPOS
        message = Text(Point(xPos, yPos), charac)
        message.setTextColor(MESSAGE_COLOR)
        message.setStyle(MESSAGE_STYLE)
        message.setFace(MESSAGE_FONT_FACE)
        message.setSize(SMALLER_FONT_SIZE) if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else message.setSize(NORMAL_FONT_SIZE)
        message.draw(slideshow.window)
        messageList.append(message)
        oddOrEven = not oddOrEven
        if charac == " ":
            xPos -= SMALLER_FONT_SIZE_GAP_FOR_SPACES if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else NORMAL_FONT_SIZE_GAP_FOR_SPACES
        xPos += SMALLER_FONT_SIZE_GAP if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else NORMAL_FONT_SIZE_GAP

def incrementIndex(idx, slideshow):
    idx += 1
    if idx >= len(slideshow.slides):
        idx = 0
    return idx

def main(slideshow):
    idx = 0
    repetitions = math.floor(WINDOW_HEIGHT / 4)
    while True:
        currentSlideImage = Image(Point(IMAGE_X_POS, FLOOR_YPOS), slideshow.slides[idx].image)
        currentSlideImage.draw(slideshow.window)
        moveAllOnLine([currentSlideImage], 0, -1, WINDOW_HEIGHT, MOVE_ALL_ON_LINE_DELAY)
        characters = list(slideshow.slides[idx].getMessageText())
        messageList = [currentSlideImage]
        generateCharacterObjects(slideshow, characters, messageList)
        rollMessageIntoWindow(messageList, repetitions)
        time.sleep(MESSAGE_DURATION)
        chooseDepartureMethodAndDepartFromWindow(messageList, repetitions, ENABLED_DEPARTURE_METHODS)
        slideshow.window.delete('all')
        slideshow.drawBackground()
        time.sleep(MESSAGE_INTERMISSION)
        idx = incrementIndex(idx, slideshow)

thisSlideshow = Slideshow(MASTER_SLIDE_LIST)
thisSlideshow.drawBackground()
main(thisSlideshow)
