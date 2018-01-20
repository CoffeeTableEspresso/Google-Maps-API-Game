# serve.py

from flask import Flask, jsonify
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():  
    message = "Hello, World"
    return render_template('index.html', message=message)

@app.route("/get_guess")
def GetGuess():
	return jsonify(
			image_url="http://www.esbnyc.com/sites/default/files/styles/timely_content_image_large__885x590_/public/default_images/brs_0330.jpg?itok=m3gzF1YH"
		)

# run the application
if __name__ == "__main__":  
    app.run(debug=True)