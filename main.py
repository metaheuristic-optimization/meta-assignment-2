from src import Utils
from src import GSAT
from multiprocessing import Process

def run():
    utils = Utils()
    cnf = utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')
    gsat = GSAT(formula = cnf, max_steps = 100, max_iterations = 1000, tabu_max_length = 5)
    solution = gsat.run()

    print(solution)

if __name__ == '__main__':
    threads = []

    for i in range(10):
        p = Process(target=run)
        p.start()
        threads.append(p)

    for process in threads:
        process.join()
