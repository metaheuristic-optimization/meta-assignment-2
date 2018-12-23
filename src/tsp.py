import time
import math
import random
import functools


class TSP:
    """
    TSP Implementation
    """

    def __init__(self, file, total_iterations, local_search_time_limit, starting_algorithm):
        self.file = file
        self.genSize = 0
        self.data = {}
        self.data_list = []
        self.read_instance()
        self.total_iterations = total_iterations
        self.local_search_time_limit = local_search_time_limit
        self.starting_algorithm = starting_algorithm

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
        Calculates the distance between 2 cities using euclidean distance algorithm

        Note as this function gets called many thousands of times, I have memoized the function with lru_cache
        which will prevent this function from running if it has the result already in cache
        :param c1: The first city
        :param c2: The second city
        :return: The distance between the first and second city
        """
        d1 = self.data[c1]
        d2 = self.data[c2]
        return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)

    def random_tours(self):
        """
        Generates a random tour of all cities ending with the same city we started at.

        Cities can only be visited once and all cities must be visited
        :return:
        """
        print('Generating initial random tour')

        # Use temporary variable to generate random tour
        tour = self.data_list.copy()

        # Randomly shuffle the cities in the tour
        random.shuffle(tour)

        # Append the first city to the end of the list to make sure we end up back at the origin city
        tour.append(tour[0])

        return tour

    def nearest_neighbours(self):
        """
        Use greedy nearest neighbour algorithm to generate the tour of cities
            1. Pick a random starting point
            2. Find the nearest neighbour to that city
            3. Add that city to the list of visited cities
            4. Remove the chosen city from our list to avoid re-visiting the city
        :return: A list of visited cities
        """
        print('Generating initial nearest neighbours')
        tour = self.data.copy()

        # Chose random starting point
        random_start = random.choice(list(tour))
        path = []
        current_location = random_start

        # While there are more cities keep looping exhaustively
        while tour:
            nearest_location = None
            nearest_distance = None

            # Loop until we find the nearest neighbour
            for i in tour.keys():

                distance = self.euclidean_distance(current_location, i)

                # Check if city is the closest to the current city
                if nearest_location is None or distance < nearest_distance:
                    nearest_location = i
                    nearest_distance = distance

            # Append the nearest city to the tour
            path.append(nearest_location)

            # Delete the current city to avoid re-visiting that city
            del tour[nearest_location]

        # Add the starting city to the end of the list to make sure we end up back where we started
        path.append(path[0])

        return path

    def three_opt(self, state, cost):
        """
        Implementation of the 3-opt algorithm
            - Swap 3 cities
            - Find the cities that when swapped produce the greatest cost reduction

        Note as this can take a long time to run we apply a time limit to the function.
        When the function exceeds this time limit we will return the best state that we have currently found
        :param state: The current best tour
        :param cost: The current best cost
        :return: The new tour and cost
        """
        tmp = state.copy()
        new_state = state
        new_cost = cost
        start_time = time.time()

        # First Loop for variable 1
        for a in self.data_list:

            # Second loop for variable 2
            for b in self.data_list:

                # Third loop for variable 3
                for c in self.data_list:

                    # Swap the 3 variables
                    new_tmp_state = tmp[:a] + tmp[a:b][::-1] + tmp[b:c][::-1] + tmp[c:]

                    # Compute the new cost
                    new_tmp_cost = self.calculate_cost(new_tmp_state)

                    # Check if the swapped 3 variables has reduced the cost
                    if new_tmp_cost < cost:
                        new_state = new_tmp_state
                        new_cost = new_tmp_cost

                    # Check if we have exceeded the configured time limit
                    if (time.time() - start_time) > self.local_search_time_limit:
                        print('Exceeded maximum time in local search, returning best found value')
                        return new_state, new_cost

        return new_state, new_cost

    def two_opt(self, state):
        """
        Implementation of the 2-opt algorithm
            - Chose 2 random variables
            - Swap the 2 variables
            - Repeat 5 times
        :param state: The current tour
        :return: The new tour with the swapped variables
        """
        tmp_state = state.copy()

        # Loop 5 times
        for i in range(5):
            # Chose 2 random variables
            random_locations = random.sample(range(len(self.data_list)), 2)

            edge_1 = random_locations[0]
            edge_2 = random_locations[1]

            # Swap the 2 variables
            tmp_state[edge_1] = state[edge_2]
            tmp_state[edge_2] = state[edge_1]

        return tmp_state

    def calculate_cost(self, state):
        """
        Compute the cost of our tour
        :param state: The current tour
        :return: The cost of the tour using euclidean distance
        """
        # Initial cost set to zero
        cost = 0

        # Loop through all the edges in the tour adding to the cost
        for i in range(self.genSize - 1):
            cost += self.euclidean_distance(state[i], state[i + 1])

        return cost

    def run(self):
        """
        TSP algorithm with local search
        :return:
        """
        initial_solution = self.data_list

        # Either use nearest neighbours or random tours to compute the starting tour
        if self.starting_algorithm == 'nearest_neighbours':
            initial_solution = self.nearest_neighbours()
        elif self.starting_algorithm == 'random_tours':
            self.starting_algorithm = self.random_tours()

        # Compute the initial cost
        initial_cost = self.calculate_cost(initial_solution)

        print('Initial Cost {0}'.format(initial_cost))

        solution = initial_solution.copy()
        cost = initial_cost

        # Do a 3-opt local search
        solution, cost = self.three_opt(solution, cost)

        # Loop for n iterations
        for i in range(self.total_iterations):
            # Dp a 2-opt perturbation
            solution = self.two_opt(solution)

            # Do a 3-opt local search
            solution, cost = self.three_opt(solution, cost)

        improvement = initial_cost - cost

        # Print results
        print('Final cost is {0}'.format(cost))
        print('Improvement is {0}'.format(improvement))
