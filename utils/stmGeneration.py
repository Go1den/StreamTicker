from copy import deepcopy
from datetime import datetime

from objects.formatInfo import FormatInfo
from objects.matchInfo import MatchInfo
from objects.playerInfo import PlayerInfo
from objects.tournamentInfo import TournamentInfo
from utils.helperMethods import writeJSON

def generateStmFile(tournamentInfo: TournamentInfo, template: dict, includeShoutout: bool) -> str:
    result = []
    sortOrder = 0
    template = template[0]
    if includeShoutout:
        result.append(getShoutout())
    for match in tournamentInfo.matches:
        sortOrder += 1
        message = {"nickname": template["nickname"] + str(match.round) + match.identifier,
                   "sortOrder": sortOrder,
                   "parts": deepcopy(template["parts"])}
        for part in message["parts"]:
            if part["partType"] == "Tournament Data":
                part["partType"] = "Text"
                part["value"] = getTournamentPartValue(match, tournamentInfo.entrants[match.player1ID], tournamentInfo.entrants[match.player2ID], tournamentInfo.format,
                                                       part["value"])
        message["overrides"] = deepcopy(template["overrides"])
        result.append(message)
    timestamp = datetime.now().strftime("%m%d%y-%H%M%S")
    writeTo = "messages/challonge_" + timestamp + ".stm"
    writeJSON(writeTo, result)
    return writeTo

def getShoutout() -> dict:
    return {
        "nickname": "StreamTicker",
        "sortOrder": 1,
        "parts": [
            {
                "partType": "Pixel Gap",
                "sortOrder": 1,
                "value": "8"
            },
            {
                "partType": "Image",
                "sortOrder": 2,
                "value": "imagefiles/stLogo28.png"
            },
            {
                "partType": "Pixel Gap",
                "sortOrder": 3,
                "value": "8"
            },
            {
                "partType": "Text",
                "sortOrder": 4,
                "value": "Powered by StreamTicker"
            }
        ],
        "overrides": {}
    }

def getTournamentPartValue(match: MatchInfo, player1: PlayerInfo, player2: PlayerInfo, format: FormatInfo, value: str) -> str:
    # TODO implement reading image from URL for the player icons
    if value == "Player 1's Score":
        return str(','.join(match.player1Scores))
    elif value == "Player 2's Score":
        return str(','.join(match.player2Scores))
    elif value == "Round":
        return getRoundName(match, player1, format)
    elif value == "Match Score with Winning Player's Score First":
        return str(match.scoreStringWithWinningPlayersScoresFirst)
    elif value == "Winning Player's Score":
        if match.winnerID == match.player1ID:
            return str(','.join(match.player1Scores))
        else:
            return str(','.join(match.player2Scores))
    elif value == "Losing Player's Score":
        if match.loserID == match.player1ID:
            return str(','.join(match.player1Scores))
        else:
            return str(','.join(match.player2Scores))
    elif value == "Player 1's Username":
        return str(player1.username)
    elif value == "Player 2's Username":
        return str(player2.username)
    elif value == "Player 1's Display Name":
        return str(player1.displayName)
    elif value == "Player 2's Display Name":
        return str(player2.displayName)
    elif value == "Winning Player's Username":
        return str(getWinningPlayer(match, player1, player2).username)
    elif value == "Winning Player's Display Name":
        return str(getWinningPlayer(match, player1, player2).displayName)
    elif value == "Winning Player's Seed":
        return str(getWinningPlayer(match, player1, player2).seed)
    elif value == "Losing Player's Username":
        return str(getLosingPlayer(match, player1, player2).username)
    elif value == "Losing Player's Display Name":
        return str(getLosingPlayer(match, player1, player2).displayName)
    elif value == "Losing Player's Seed":
        return str(getWinningPlayer(match, player1, player2).seed)
    return ""

def getLosingPlayer(match: MatchInfo, player1: PlayerInfo, player2: PlayerInfo) -> PlayerInfo:
    if match.loserID == match.player1ID:
        return player1
    elif match.loserID == match.player2ID:
        return player2
    return PlayerInfo()

def getWinningPlayer(match: MatchInfo, player1: PlayerInfo, player2: PlayerInfo) -> PlayerInfo:
    if match.winnerID == match.player1ID:
        return player1
    elif match.winnerID == match.player2ID:
        return player2
    return PlayerInfo()

def getRoundName(match: MatchInfo, player1: PlayerInfo, format: FormatInfo):
    if player1.isGroupID:
        return "Pools Round " + str(abs(match.round))
    if format.type == "single elimination":
        if format.hasGroupStages:
            return "Bracket Round " + str(abs(match.round))
        else:
            return "Round " + str(abs(match.round))
    if format.type == "double elimination":
        result = ""
        if match.round * -1 < 0:
            result += "Winners "
        else:
            result += "Losers "
        result += "Round " + str(abs(match.round))
        return result
    return "Round " + str(abs(match.round))
