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