class MessageSettings:
    def __init__(self, style="", color="#ffffff", fontFace="Courier New", intermission=".5", fontSize="26", duration="10", arrival="Pick For Me", departure="Pick For Me"):
        self.style = style
        self.color = color
        self.fontFace = fontFace
        self.intermission = intermission
        self.fontSize = fontSize
        self.duration = duration
        self.arrival = arrival
        self.departure = departure

    def print(self):
        print("Message Settings:")
        print("Style: " + self.style)
        print("Color: " + self.color)
        print("Font Face: " + self.fontFace)
        print("Intermission: " + self.intermission)
        print("Font Size: " + self.fontSize)
        print("Duration: " + self.duration)
        print("Arrival: " + self.arrival)
        print("Departure: " + self.departure)
