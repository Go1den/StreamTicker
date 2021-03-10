from json import JSONEncoder

from objects.messageSettings import MessageSettings
from objects.windowSettings import WindowSettings

class Settings:
    def __init__(self, windowSettings=WindowSettings(), messageSettings=MessageSettings()):
        self.windowSettings = windowSettings
        self.messageSettings = messageSettings

    def print(self):
        self.windowSettings.print()
        self.messageSettings.print()

class SettingsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
