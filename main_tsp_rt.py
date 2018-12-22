from src.tsp import TSP
import sys

for i in range(5):
    print('=======Experiment {0}======='.format(i))

    tsp = TSP('./datasets/tsp/' + sys.argv[1], total_iterations=5, local_search_time_limit=300, starting_algorithm='random_tours')

    tsp.run()