class APISettings:
    def __init__(self, challongeUsername: str="", challongeAPIKey: str="", smashggAPIKey: str=""):
        self.challongeUsername = challongeUsername
        self.challongeAPIKey = challongeAPIKey
        self.smashggAPIKey = smashggAPIKey

    def print(self):
        print("API Settings:")
        print("Challonge.com Username: " + self.challongeUsername)
        print("Challonge.com API Key: " + self.challongeAPIKey)
        print("Smash.gg API Key: " + self.smashggAPIKey)
