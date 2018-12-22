from src.tsp import TSP

tsp = TSP('./datasets/tsp/inst-0.tsp', total_iterations=5, local_search_time_limit=300, starting_algorithm='random_tours')

tsp.run()
