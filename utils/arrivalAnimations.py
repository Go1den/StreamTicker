import random
from tkinter import Canvas, PhotoImage, W

from objects.message import Message
from objects.settings import Settings
from utils.helperMethods import readFile, pause

def getWidthAndHeight(currentMessage: Message, settings: Settings) -> (int, int):
    font = currentMessage.overrides.font if currentMessage.overrides.font else settings.messageSettings.fontFace
    fontSize = currentMessage.overrides.fontSize if currentMessage.overrides.fontSize else settings.messageSettings.fontSize
    fontColor = currentMessage.overrides.fontColor if currentMessage.overrides.fontColor else settings.messageSettings.color
    xCoord = 0
    yCoord = 0
    canvas = Canvas()
    box = (0, 0, 0, 0)
    for part in sorted(currentMessage.parts, key=lambda x: x.sortOrder):
        if part.partType == "Pixel Gap":
            xCoord += int(part.value)
        elif part.partType == "Text":
            for char in part.value:
                # TODO replace this hard coded Y coordinate, and add font style option instead of bold
                canvas.create_text(xCoord, yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="text", anchor=W)
                box = canvas.bbox(canvas.find_withtag("text")[-1])
                xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
        elif part.partType == "Text From File":
            fileText = readFile(part.value)
            for char in fileText:
                # TODO replace this hard coded Y coordinate, and add font style option instead of bold
                canvas.create_text(xCoord, yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="text", anchor=W)
                box = canvas.bbox(canvas.find_withtag("text")[-1])
                xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
        elif part.partType == "Image":
            try:
                img = PhotoImage(file=part.value)
                canvas.create_image(xCoord, yCoord, image=img, anchor=W, tags="image")
                box = canvas.bbox(canvas.find_withtag("image")[-1])
                xCoord = box[2] - 1
            except Exception as e:
                print("Error loading image: " + str(e))
    width = box[2]
    height = 0
    for elem in canvas.find_withtag("text"):
        box = canvas.bbox(elem)
        height = max(height, box[3] - box[1])
    for elem in canvas.find_withtag("image"):
        box = canvas.bbox(elem)
        height = max(height, box[3] - box[1])
    canvas.delete("all")
    return width, height

def pickArrival() -> str:
    return random.choice(["Pick For Me", "Slide Right", "Slide Left", "Slide Up", "Slide Down", "Zip Forward", "Zip Backward", "Zip Randomly"])

def getStartingXYCoordinates(width: int, height: int, currentMessage: Message, arrival: str, settings: Settings) -> (int, int):
    xCoord = 0
    yCoord = int(int(settings.windowSettings.height) / 2)
    if arrival == "Slide Left":
        xCoord = int(settings.windowSettings.width) + 1
    if arrival == "Slide Right":
        xCoord = -1 * width
    if arrival == "Slide Up":
        yCoord = height + int(settings.windowSettings.height)
    if arrival == "Slide Down":
        yCoord = -1 * height
    return xCoord, yCoord

def slideLeft(settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(int(settings.windowSettings.width)):
        for elem in canvas.find_withtag("text") + canvas.find_withtag("image"):
            canvas.move(elem, -1, 0)
        pause(scrollSpeed)

def slideRight(width: int, canvas: Canvas, scrollSpeed: float):
    for x in range(width):
        for elem in canvas.find_withtag("text") + canvas.find_withtag("image"):
            canvas.move(elem, 1, 0)
        pause(scrollSpeed)

def slideUp(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(height + int(int(settings.windowSettings.height) / 2)):
        for elem in canvas.find_withtag("text") + canvas.find_withtag("image"):
            canvas.move(elem, 0, -1)
        pause(scrollSpeed)

def slideDown(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(height + int(int(settings.windowSettings.height) / 2)):
        for elem in canvas.find_withtag("text") + canvas.find_withtag("image"):
            canvas.move(elem, 0, 1)
        pause(scrollSpeed)