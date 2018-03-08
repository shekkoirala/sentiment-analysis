__author__ = "Bipin Oli"

import datetime

from database import Database

class Sentiment:
	TYPE = "Sentiment"

	def __init__(self, tag, pos = 0, neg = 0):
		Database.init()
		self.type = Sentiment.TYPE
		self.tag = tag
		self.pos = pos
		self.neg = neg
		self.time = str(datetime.datetime.now())

	def save_to_database(self):
		Database.insert(collection = self.tag, data = self.json())

	def update_in_database(self):
		Database.update(self.tag, self.json())

	def find_in_database(self):
		return Database.find_one(collection = self.tag, tag = self.tag, type = self.type)

	def json(self):
		return {
			"type": self.type,
			"tag": self.tag,
			"pos": self.pos,
			"neg": self.neg,
			"time": self.time 
		}