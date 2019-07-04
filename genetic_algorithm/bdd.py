import pymongo
import datetime



import json


uri = "mongodb://testetete:hHHA8cYHbRDG3lLcvmcst2ZbmsNz8fN6be7YVUh1CezAF081UfUnNSAfs6DmyPCP4k0kP0owB22jfcQEig7fpg==@testetete.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
db = client.projet
city = db.city




with open("out_txt/thomas.json") as json_file:
    data = json.load(json_file)

city.insert_one(data)
client.close()