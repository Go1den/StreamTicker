import random
from tkinter import Canvas

from objects.settings import Settings
from utils.helperMethods import pause

def selectDepartureAnimation(canvas: Canvas, settings: Settings, departure: str, height: int, scrollSpeed: float, width: int):
    if departure == "Slide Left":
        slideLeft(width, canvas, scrollSpeed)
    if departure == "Slide Right":
        slideRight(settings, canvas, scrollSpeed)
    if departure == "Slide Up":
        slideUp(height, settings, canvas, scrollSpeed)
    if departure == "Slide Down":
        slideDown(height, settings, canvas, scrollSpeed)
    if departure == "Zip Forward":
        zipForward(height, settings, canvas, scrollSpeed)
    if departure == "Zip Backward":
        zipBackward(height, settings, canvas, scrollSpeed)
    if departure == "Zip Randomly":
        zipRandomly(height, settings, canvas, scrollSpeed)

def pickDeparture() -> str:
    return random.choice(["Slide Right", "Slide Left", "Slide Up", "Slide Down", "Zip Forward", "Zip Backward", "Zip Randomly"])

def slideLeft(width: int, canvas: Canvas, scrollSpeed: float):
    for x in range(width):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, -1, 0)
        pause(scrollSpeed)

def slideRight(settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(int(settings.windowSettings.width)):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, 1, 0)
        pause(scrollSpeed)

def slideUp(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(height + int(int(settings.windowSettings.height) / 2)):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, 0, -1)
        pause(scrollSpeed)

def slideDown(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(height + int(int(settings.windowSettings.height) / 2)):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, 0, 1)
        pause(scrollSpeed)

def zipForward(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    for elem in canvas.find_withtag("currentMessage"):
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def zipBackward(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    if len(canvas.find_withtag("currentMessage")) % 2 == 0:
        deltaY = -1
    for elem in reversed(canvas.find_withtag("currentMessage")):
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def zipRandomly(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    elems = random.sample(list(canvas.find_withtag("currentMessage")), len(list(canvas.find_withtag("currentMessage"))))
    for elem in elems:
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1
