import math
import random
import time

from src.graphics import Rectangle, Point
from src.mover import moveAllOnLine

def getEnabledDepartureMethods(settings):
    enabledMethods = []
    if settings.ENABLE_DEPARTING_BY_SLIDING_RIGHT:
        enabledMethods.append(0)
    if settings.ENABLE_DEPARTING_BY_SLIDING_DOWN:
        enabledMethods.append(1)
    if settings.ENABLE_DEPARTING_BY_SLIDING_LEFT:
        enabledMethods.append(2)
    if settings.ENABLE_DEPARTING_BY_SLIDING_UP:
        enabledMethods.append(3)
    if settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT:
        enabledMethods.append(4)
    if settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT:
        enabledMethods.append(5)
    if settings.ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER:
        enabledMethods.append(6)
    if settings.ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES:
        enabledMethods.append(7)
    return enabledMethods

def chooseDepartureMethodAndDepartFromWindow(settings, messageList, repetitions, enabledMethods):
    directionToLeave = 4
    methodOfDeparture = random.choice(enabledMethods)
    if methodOfDeparture == 0:
        departBySlidingRight(settings, messageList, directionToLeave)
    if methodOfDeparture == 1:
        departBySlidingDown(settings, messageList, repetitions, directionToLeave)
    if methodOfDeparture == 2:
        departBySlidingLeft(settings, messageList, directionToLeave)
    if methodOfDeparture == 3:
        departBySlidingUp(settings, messageList, repetitions, directionToLeave)
    if methodOfDeparture == 4:
        departAlternatingUpAndDownWorkingRightToLeft(settings, messageList, repetitions, directionToLeave)
    if methodOfDeparture == 5:
        departAlternatingUpAndDownWorkingLeftToRight(settings, messageList, repetitions, directionToLeave)
    if methodOfDeparture == 6:
        departAlternatingUpAndDownRandomlyChoosingCharacters(settings, messageList, repetitions, directionToLeave)
    # if methodOfDeparture == 7:
    #     departByCoveringWithRectangles(slideshow)

def departAlternatingUpAndDownWorkingRightToLeft(settings, messageList, repetitions, directionToLeave):
    messageList.reverse()
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, settings.MOVE_ALL_ON_LINE_DELAY)

def departAlternatingUpAndDownWorkingLeftToRight(settings, messageList, repetitions, directionToLeave):
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, settings.MOVE_ALL_ON_LINE_DELAY)

def departAlternatingUpAndDownRandomlyChoosingCharacters(settings, messageList, repetitions, directionToLeave):
    random.shuffle(messageList)
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, settings.MOVE_ALL_ON_LINE_DELAY)

def departBySlidingDown(settings, messageList, repetitions, directionToLeave):
    moveAllOnLine(messageList, 0, directionToLeave, repetitions, settings.MOVE_ALL_ON_LINE_DELAY)

def departBySlidingUp(settings, messageList, repetitions, directionToLeave):
    moveAllOnLine(messageList, 0, directionToLeave * -1, repetitions, settings.MOVE_ALL_ON_LINE_DELAY)

def departBySlidingRight(settings, messageList, directionToLeave):
    moveAllOnLine(messageList, directionToLeave, 0, math.ceil(settings.WINDOW_WIDTH / 4), settings.MOVE_ALL_ON_LINE_DELAY)

def departBySlidingLeft(settings, messageList, directionToLeave):
    moveAllOnLine(messageList, directionToLeave * -1, 0, math.ceil(settings.WINDOW_WIDTH / 4), settings.MOVE_ALL_ON_LINE_DELAY)

def departByCoveringWithRectangles(settings, slideshow):  # TODO: Implement later when I figure this out
    recList = []
    for yCoordRange in range(0, settings.WINDOW_HEIGHT + 4, 4):
        recList.append(Rectangle(Point(0, yCoordRange), Point(settings.WINDOW_WIDTH, yCoordRange + 4)))
    random.shuffle(recList)
    for rec in recList:
        rec.setFill(settings.WINDOW_BG_COLOR)
        rec.draw(slideshow.window)
        time.sleep(.05)
