__author__ = "Bipin Oli"

import requests
import datetime

from flask import Flask, jsonify, request, render_template, url_for, redirect
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


tweet_stream_url = "http://127.0.0.1:8000/serve/"
get_sentiment_url = "http://127.0.0.1:8000/ask_sentiment/"
get_live_sentiment_url = "http://127.0.0.1:8000/ask_liveSentiment"
get_sentiment_history_url = "http://127.0.0.1:8000/ask_sentimentHistory"
# --------------------------------------------------------------------




# Home
@app.route("/")
def home():
	return render_template("home.html")

# Categories
@app.route("/categories")
def categories():
	return render_template("categories.html")


# Technology
@app.route("/technology")
def technology():
	return render_template("technology.html")

# About
@app.route("/about")
def about():
	return render_template("about.html")

# previous_analysis
@app.route("/previous_analysis")
def previous_analysis():
	retval = requests.get(get_sentiment_history_url)
	retval = retval.json()
	return render_template("previous_analysis.html", data = retval)


# Analyze/ Sentiment analysis of the keyword
@app.route("/analyze", methods = ["POST"])
def analyze():
	keyword = request.form["search"]
	return render_template("analyze.html", data = {"keyword": keyword})

@app.route("/analyze/<string:tag>", methods = ["GET"])
def analyze_with_tag(tag):
	keyword = tag
	return render_template("analyze.html", data = {"keyword": keyword})


@socketio.on("ready_to_analyze")
def ready_to_analyze(data):
	print("ready to analyze: " + data["keyword"])
	requests.get(tweet_stream_url + data["keyword"])


@socketio.on("get_liveSentiment")
def get_liveSentiment():
	retval = requests.get(get_live_sentiment_url)
	retval = retval.json()
	socketio.emit("liveSentiment_data", retval)


if __name__ == "__main__":
	socketio.run(app, debug=True, port=5000)