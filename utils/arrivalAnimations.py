import random
from tkinter import Canvas, PhotoImage, W

from objects.message import Message
from objects.settings import Settings
from utils.helperMethods import readFile, pause

def selectArrivalAnimation(canvas: Canvas, settings: Settings, yCoord: int, yCoord2: int, arrival: str, height: int, scrollSpeed: float, width: int):
    if arrival == "Slide Left":
        slideLeft(settings, canvas, scrollSpeed)
    if arrival == "Slide Right":
        slideRight(width, canvas, scrollSpeed)
    if arrival == "Slide Up":
        slideUp(height, settings, canvas, scrollSpeed)
    if arrival == "Slide Down":
        slideDown(height, settings, canvas, scrollSpeed)
    if arrival == "Zip Forward":
        zipForward(height, settings, canvas, scrollSpeed)
    if arrival == "Zip Backward":
        zipBackward(height, settings, canvas, scrollSpeed)
    if arrival == "Zip Randomly":
        zipRandomly(yCoord, yCoord2, settings, canvas, scrollSpeed)

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
                # TODO add font style option instead of bold
                canvas.create_text(xCoord, yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="currentMessage", anchor=W)
                box = canvas.bbox(canvas.find_withtag("currentMessage")[-1])
                xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
        elif part.partType == "Text From File":
            fileText = readFile(part.value)
            for char in fileText:
                # TODO add font style option instead of bold
                canvas.create_text(xCoord, yCoord, fill=fontColor, text=char, font=(font, fontSize, "bold"), tags="currentMessage", anchor=W)
                box = canvas.bbox(canvas.find_withtag("currentMessage")[-1])
                xCoord = box[2] - 1  # TODO This -1 could be a message setting "gap between letters" or some such
        elif part.partType == "Image":
            try:
                img = PhotoImage(file=part.value)
                canvas.create_image(xCoord, yCoord, image=img, anchor=W, tags="currentMessage")
                box = canvas.bbox(canvas.find_withtag("currentMessage")[-1])
                xCoord = box[2] - 1
            except Exception as e:
                print("Error loading image: " + str(e))
    width = box[2]
    height = 0
    for elem in canvas.find_withtag("currentMessage"):
        box = canvas.bbox(elem)
        height = max(height, box[3] - box[1])
    canvas.delete("all")
    return width, height

def pickArrival() -> str:
    return random.choice(["Slide Right", "Slide Left", "Slide Up", "Slide Down", "Zip Forward", "Zip Backward", "Zip Randomly"])

def getStartingXYCoordinates(width: int, height: int, arrival: str, settings: Settings) -> (int, int):
    xCoord = 0
    yCoord = int(int(settings.windowSettings.height) / 2)
    yCoord2 = 0
    if arrival == "Slide Left":
        xCoord = int(settings.windowSettings.width) + 1
    if arrival == "Slide Right":
        xCoord = -1 * width
    if arrival == "Slide Up":
        yCoord = height + int(settings.windowSettings.height)
    if arrival == "Slide Down":
        yCoord = -1 * height
    if arrival == "Zip Forward" or arrival == "Zip Backward" or arrival == "Zip Randomly":
        yCoord = -1 * height
        yCoord2 = height + int(settings.windowSettings.height)
    return xCoord, yCoord, yCoord2

def slideLeft(settings: Settings, canvas: Canvas, scrollSpeed: float):
    for x in range(int(settings.windowSettings.width)):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, -1, 0)
        pause(scrollSpeed)

def slideRight(width: int, canvas: Canvas, scrollSpeed: float):
    for x in range(width):
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
        while int((canvas.bbox(elem)[3] + canvas.bbox(elem)[1]) / 2) != int(int(settings.windowSettings.height)/2):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def zipBackward(height: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    if len(canvas.find_withtag("currentMessage")) % 2 == 0:
        deltaY = -1
    for elem in reversed(canvas.find_withtag("currentMessage")):
        while int((canvas.bbox(elem)[3] + canvas.bbox(elem)[1]) / 2) != int(int(settings.windowSettings.height)/2):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1

def zipRandomly(yCoord: int, yCoord2: int, settings: Settings, canvas: Canvas, scrollSpeed: float):
    deltaY = 1
    elems = random.sample(list(canvas.find_withtag("currentMessage")), len(list(canvas.find_withtag("currentMessage"))))
    for elem in elems:
        if deltaY == 1:
            canvas.moveto(elem, canvas.bbox(elem)[0], yCoord)
        else:
            canvas.moveto(elem, canvas.bbox(elem)[0], yCoord2)
        while int((canvas.bbox(elem)[3] + canvas.bbox(elem)[1]) / 2) != int(int(settings.windowSettings.height)/2):
            canvas.move(elem, 0, deltaY)
            pause(scrollSpeed)
        deltaY = deltaY * -1
