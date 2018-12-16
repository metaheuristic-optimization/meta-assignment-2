from src import Utils

utils = Utils()

cnf, max_var = utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')

print(cnf)
print(max_var)
