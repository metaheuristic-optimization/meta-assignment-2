from src import Utils
from src import GSAT

utils = Utils()
cnf = utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')

for i in range(10):
    gsat = GSAT(formula = cnf, max_steps = 100, max_iterations = 1000, tabu_max_length = 5)
    solution = gsat.run()

    print(solution)
