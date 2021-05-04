from tkinter import Canvas

from utils.helperMethods import pause

def moveAllCanvasElements(delta: int, canvas: Canvas, deltaX: int, deltaY: int, scrollSpeed: float):
    for x in range(delta):
        for elem in canvas.find_withtag("currentMessage"):
            canvas.move(elem, deltaX, deltaY)
        pause(scrollSpeed)
