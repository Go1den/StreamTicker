import random

from graphics import *
from mover import moveAllOnLine
from settings import *
from slideConstants import MASTER_SLIDE_LIST
from slideshow import Slideshow

def drawBackground(window):
    try:
        backgroundImage = Image(Point(202, 24), WINDOW_BG_IMAGE)
        backgroundImage.draw(window)
    except:
        print("Unable to load background image.")

def main(slideshow):
    methodOfDeparture = 0
    idx = 0
    while True:
        currentSlideImage = Image(Point(24, 66), slideshow.slides[idx].image)
        currentSlideImage.draw(win)
        moveAllOnLine([currentSlideImage], 0, -1, 44, MOVE_ALL_ON_LINE_DELAY)
        characters = list(slideshow.slides[idx].getMessageText())
        messageList = [currentSlideImage]
        oddOrEven = False
        xPos = 40
        for charac in characters:
            xPos += 16 if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else 20
            if oddOrEven:
                yPos = 66
            else:
                yPos = -22
            message = Text(Point(xPos, yPos), charac)
            message.setTextColor(MESSAGE_COLOR)
            message.setStyle(MESSAGE_STYLE)
            message.setFace(MESSAGE_FONT_FACE)
            message.setSize(SMALLER_FONT_SIZE) if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else message.setSize(NORMAL_FONT_SIZE)
            message.draw(win)
            oddOrEven = not oddOrEven
            messageList.append(message)
            if charac == " ":
                xPos -= 6 if len(characters) > MAX_LENGTH_FOR_NORMAL_FONT_SIZE else 4
        for m in messageList[1:]:
            if m.getAnchor().getY() == 66:
                moveAllOnLine([m], 0, -4, 11, MOVE_ALL_ON_LINE_DELAY)
            else:
                moveAllOnLine([m], 0, 4, 11, MOVE_ALL_ON_LINE_DELAY)
        time.sleep(MESSAGE_DURATION)
        directionToLeave = 4
        if methodOfDeparture == 0:
            messageList.reverse()
        if methodOfDeparture == 1 or methodOfDeparture == 2:
            random.shuffle(messageList)
        # if methodOfDeparture == 2:
        #     recList = []
        #     for yCoordRange in range(0, 48, 4):
        #         recList.append(Rectangle(Point(0, yCoordRange), Point(400, yCoordRange + 4)))
        #     random.shuffle(recList)
        #     for rec in recList:
        #         rec.setFill(WINDOW_BG_COLOR)
        #         rec.draw(win)
        #         time.sleep(.05)
        if methodOfDeparture == 3:
            if random.random() > 0.5:
                directionToLeave = directionToLeave * -1
            if random.random() > 0.5:
                moveAllOnLine(messageList, 0, directionToLeave, 11, MOVE_ALL_ON_LINE_DELAY)
            else:
                moveAllOnLine(messageList, directionToLeave, 0, 100, MOVE_ALL_ON_LINE_DELAY)
        elif methodOfDeparture < 3:
            for x in messageList:
                directionToLeave = directionToLeave * -1
                moveAllOnLine([x], 0, directionToLeave, 11, MOVE_ALL_ON_LINE_DELAY)
        win.delete('all')
        drawBackground(win)
        methodOfDeparture = (methodOfDeparture + 1) % 4
        time.sleep(MESSAGE_INTERMISSION)
        idx += 1
        if idx >= len(slideshow.slides):
            idx = 0

thisSlideshow = Slideshow(MASTER_SLIDE_LIST)
win = GraphWin('StreamTicker by Go1den', WINDOW_WIDTH, WINDOW_HEIGHT)
win.setBackground(WINDOW_BG_COLOR)
drawBackground(win)
main(thisSlideshow)
