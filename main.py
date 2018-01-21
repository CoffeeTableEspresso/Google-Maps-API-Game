# serve.py

from flask import Flask, jsonify, request
from flask import render_template
from backend import returnurl
from Algorithms import *

# creates a Flask application, named app
app = Flask(__name__)

class coordinates():
	def __init__(self, lat, lng):
		self.lat = lat
		self.lng = lng
		return


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/get_guess")
def GetGuess():
	image = returnurl()
	coordinates.lat = float(image['lat'])
	coordinates.lng = float(image['lng'])
	return jsonify(
			image_url=image['url']
		)

@app.route("/guess", methods=["POST"])
def Guess():
	lat_guess = float(request.get_json()["lat"])
	lng_guess = float(request.get_json()["lng"])
	return jsonify(
			new_score = getScore((lat_guess,lng_guess),(coordinates.lat,coordinates.lng)),
			actual_lat = coordinates.lat,
			actual_lng = coordinates.lng
		)

# run the application
if __name__ == "__main__":  
    app.run(debug=True)