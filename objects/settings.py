from json import JSONEncoder

from objects.messageSettings import MessageSettings
from objects.windowSettings import WindowSettings

class Settings:
    def __init__(self, windowSettings=WindowSettings(), messageSettings=MessageSettings(), defaultTemplate=None):
        self.windowSettings = windowSettings
        self.messageSettings = messageSettings
        if defaultTemplate is None:
            self.defaultTemplate = {"parts": [{"partType": "Streamed Text Line From File", "sortOrder": 1, "value": ""}], "overrides": {}}
        else:
            self.defaultTemplate = defaultTemplate

    def print(self):
        self.windowSettings.print()
        self.messageSettings.print()
        print(self.defaultTemplate)

class SettingsEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
