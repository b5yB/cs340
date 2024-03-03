from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal collection in MongoDB """

	def __init__(self, username, password):
		# Initializing the MongoClient. This helps to 
		# access the MongoDB databases and collections.
		# This is hard-wired to use the aac database, the 
		# animals collection, and the aac user.
		# Definitions of the connection string variables are
		# unique to the individual Apporto environment.
		#
		# You must edit the connection variables below to reflect
		# your own instance of MongoDB!
		#
		# Connection Variables
		#
		USER = username
		PASS = password
		HOST = 'nv-desktop-services.apporto.com'
		PORT = 30716
		DB = 'aac'
		COL = 'animals'
		#
		# Initialize Connection
		#
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD.
	def c(self, data):
		if data is not None:
			createData = self.database.animals.insert_one(data)
			return True if createData.inserted_id else False
		else:
			raise Exception("Nothing to create, because data parameter is empty")
			return False

# Read method to implement the R in CRUD.
	def r(self, data):
		if data is not None:
			readData = self.database.animals.find(data)
			readList = list(readData)
			return [] if not readList else readList
		else:
			raise Exception("Nothing to read, because data parameter is empty")
			return []	

# Update method to implement the U in CRUD.
	def u(self, data, newValue):
		if data is not None:
			updateData = self.database.animals.update_many(data, {"$set":newValue})
			return updateData.modified_count
		else:
			raise Exception("Nothing to update, because data parameter is empty")
			return 0

# Delete method to implement the D in CRUD.
	def d(self, data):
		if data is not None:
			deleteData = self.database.animals.delete_many(data)
			return deleteData.deleted_count
		else:
			raise Exception("Nothing to delete, because data parameter is empty")
			return 0
