class MatchInfo:
    def __init__(self, match: dict):
        self.matchID = match["id"]
        self.state = match["state"]
        self.round = match["round"]
        self.identifier = match["identifier"]
        self.player1ID = match["player1_id"]
        self.player2ID = match["player2_id"]
        self.scoreString = match["scores_csv"]
        self.winnerID = match["winner_id"]
        self.loserID = match["loser_id"]
        self.setScore = ""
        self.player1Scores = []
        self.player2Scores = []
        self.winnerScores = []
        self.loserScores = []
        self.scoreStringWithWinningPlayersScoresFirst = ""
        self.setPlayerScores()
        self.roundForSortingPurposes = (self.round - 0.5) * -1 if self.round < 0 else self.round

    def setPlayerScores(self):
        if self.scoreString:
            sets = self.scoreString.split(",")
            try:
                for set in sets:
                    scores = set.split("-")
                    self.player1Scores.append(scores[0])
                    self.player2Scores.append(scores[1])
            except IndexError:
                print("IndexError")
            if self.winnerID == self.player1ID:
                self.winnerScores = self.player1Scores
            elif self.winnerID == self.player2ID:
                self.winnerScores = self.player2Scores
            if self.loserID == self.player1ID:
                self.loserScores = self.player1Scores
            elif self.loserID == self.player2ID:
                self.loserScores = self.player2Scores
            self.setScoreStringWithWinningPlayersScoresFirst()

    def setScoreStringWithWinningPlayersScoresFirst(self):
        self.scoreStringWithWinningPlayersScoresFirst = ""
        for x in range(len(self.winnerScores)):
            self.scoreStringWithWinningPlayersScoresFirst += str(self.winnerScores[x]) + "-" + str(self.loserScores[x]) + ", "
            self.scoreStringWithWinningPlayersScoresFirst = self.scoreStringWithWinningPlayersScoresFirst.rstrip(", ")

    def print(self):
        print("ID: " + str(self.matchID))
        print("State: " + str(self.state))
        print("Round: " + str(self.round))
        print("Identifier: " + str(self.identifier))
        print("Player1 ID: " + str(self.player1ID))
        print("Player2 ID: " + str(self.player2ID))
        print("Score string: " + str(self.scoreString))
        print("Winner ID: " + str(self.winnerID))
        print("Loser ID: " + str(self.loserID))
        print("Set Score: " + str(self.setScore))
        print("Player1 Scores: " + str(self.player1Scores))
        print("Player2 Scores: " + str(self.player2Scores))
        print("Winner Scores: " + str(self.winnerScores))
        print("Loser Scores: " + str(self.loserScores))
        print("Set Scores with winning player first: " + str(self.scoreStringWithWinningPlayersScoresFirst))
