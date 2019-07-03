import json
import matplotlib.pyplot as plt

#open and load json data
with open("out_txt/bestroute.txt") as json_file:
    data = json.load(json_file)



listlist=[[188, 104], [190, 150], [113, 198], [67, 186], [95, 152], [136, 148], [165, 109], [151, 90], [148, 110], [144, 109], [130, 104], [96, 104], [108, 76], [47, 49], [107, 41], [134, 37], [162, 14], [162, 70], [197, 60], [194, 75]]

#print(data)
listX=[]
listY=[]
for (x,y) in listlist:
    listX.append(x)
    listY.append(y)

print(listX)
print(listY)
plt.plot(listX,listY)


plt.grid()

plt.show()


"""

#retrieve neighbours from json
def get_neighbours(id):
    return data[id]['Neighbours']

#retrieve city from neighbours from json NOT OPERATIONAL NOW
def get_neighbours_id(id,nbr_item):
    for i in range(0, nbr_item):
        return data[0]['Neighbours'][i]["City"]



def writeFile():
    f = open("test.txt", "r")
    f.write("Now the file has more content!")
   f.close()

writeFile()


"""