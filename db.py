from pymongo import MongoClient


client = MongoClient("mongodb+srv://afif:123@afifcluster.yavul.mongodb.net/reksti?retryWrites=true&w=majority")

db = client.reksti