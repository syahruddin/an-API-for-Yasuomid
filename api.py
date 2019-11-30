import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

apikey = ''

@app.route('/', methods=['GET'])
def home():
    return "<h1>Yasapi</h1> <p>home<p>"

@app.route('/lol/match/v4/matches', methods=['GET'])   
def api_id():
    if 'username' in request.args:
        username = string(request.args['username'])
        if 'region' in request.args:
            region = string(request.args['region'])
        else:
            return "Error: No region field provided. Please specify an region."
    else:
        return "Error: No username field provided. Please specify an username."

    # Create an empty list for our results
    results = username + ' ' + region
    
    return jsonify(results)

app.run()