import json
import matplotlib.pyplot as plt

#open and load json data
with open("out_txt/thomas.json") as json_file:
    data = json.load(json_file)



def readJsonCities(path,id,type):
    with open(path) as json_file:
        dataJsonCities = json.load(json_file)
        return(str(dataJsonCities[len(dataJsonCities)-1]['ID']))






print(readJsonCities("out_txt/thomas.json",19,'Y'))

