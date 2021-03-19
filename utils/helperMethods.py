import json
import time

from objects.message import Message, MessageEncoder
from objects.settings import Settings, SettingsEncoder

def isFloat(value) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def readFile(path) -> str:
    try:
        f = open(path, "r")
        return f.read()
    except:
        return ""

def getFileNameFromPath(path) -> str:
    try:
        x = path.split('/')[-1]
        y = path.split('\\')[-1]
        return x if len(x) <= len(y) else y
    except:
        return path

def readJSON(path) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def writeJSON(path, data) -> bool:
    try:
        print(data)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            return True
    except:
        return False

def writeMessagesToJSON(path, messages: list[Message]) -> bool:
    try:
        with open(path, 'w') as f:
            json.dump(messages, f, indent=4, cls=MessageEncoder)
            return True
    except Exception as e:
        print(e)
        return False

def writeSettingsToJSON(path, settings: Settings) -> bool:
    try:
        with open(path, 'w') as f:
            json.dump(settings, f, indent=4, cls=SettingsEncoder)
            return True
    except Exception as e:
        print(e)
        return False

def getScrollSpeedFloat(speedString: str) -> float:
    if speedString == "Fastest":
        return float(0.001)
    if speedString == "Fast":
        return float(0.007)
    if speedString == "Normal":
        return float(0.013)
    if speedString == "Slow":
        return float(0.019)
    if speedString == "Slowest":
        return float(0.025)
    return float(0.013)

def pause(delay: float):
    t = time.time()
    while True:
        if t + delay <= time.time():
            break
