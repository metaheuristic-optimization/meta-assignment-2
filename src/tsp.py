import numpy as np
import math


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

    def random_permutation(self):
        return np.random.permutation(self.data_list)

    def euclidean_distance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

    def calculate_cost(self, state):
        """
        Computing the cost or fitness of the individual
        """
        cost = 0
        for i in range(self.genSize - 1):
            print(cost)
            cost += self.euclidean_distance(state[i], state[i + 1])

        return cost

    def run(self):
        print(self.data)
        print(self.genSize)
        print(self.data_list)

        random_starting_point = self.random_permutation()
        cost = self.calculate_cost(random_starting_point)

        print(cost)
