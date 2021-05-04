class WindowSettings:
    def __init__(self, moveAllOnLineDelay: str = "99", bgImage: str = "imagefiles/background.png", width: str = "400", height: str = "44", bgColor: str = "#000000",
                 shuffle: bool = False):
        self.moveAllOnLineDelay = moveAllOnLineDelay
        self.bgImage = bgImage
        self.width = width
        self.height = height
        self.bgColor = bgColor
        self.shuffle = shuffle

    def print(self):
        print("Window Settings:")
        print("Move all on line delay: " + self.moveAllOnLineDelay)
        print("Background image: " + self.bgImage)
        print("Width: " + self.width)
        print("Height: " + self.height)
        print("Background Color: " + self.bgColor)
        print("Shuffle: " + str(self.shuffle))
