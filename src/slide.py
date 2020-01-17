from src import bitutilities

class Slide:

    def __init__(self, image="", text="", filePath="", prefixText="", suffixText="", isBitMessage=False):
        self.image = image
        self.text = text
        self.filePath = filePath
        self.prefixText = prefixText
        self.suffixText = suffixText
        self.isBitMessage = isBitMessage
        if isBitMessage:
            self.getBitImage()

    def getMessageText(self):
        if self.filePath != "":
            return self.getTextWithFileInput()
        else:
            return self.getTextWithoutFileInput()

    def getTextWithoutFileInput(self):
        return self.prefixText + self.text + self.suffixText

    def getTextWithFileInput(self):
        try:
            with open(self.filePath) as f:
                contents = f.readline().rstrip().replace(':', ' -')
            return self.prefixText + self.text + contents + self.suffixText
        except:
            return self.getTextWithoutFileInput()

    def getBitImage(self):
        try:
            with open(self.filePath) as f:
                contents = f.readline().rstrip().replace(':', ' -')
            self.image = bitutilities.chooseBitIcon(int(contents.split(' ')[2]))
        except:
            self.image = ["bitimagefiles/bit10.png"]
