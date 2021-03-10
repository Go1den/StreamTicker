class MessagePart:
    def __init__(self, partType: str, sortOrder: int, value: str):
        self.partType = partType
        self.sortOrder = sortOrder
        self.value = value

    def print(self):
        print("Part:")
        print("Part Type: " + self.partType)
        print("Sort Order: " + str(self.sortOrder))
        print("Value: " + self.value)
