from flask import Flask, request, jsonify, make_response

import json
import os


# Init app
app = Flask(__name__)


@app.route('/isalive', methods=['GET'])
def islive():
    return "Działa"


@app.route('/getminmax', methods=['GET', 'POST'])
def getminmax():
    if request.is_json:

        # Parsuje JSONa do słownika Python 
        req = request.get_json()

        element = req["geometry"]["type"]
        coordinates = req["geometry"]["coordinates"]

        # Zwraca ciąg wraz z kodem statusu HTTP
        return "JSON received!", 200

    else:

        # Treść żądania nie była JSON, więc zwróć kod stanu HTTP 400
        return "Request was not JSON", 400


@app.route('/getpolygons', methods=['GET', 'POST'])
def getpolygons():
    if request.is_json:

        # Parsuje JSONa do słownika Python 
        polygons = request.get_json()

        element = polygons["geometry"]["type"]
        coordinates = polygons["geometry"]["coordinates"]

        # Zwraca ciąg wraz z kodem statusu HTTP
        return "JSON received!", 200

    else:

        # Treść żądania nie była JSON, więc zwróć kod stanu HTTP 400
        return "Request was not JSON", 400

# Start
if __name__ == "__main__":
    app.run()