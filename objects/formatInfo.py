class FormatInfo:
    def __init__(self, hasGroupStages: bool = False, holdThirdPlaceMatch: bool = False, challongeURL: str = "", swissRounds: int = 0, type: str = ""):
        self.hasGroupStages = hasGroupStages
        self.holdThirdPlaceMatch = holdThirdPlaceMatch
        self.challongeURL = challongeURL
        self.swissRounds = swissRounds
        self.type = type

    def print(self):
        print("Group stages: " + str(self.hasGroupStages))
        print("Third place match: " + str(self.holdThirdPlaceMatch))
        print("Tournament URL: " + str(self.challongeURL))
        print("Swiss rounds: " + str(self.swissRounds))
        print("Type: " + str(self.type))
