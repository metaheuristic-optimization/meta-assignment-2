from src.tsp import TSP
import sys

"""
Entry point for TSP with Random Tours
"""
for i in range(5):
    # Print the experiment number
    print('=======Experiment {0}======='.format(i))

    # Create and run a new TSP instance with values
    tsp = TSP('./datasets/tsp/' + sys.argv[1], total_iterations=5, local_search_time_limit=300, starting_algorithm='random_tours')

    tsp.run()
