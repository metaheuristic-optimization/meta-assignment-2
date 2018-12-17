from src import Utils
from src import GSAT

utils = Utils()
gsat = GSAT()

cnf = utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')

solution = gsat.run(cnf, 1000)

print(solution)
