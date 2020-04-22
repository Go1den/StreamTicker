import json

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

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
