import json

from objects.message import Message, MessageEncoder
from objects.settings import Settings, SettingsEncoder

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def readFile(path):
    try:
        f = open(path, "r")
        return f.read()
    except:
        return ""

def getFileNameFromPath(path):
    try:
        x = path.split('/')[-1]
        y = path.split('\\')[-1]
        return x if len(x) <= len(y) else y
    except:
        return path

def readJSON(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def writeJSON(path, data):
    try:
        print(data)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            return True
    except:
        return False

def writeMessagesToJSON(path, messages: list[Message]):
    try:
        with open(path, 'w') as f:
            json.dump(messages, f, indent=4, cls=MessageEncoder)
            return True
    except Exception as e:
        print(e)
        return False

def writeSettingsToJSON(path, settings: Settings):
    try:
        with open(path, 'w') as f:
            json.dump(settings, f, indent=4, cls=SettingsEncoder)
            return True
    except Exception as e:
        print(e)
        return False
