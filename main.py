from src import Utils

utils = Utils()

cnf = utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')

print(cnf)
