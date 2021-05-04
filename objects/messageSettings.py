class MessageSettings:
    def __init__(self, color: str = "#ffffff", fontFace: str = "Courier New", intermission: str = ".5", fontSize: str = "26", duration: str = "10",
                 arrival: str = "Pick For Me", departure: str = "Pick For Me", bold: bool = False, italic: bool = False, overstrike: bool = False,
                 alignment: str = "Left"):
        self.color = color
        self.fontFace = fontFace
        self.intermission = intermission
        self.fontSize = fontSize
        self.duration = duration
        self.arrival = arrival
        self.departure = departure
        self.bold = bold
        self.italic = italic
        self.overstrike = overstrike
        self.alignment = alignment

    def print(self):
        print("Message Settings:")
        print("Color: " + self.color)
        print("Font Face: " + self.fontFace)
        print("Intermission: " + self.intermission)
        print("Font Size: " + self.fontSize)
        print("Duration: " + self.duration)
        print("Arrival: " + self.arrival)
        print("Departure: " + self.departure)
        print("Bold: " + str(self.bold))
        print("Italic: " + str(self.italic))
        print("Overstrike: " + str(self.overstrike))
        print("Alignment: " + self.alignment)
