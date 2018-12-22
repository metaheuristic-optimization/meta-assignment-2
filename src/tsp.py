import numpy as np
import math
import random


class TSP:

    def __init__(self, file):
        self.file = file
        self.genSize = 0
        self.data = {}
        self.data_list = []
        self.readInstance()

    def readInstance(self):
        """
        Read data from a given file
        """
        file = open(self.file, 'r')
        self.genSize = int(file.readline())
        for line in file:
            (id, x, y) = line.split()
            self.data[int(id)] = (int(x), int(y))

        self.data_list = list(self.data.keys())
        file.close()

    def euclidean_distance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

    def nearest_neighbours(self):
        tour = self.data.copy()
        print(tour.keys())
        random_start = random.choice(list(tour))
        path = []
        current_location = random_start

        while tour:
            nearest_location = None
            nearest_distance = None
            for i in tour.keys():

                distance = self.euclidean_distance(current_location, i)

                if nearest_location is None or distance < nearest_distance:
                    nearest_location = i
                    nearest_distance = distance

            path.append(nearest_location)
            del tour[nearest_location]

        return path

    def calculate_cost(self, state):
        """
        Computing the cost or fitness of the individual
        """
        cost = 0
        for i in range(self.genSize - 1):
            cost += self.euclidean_distance(state[i], state[i + 1])

        return cost

    def run(self):
        nearest_neighbours = self.nearest_neighbours()
        cost = self.calculate_cost(nearest_neighbours)

        print(nearest_neighbours)
        print(cost)
