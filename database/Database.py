__author__ = "Bipin Oli"

import pymongo


class Database:
	''' It performs all the works related to database '''
	DATABASE = "sentemon"
	URI = "mongodb://127.0.0.1:27017"
	db = None

	@staticmethod
	def init():
		client = pymongo.MongoClient(Database.URI)
		Database.db = client[Database.DATABASE]
		print("Database initialized!")

	@staticmethod
	def insert(collection, data):
		# data must be a dictionary
		if Database.db == None:
			print("--- Database hasn't been initialized!")
		try:
			Database.db[collection].insert(data)
			print("Data inserted successfully!")
		except Exception as e:
			print("Exception occur while inserting!!")
			print(str(e))

	@staticmethod
	def update(collection, data):
		if Database.db == None:
			print("--- Database hasn't been initialized!")
		try:
			Database.db[collection].update({"type": data["type"]}, data, upsert = True)
			print("Data updated successfully!")
		except Exception as e:
			print("Exception occur while updating!!")
			print(str(e))

	@staticmethod
	def find_one(collection, type, tag = None):
		if Database.db == None:
			print("--- Database hasn't been initialized!")
		try:
			if tag == None:
				return Database.db[collection].find_one({"type": type})
			else:
				return Database.db[collection].find_one({"type": type, "tag": tag})
		except Exception as e:
			print("Exception occur while updating!!")
			print(str(e))
	
	@staticmethod
	def find_all(type):
		if Database.db == None:
			print("--- Database hasn't been initialized!")
		try:
			collections = [col for col in Database.db.collection_names()]
			retval = []
			for col in collections:
				retval.append(Database.find_one(col, type = type))

			return retval
		except Exception as e:
			print("Database Exception in find_all() function!!")
			print(str(e))
