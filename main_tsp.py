from src.tsp import TSP

tsp = TSP('./datasets/tsp/inst-0.tsp', total_iterations=5, local_search_time=60)

tsp.run()
