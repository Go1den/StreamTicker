class WindowSettings:
    def __init__(self, moveAllOnLineDelay="Fast", bgImage="imagefiles/background.png", width="400", height="44", bgColor="#000000"):
        self.moveAllOnLineDelay = moveAllOnLineDelay
        self.bgImage = bgImage
        self.width = width
        self.height = height
        self.bgColor = bgColor

    def print(self):
        print("Window Settings:")
        print("Move all on line delay: " + self.moveAllOnLineDelay)
        print("Background image: " + self.bgImage)
        print("Width: " + self.width)
        print("Height: " + self.height)
        print("Background Color: " + self.bgColor)
