from tkinter import Canvas, W, PhotoImage, NW

from utils.pause import pause
from windows.streamTickerWindow import StreamTickerWindow

streamTickerWindow = StreamTickerWindow()

canvas = Canvas(streamTickerWindow, width=400, height=44, bd=0, highlightthickness=0, background="#000000")
canvas.bind('<Button-3>', streamTickerWindow.rightClickMenu)

img = PhotoImage(file="testBG.png")
canvas.create_image(0, 0, anchor=NW, image=img)

testString = "This is a test"
x = 4
y = 22
for char in testString:
    canvas.create_text(x, y, fill="white", text=char, font=("Motion Control", "20", "bold"), tags="text", anchor=W)
    box = canvas.bbox(canvas.find_withtag("text")[-1])
    x = box[2] - 1

# canvas.create_text(4, 22, fill="yellow", text="This is a test", font=("Motion Control", "20", "bold"), tags="text", anchor=W)

canvas.grid(row=0, column=0)

def moveAllLetters():
    for x in range(10):
        for text in canvas.find_withtag("text"):
            canvas.move(text, 0, 1)
        streamTickerWindow.update()
        pause(0.03)

streamTickerWindow.after(2000, moveAllLetters)
streamTickerWindow.mainloop()

# print (canvas.find_withtag("all")) FINDS ALL ELEMENTS CURRENTLY ON THE CANVAS

# for t in canvas.find_withtag("all"):
#     print(canvas.bbox(t))

# print(canvas.bbox(canvas.find_withtag("all")[0])) #Prints the bounding box coordinates of the first element in the canvas
# print (canvas.find_withtag("tagName")) FINDS ALL ELEMENTS WITH tags="tagName", can have multiple tags per element
