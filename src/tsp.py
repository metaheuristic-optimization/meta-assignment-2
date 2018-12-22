import time
import math
import random
import functools


class TSP:

    def __init__(self, file, total_iterations, local_search_time_limit):
        self.file = file
        self.genSize = 0
        self.data = {}
        self.data_list = []
        self.read_instance()
        self.total_iterations = total_iterations
        self.local_search_time_limit = local_search_time_limit

    def read_instance(self):
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

    @functools.lru_cache(maxsize=None)
    def euclidean_distance(self, c1, c2):
        """
        Distance between two cities
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

    def nearest_neighbours(self):
        tour = self.data.copy()
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

    def three_opt(self, state, cost):

        tmp = state.copy()
        new_state = state
        new_cost = cost
        start_time = time.time()

        for a in self.data_list:

            for b in self.data_list:

                for c in self.data_list:

                    new_tmp_state = tmp[:a] + tmp[a:b][::-1] + tmp[b:c][::-1] + tmp[c:]
                    new_tmp_cost = self.calculate_cost(new_tmp_state)

                    if new_tmp_cost < cost:
                        new_state = new_state
                        new_cost = new_tmp_cost

                    if (time.time() - start_time) > self.local_search_time_limit:
                        print('Exceeded maximum time in local search, returning best found value')
                        return new_state, new_cost

        return new_state, new_cost

    def two_opt(self, state):

        tmp_state = state.copy()

        for i in range(5):
            random_locations = random.sample(range(len(self.data_list)), 2)

            edge_1 = random_locations[0]
            edge_2 = random_locations[1]

            tmp_state[edge_1] = state[edge_2]
            tmp_state[edge_2] = state[edge_1]

        return tmp_state

    def calculate_cost(self, state):
        """
        Computing the cost or fitness of the individual
        """
        cost = 0
        for i in range(self.genSize - 1):
            cost += self.euclidean_distance(state[i], state[i + 1])

        return cost

    def run(self):
        initial_solution = self.nearest_neighbours()
        initial_cost = self.calculate_cost(initial_solution)

        print('Initial Cost {0}'.format(initial_cost))

        solution = initial_solution.copy()
        cost = initial_cost

        solution, cost = self.three_opt(solution, cost)

        for i in range(self.total_iterations):
            solution = self.two_opt(solution)

            solution, cost = self.three_opt(solution, cost)

        improvement = initial_cost - cost
        print('Final cost is {0}'.format(cost))
        print('Improvement is {0}'.format(improvement))
