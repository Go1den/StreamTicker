import math
import random
import time

from graphics import Rectangle, Point
from mover import moveAllOnLine
from settings import MOVE_ALL_ON_LINE_DELAY, WINDOW_BG_COLOR, WINDOW_WIDTH, WINDOW_HEIGHT, ENABLE_DEPARTING_BY_SLIDING_RIGHT, ENABLE_DEPARTING_BY_SLIDING_DOWN, \
    ENABLE_DEPARTING_BY_SLIDING_LEFT, ENABLE_DEPARTING_BY_SLIDING_UP, ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT, \
    ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT, ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER, ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES

def getEnabledDepartureMethods():
    enabledMethods = []
    if ENABLE_DEPARTING_BY_SLIDING_RIGHT:
        enabledMethods.append(0)
    if ENABLE_DEPARTING_BY_SLIDING_DOWN:
        enabledMethods.append(1)
    if ENABLE_DEPARTING_BY_SLIDING_LEFT:
        enabledMethods.append(2)
    if ENABLE_DEPARTING_BY_SLIDING_UP:
        enabledMethods.append(3)
    if ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_RIGHT_TO_LEFT:
        enabledMethods.append(4)
    if ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_WORKING_LEFT_TO_RIGHT:
        enabledMethods.append(5)
    if ENABLE_DEPARTING_BY_ALTERNATING_UP_AND_DOWN_IN_RANDOM_ORDER:
        enabledMethods.append(6)
    if ENABLE_DEPARTING_BY_COVERING_WITH_RECTANGLES:
        enabledMethods.append(7)
    return enabledMethods

def chooseDepartureMethodAndDepartFromWindow(messageList, repetitions, enabledMethods):
    directionToLeave = 4
    methodOfDeparture = random.choice(enabledMethods)
    if methodOfDeparture == 0:
        departBySlidingRight(messageList, directionToLeave)
    if methodOfDeparture == 1:
        departBySlidingDown(messageList, repetitions, directionToLeave)
    if methodOfDeparture == 2:
        departBySlidingLeft(messageList, directionToLeave)
    if methodOfDeparture == 3:
        departBySlidingUp(messageList, repetitions, directionToLeave)
    if methodOfDeparture == 4:
        departAlternatingUpAndDownWorkingRightToLeft(messageList, repetitions, directionToLeave)
    if methodOfDeparture == 5:
        departAlternatingUpAndDownWorkingLeftToRight(messageList, repetitions, directionToLeave)
    if methodOfDeparture == 6:
        departAlternatingUpAndDownRandomlyChoosingCharacters(messageList, repetitions, directionToLeave)
    # if methodOfDeparture == 7:
    #     departByCoveringWithRectangles(slideshow)

def departAlternatingUpAndDownWorkingRightToLeft(messageList, repetitions, directionToLeave):
    messageList.reverse()
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, MOVE_ALL_ON_LINE_DELAY)

def departAlternatingUpAndDownWorkingLeftToRight(messageList, repetitions, directionToLeave):
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, MOVE_ALL_ON_LINE_DELAY)

def departAlternatingUpAndDownRandomlyChoosingCharacters(messageList, repetitions, directionToLeave):
    random.shuffle(messageList)
    for msg in messageList:
        directionToLeave = directionToLeave * -1
        moveAllOnLine([msg], 0, directionToLeave, repetitions, MOVE_ALL_ON_LINE_DELAY)

def departBySlidingDown(messageList, repetitions, directionToLeave):
    moveAllOnLine(messageList, 0, directionToLeave, repetitions, MOVE_ALL_ON_LINE_DELAY)

def departBySlidingUp(messageList, repetitions, directionToLeave):
    moveAllOnLine(messageList, 0, directionToLeave * -1, repetitions, MOVE_ALL_ON_LINE_DELAY)

def departBySlidingRight(messageList, directionToLeave):
    moveAllOnLine(messageList, directionToLeave, 0, math.ceil(WINDOW_WIDTH / 4), MOVE_ALL_ON_LINE_DELAY)

def departBySlidingLeft(messageList, directionToLeave):
    moveAllOnLine(messageList, directionToLeave * -1, 0, math.ceil(WINDOW_WIDTH / 4), MOVE_ALL_ON_LINE_DELAY)

def departByCoveringWithRectangles(slideshow):  # TODO: Implement later when I figure this out
    recList = []
    for yCoordRange in range(0, WINDOW_HEIGHT + 4, 4):
        recList.append(Rectangle(Point(0, yCoordRange), Point(WINDOW_WIDTH, yCoordRange + 4)))
    random.shuffle(recList)
    for rec in recList:
        rec.setFill(WINDOW_BG_COLOR)
        rec.draw(slideshow.window)
        time.sleep(.05)
