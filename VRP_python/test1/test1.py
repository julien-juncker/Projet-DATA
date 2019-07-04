
"""Vehicles Routing Problem (VRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import json
from pprint import pprint
import time
import random
import math

class city:
    def __init__(self):
        self.id = 0
        self.X = 0
        self.Y = 0

class result:
    def __init__(self):
        self.onetruck = []
        self.twotruck = []
        self.threetruck = []
        self.fourtruck = []

def generate_matrix(population, xmax, ymax):
    matrix = [[0 for x in range(population)] for y in range(population)]
    points = []

    for i in range(population):
        temp = city()
        temp.id = i
        temp.X = random.randint(0, xmax)
        temp.Y = random.randint(0, ymax)
        points.append(temp)

    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = get_distance(points[i], points[j])
    return matrix

def get_distance(citya, cityb):
    return int(math.sqrt(math.pow(math.fabs(citya.X - cityb.X), 2) + math.pow(math.fabs(citya.Y - cityb.Y), 2)))

def create_data_model(nbtruck, population, xmax, ymax):
    data = {}
    #with open('test10.json') as f:
    #    data['distance_matrix'] = json.load(f)
    data['distance_matrix'] = generate_matrix(population, xmax, ymax)
    data['num_vehicles'] = nbtruck
    data['depot'] = 0   
    return data


def print_solution(data, manager, routing, solution):
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
    print('Maximum of the route distances: {}m'.format(max_route_distance))
    file = open("result.json","a")
    file.writelines( str(max_route_distance) + ":")
    file.close()

def launch(nbtruck, population, xmax, ymax):
    data = create_data_model(nbtruck, population, xmax, ymax)
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    dimension_name = 'Distance'
    routing.AddDimension(transit_callback_index, 0, 100000, True, dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    start_time = time.time()
    solution = routing.SolveWithParameters(search_parameters)
    end_time = time.time()
    print("Temps d execution : %s secondes ---" % (end_time - start_time))

    if solution:
        print_solution(data, manager, routing, solution)

    return end_time - start_time

def main():
    res = result()
    file = open("result.json","a")
    for j in range(200):
        temp = []
        #for i in range(5):
        #temp.append(launch(4, 75, 400, 400))
        #res.onetruck.append(sum(temp) / len(temp))
        #file.writelines(str(j + 10))
        l = launch(4, 30, 400, 400)
        file.writelines("4:" + str(l) + ":4\n")
        file.flush()
    #for j in range(40):
    #    temp = []
    #    for i in range(5):
    #        temp.append(launch(2,j + 10, 800, 800))
    #    res.twotruck.append(sum(temp) / len(temp))
    #    file.writelines(str(j + 10))
    #    file.writelines(":" + str(res.twotruck[j]) + ":2\n")
    #    file.flush()
    #for j in range(40):
    #    temp = []
    #    for i in range(5):
    #        temp.append(launch(3,j + 10, 800, 800))
    #    res.threetruck.append(sum(temp) / len(temp))
    #    file.writelines(str(j + 10))
    #    file.writelines(":" + str(res.threetruck[j]) + ":3\n")
    #    file.flush()
    #for j in range(40):
    #    temp = []
    #    for i in range(5):
    #        temp.append(launch(4,j + 10, 800, 800))
    #    res.fourtruck.append(sum(temp) / len(temp))
    #    file.writelines(str(j + 10))
    #    file.writelines(":" + str(res.fourtruck[j]) + ":4\n")
    #    file.flush()
    #for j in range(40):
    #    temp = []
    #    for i in range(5):
    #        temp.append(launch(5,j + 10, 800, 800))
    #    res.fourtruck.append(sum(temp) / len(temp))
    #    file.writelines(str(j + 10))
    #    file.writelines(":" + str(res.fourtruck[j]) + ":5\n")
    #    file.flush()
    #for j in range(40):
    #    temp = []
    #    for i in range(5):
    #        temp.append(launch(6,j + 10, 800, 800))
    #    res.fourtruck.append(sum(temp) / len(temp))
    #    file.writelines(str(j + 10))
    #    file.writelines(":" + str(res.fourtruck[j]) + ":6\n")
    #    file.flush()
    #file.writelines("")
    file.close()

if __name__ == '__main__':
    main()