import json


data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)




#mon_fichier = open("../data simulation/1000 villes/result_tronque.json","r")
#contenu = mon_fichier.read()
#print(contenu)

with open("../data simulation/1000 villes/result_tronque.json") as json_file:
    data = json.load(json_file)


def get_neighbours(id):
    return data[id]['Neighbours']

def get_neighbours_id(id):
    return data[id]['Neighbours']['City']

#print(get_neighbours(2))
#print(get_neighbours_id(2))
print(data[0]['Neighbours']["City"])