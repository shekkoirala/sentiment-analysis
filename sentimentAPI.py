__author__ = "Bipin Oli"

import threading
from flask import Flask, jsonify

from machine_learning.streamTwitter import stream
from database import Database
from models import LiveSentiment, Sentiment

Database.init()
app = Flask(__name__)


threads = []

@app.route("/serve/<string:keyword>")
def serve(keyword):
	print("To stream: " + keyword)
	# stream(keyword)
	print ("There were {} threads running.".format(len(threads)))
	# for th in threads:
	# 	print ("Killing thread " + str(th))
	# 	th._stop()
	# th = []

	t = threading.Thread(target = stream, args=(keyword,))
	threads.append(t)
	t.start()
	print ("{} streaming from Twitter in separate thread".format(keyword))
	return "{} streaming from Twitter in separate thread".format(keyword)


@app.route("/ask_liveSentiment")
def ask_liveSentiment():
	retval = Database.find_one("liveSentiment", type = LiveSentiment.TYPE)
	if retval == None:
		print ("ask_liveSentiment returned None")
		return jsonify(retval)
	retval = {
		"type": retval["type"],
		"tag": retval["tag"],
		"pos": retval["pos"],
		"neg": retval["neg"],
		"time": retval["time"]
	}
	return jsonify(retval)

@app.route("/ask_sentiment/<string:keyword>")
def ask_sentiment(keyword):
	retval = Database.find_one(keyword, type = Sentiment.TYPE, tag=keyword)
	if retval == None:
		return jsonify(retval)
	retval = {
		"type": retval["type"],
		"tag": retval["tag"],
		"pos": retval["pos"],
		"neg": retval["neg"],
		"time": retval["time"]
	}
	return jsonify(retval)

@app.route("/ask_sentimentHistory")
def ask_sentimentHistory():
	retval = Database.find_all(Sentiment.TYPE)
	if retval == None:
		return jsonify(retval)

	retvalFinal = []
	for r in retval:
		# print(str(r))
		if r != None:
			retvalFinal.append({
				"type": r["type"],
				"tag": r["tag"],
				"pos": r["pos"],
				"neg": r["neg"],
				"time": r["time"]
			})

	return jsonify(retvalFinal)

if __name__ == "__main__":
	app.run(port = 8000, debug = True)

