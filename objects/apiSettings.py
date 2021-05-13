class APISettings:
    def __init__(self, challongeUsername: str="", challongeAPIKey: str="", smashggAPIKey: str="", templatePath: str="templates/tournamentTemplate.stt"):
        self.challongeUsername = challongeUsername
        self.challongeAPIKey = challongeAPIKey
        self.smashggAPIKey = smashggAPIKey
        self.templatePath = templatePath

    def print(self):
        print("API Settings:")
        print("Challonge.com Username: " + self.challongeUsername)
        print("Challonge.com API Key: " + self.challongeAPIKey)
        print("Smash.gg API Key: " + self.smashggAPIKey)
        print("Template Path: " + self.templatePath)
