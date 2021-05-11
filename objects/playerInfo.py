class PlayerInfo:
    def __init__(self, playerID: int = 0, username: str = "", displayName: str = "", seed: int = 0, iconURL: str = "", isGroupID: bool = False):
        self.playerID = playerID
        self.username = username if username else "Anonymous"
        self.displayName = displayName if displayName else "Anonymous"
        self.seed = seed
        self.iconURL = iconURL
        self.isGroupID = isGroupID

    def print(self):
        if self.playerID:
            print("ID: " + str(self.playerID))
        if self.username:
            print("Username: " + self.username)
        if self.displayName:
            print("Display Name: " + self.displayName)
        if self.seed:
            print("Seed: " + str(self.seed))
        if self.iconURL:
            print("Icon URL: " + self.iconURL)
