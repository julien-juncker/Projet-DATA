import json

#open and load json data
with open("../data simulation/1000 villes/result_tronque.json") as json_file:
    data = json.load(json_file)

#retrieve neighbours from json
def get_neighbours(id):
    return data[id]['Neighbours']

#retrieve city from neighbours from json NOT OPERATIONAL NOW
def get_neighbours_id(id,nbr_item):
    for i in range(0, nbr_item):
        return data[0]['Neighbours'][i]["City"]



