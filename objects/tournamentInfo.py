from objects.formatInfo import FormatInfo
from objects.matchInfo import MatchInfo
from objects.playerInfo import PlayerInfo

class TournamentInfo:
    def __init__(self, matches: list[MatchInfo], entrants: dict[int, PlayerInfo], format: FormatInfo):
        self.matches = matches
        self.entrants = entrants
        self.format = format

    def print(self):
        for match in self.matches:
            match.print()
        for entrant in self.entrants.values():
            entrant.print()
        self.format.print()
