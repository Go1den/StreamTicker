from json import JSONEncoder

from objects.apiSettings import APISettings
from objects.messageSettings import MessageSettings
from objects.windowSettings import WindowSettings

class Settings:
    def __init__(self, windowSettings=WindowSettings(), messageSettings=MessageSettings(), apiSettings=APISettings()):
        self.windowSettings = windowSettings
        self.messageSettings = messageSettings
        self.apiSettings = apiSettings

    def print(self):
        self.windowSettings.print()
        self.messageSettings.print()
        self.apiSettings.print()

class SettingsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
