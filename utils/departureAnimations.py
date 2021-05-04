from random import sample, choice
from tkinter import Canvas

from objects.settings import Settings
from utils.animations import moveAllCanvasElements
from utils.helperMethods import pause

def selectDepartureAnimation(canvas: Canvas, settings: Settings, departure: str, height: int, scrollSpeed: float, width: int, alignment: str):
    if departure == "Slide Left":
        slideLeft(settings, width, canvas, scrollSpeed, alignment)
    if departure == "Slide Right":
        slideRight(settings, width, canvas, scrollSpeed, alignment)
    if departure == "Slide Up":
        slideUp(height, settings, canvas, scrollSpeed)
    if departure == "Slide Down":
        slideDown(height, settings, canvas, scrollSpeed)
    if departure == "Unzip Forward":
        unzipForward(height, settings, canvas, scrollSpeed)
    if departure == "Unzip Backward":
        unzipBackward(height, settings, canvas, scrollSpeed)
    if departure == "Unzip Randomly":
        unzipRandomly(height, settings, canvas, scrollSpeed)

def pickDeparture(italic: str) -> str:
    if italic == "italic":
        return choice(["Slide Right", "Slide Left", "Slide Up", "Slide Down"])
    return choice(["Slide Right", "Slide Left", "Slide Up", "Slide Down", "Unzip Forward", "Unzip Backward", "Unzip Randomly"])

def slideLeft(settings: Settings, width: int, canvas: Canvas, scrollSpeed: float, alignment: str):
    delta = 0
    if alignment == "Left":
        delta = width
    elif alignment == "Right":
        delta = int(settings.windowSettings.width)
    elif alignment == "Center":
        center = int(int(settings.windowSettings.width) / 2)
        delta = center + int(width / 2)
    moveAllCanvasElements(delta, canvas, -1, 0, scrollSpeed)

def slideRight(settings: Settings, width: int, canvas: Canvas, scrollSpeed: float, alignment: str):
    delta = 0
    if alignment == "Left":
        delta = int(settings.windowSettings.width)
    elif alignment == "Right":
        delta = width
    elif alignment == "Center":
        center = int(int(settings.windowSettings.width) / 2)
        delta = center + int(width / 2)
    moveAllCanvasElements(delta, canvas, 1, 0, scrollSpeed)

def slideUp(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    delta = height + int(int(settings.windowSettings.height) / 2)
    moveAllCanvasElements(delta, canvas, 0, -1, scrollSpeed)

def slideDown(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    delta = height + int(int(settings.windowSettings.height) / 2)
    moveAllCanvasElements(delta, canvas, 0, 1, scrollSpeed)

def unzipForward(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    for elem in canvas.find_withtag("currentMessage"):
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def unzipBackward(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    if len(canvas.find_withtag("currentMessage")) % 2 == 0:
        deltaY = -1
    for elem in reversed(canvas.find_withtag("currentMessage")):
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def unzipRandomly(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    elems = sample(list(canvas.find_withtag("currentMessage")), len(list(canvas.find_withtag("currentMessage"))))
    for elem in elems:
        for x in range(height + int(int(settings.windowSettings.height) / 2)):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1
