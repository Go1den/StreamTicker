from base64 import b64encode

import requests
from requests.auth import HTTPBasicAuth

from objects.formatInfo import FormatInfo
from objects.matchInfo import MatchInfo
from objects.playerInfo import PlayerInfo
from objects.tournamentInfo import TournamentInfo

def getAuthString(username, apiKey) -> str:
    try:
        thing = username + ":" + apiKey
        s = b64encode(thing.encode()).decode()
        return "Basic %s" % s
    except Exception as e:
        print("Unable to get auth string")

def getTournament(username: str, apiKey: str, url: str = "", subdomain: str = "") -> dict:
    apiEndpoint = 'https://api.challonge.com/v1/tournaments/'
    if subdomain:
        apiEndpoint += subdomain + "-"
    apiEndpoint += url + ".json"
    basicAuth = HTTPBasicAuth(username, apiKey)
    try:
        r = requests.get(apiEndpoint, auth=basicAuth, headers={"User-Agent": "Mozilla/5.0"}, params={"include_participants": 1, "include_matches": 1})
        t = r.json()["tournament"]
        return t
    except Exception as e:
        print("Unable to obtain tournament information from the API")
        return {}

def getParticipants(participants: dict) -> list[PlayerInfo]:
    result = []
    for participant in participants:
        p = participant["participant"]
        for gpID in p["group_player_ids"]:
            result.append(PlayerInfo(gpID, p["username"], p["display_name"], p["seed"], p["attached_participatable_portrait_url"], True))
        result.append(PlayerInfo(p["id"], p["username"], p["display_name"], p["seed"], p["attached_participatable_portrait_url"], False))
    return result

def getParticipantDictionary(participants: list[PlayerInfo]) -> dict[int, PlayerInfo]:
    result = {}
    for p in participants:
        if p.playerID not in result:
            result[p.playerID] = p
    return result

def getMatches(matches: dict) -> list[MatchInfo]:
    return [MatchInfo(match["match"]) for match in matches]

def getTournamentInfo(challongeUsername: str, challongeAPIKey: str, tournamentURL: str) -> TournamentInfo:
    try:
        url = tournamentURL.rstrip('/').split('/')[-1]
    except:
        url = None
    try:
        subdomain = tournamentURL.split('.')[0].split('/')[-1]
        if subdomain.lower() == "challonge":
            subdomain = None
    except:
        subdomain = None
    t = getTournament(challongeUsername, challongeAPIKey, url, subdomain)
    formatInfo = FormatInfo(t["group_stages_enabled"], t["hold_third_place_match"], t["full_challonge_url"], t["swiss_rounds"], t["tournament_type"])
    entrants = getParticipants(t["participants"])
    entrantsDict = getParticipantDictionary(entrants)
    games = getMatches(t["matches"])
    return TournamentInfo(games, entrantsDict, formatInfo)
