from json import JSONEncoder

from objects.messagePart import MessagePart
from objects.override import Override

class Message:
    def __init__(self, nickname: str = "My New Message", sortOrder: int = 1, parts: list[MessagePart] = [], overrides: Override = Override()):
        self.nickname = nickname
        self.sortOrder = sortOrder
        self.parts = parts
        self.overrides = overrides

    def print(self):
        print("Message:")
        print("Nickname: " + self.nickname)
        print("Sort Order:" + str(self.sortOrder))
        print("Parts:")
        for part in self.parts:
            part.print()
        self.overrides.print()

    def sortParts(self):
        self.parts = sorted(self.parts, key=lambda x: x.sortOrder)

class MessageEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
