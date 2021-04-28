class WindowSettings:
    def __init__(self, moveAllOnLineDelay="99", bgImage="imagefiles/background.png", width="400", height="44", bgColor="#000000", shuffle: bool = False):
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
