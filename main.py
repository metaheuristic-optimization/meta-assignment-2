from src import Utils
from src import GSAT
from multiprocessing import Process

cnf = Utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')

def run():
    gsat = GSAT(formula=cnf, max_steps=10, max_iterations=1000, tabu_max_length=5)
    solution = gsat.run()

    print(solution)


if __name__ == '__main__':

    for i in range(10):
        p = Process(target=run)
        p.start()
