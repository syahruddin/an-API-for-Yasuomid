import flask
import requests
import json
from flask import request, jsonify ,request ,Flask

app = Flask(__name__)


#masukin api key disini, ingatkan untuk ganti tiap 24 jam
apikey = 'RGAPI-54167148-b56a-4a91-940c-41cbf6dc735d'


#home, kosong
@app.route('/', methods=['GET'])
def home():
    return "<h1>Yasapi</h1> <p>home<p>"

#untuk data2 umum di match tersebut  
@app.route('/match/matches_info', methods=['GET'])   
def matchinfo():
    if 'match_id' in request.args:
        match_id = int(request.args['match_id'])
    else:
        return "Error: No match field provided. Please specify an match."

    # Create an empty list for our results
    matchdata = {
      "gameDuration": 0, 
      "gameId": 0, 
      "gameMode": " ", 
      "gameType": " ", 
      "gameVersion": " ", 
      "mapId": 0, 
      "teamWin": 0,
      "bans": []
    }
    
    url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + apikey
    
    response = requests.get(url)
    
    matchdata['gameDuration'] = response.json()['gameDuration']
    matchdata['gameId'] = response.json()['gameId']
    matchdata['gameMode'] = response.json()['gameMode']
    matchdata['gameType'] = response.json()['gameType']
    matchdata['gameVersion'] = response.json()['gameVersion']
    matchdata['mapId'] = response.json()['mapId']
    matchdata['bans'].extend(response.json()['teams'][0]['bans'])
    matchdata['bans'].extend(response.json()['teams'][1]['bans'])
    if response.json()['teams'][0]['win'] == 'Win':
        matchdata['teamWin'] = 1
    else:
        if response.json()['teams'][1]['win'] == 'Win':
            matchdata['teamWin'] = 2


    
    return matchdata


#untuk info pemain yg terlibat seperti champion yg dipakai, jumlah k/d/a, dll    
@app.route('/match/participant', methods=['GET'])   
def party():
    if 'match_id' in request.args:
        match_id = int(request.args['match_id'])
    else:
        return "Error: No match field provided. Please specify an match."
    
    
    participant = [
                    {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                     {
                        "summonerName": " ",
                        "championId": 0, 
                        "kills": 0, 
                        "deaths": 0, 
                        "assists": 0
                    },
                ]
    
    url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + apikey
    
    response = requests.get(url)
    iteratif = 0
    while iteratif < len(participant):
        participant[iteratif]['summonerName'] = response.json()['participantIdentities'][iteratif]['player']['summonerName']
        participant[iteratif]['championId'] = response.json()['participants'][iteratif]['championId']
        participant[iteratif]['kills'] = response.json()['participants'][iteratif]['stats']['kills']
        participant[iteratif]['deaths'] = response.json()['participants'][iteratif]['stats']['deaths']
        participant[iteratif]['assists'] = response.json()['participants'][iteratif]['stats']['assists']
        iteratif+=1
    
    return jsonify(participant)
    
    

@app.route('/match/matches', methods=['GET'])   
def match():
    if 'match_id' in request.args:
        match_id = int(request.args['match_id'])
    else:
        return "Error: No match field provided. Please specify an match."

    
    url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + apikey
    
    response = requests.get(url)
    
    return response.json()
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)