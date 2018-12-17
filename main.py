from src import Utils

utils = Utils()

max_var, cnf = utils.load_dimacs_cnf_file('./datasets/test.cnf')

print(cnf)
