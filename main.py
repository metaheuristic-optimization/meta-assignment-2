from src import Utils
from src import GSAT

utils = Utils()
gsat = GSAT()

cnf = utils.load_dimacs_cnf_file('./datasets/test.cnf')

print(cnf)

solution = gsat.run(cnf, 100)

print(solution)
