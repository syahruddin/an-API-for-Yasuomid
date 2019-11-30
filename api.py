import flask
import requests
from flask import request, jsonify ,request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


#masukin api key disini, ingatkan untuk ganti tiap 24 jam
apikey = 'RGAPI-cec5aec1-54ed-4865-87ec-5870e601c44e'

@app.route('/', methods=['GET'])
def home():
    return "<h1>Yasapi</h1> <p>home<p>"

@app.route('/match/matches', methods=['GET'])   
def api_id():
    if 'match_id' in request.args:
        match_id = int(request.args['match_id'])
    else:
        return "Error: No match field provided. Please specify an match."

    # Create an empty list for our results
    results = []
    
    url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(match_id) + "?api_key=" + apikey
    
    response = requests.get(url)
    print(response)
    response
    
    return response.json()

app.run()