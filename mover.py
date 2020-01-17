import math
import time

from settings import WINDOW_HEIGHT, MOVE_ALL_ON_LINE_DELAY

def moveAll(shapeList, dx, dy):
    """ Move all shapes in shapeList by (dx, dy)."""
    for shape in shapeList:
        shape.move(dx, dy)

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    """Animate the shapes in shapeList along a line.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    """
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

def rollMessageIntoWindow(messageList, repetitions):
    for m in messageList[1:]:
        if m.getAnchor().getY() == math.ceil(WINDOW_HEIGHT * 1.5):
            moveAllOnLine([m], 0, -4, repetitions, MOVE_ALL_ON_LINE_DELAY)
        else:
            moveAllOnLine([m], 0, 4, repetitions, MOVE_ALL_ON_LINE_DELAY)
