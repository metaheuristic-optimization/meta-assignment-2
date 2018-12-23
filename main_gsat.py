import time
from src import Utils
from src import GSAT
from multiprocessing import Process
import sys

cnf = Utils.load_dimacs_cnf_file('./datasets/{0}'.format(sys.argv[1]))


def run():
    start_time = time.time()

    gsat = GSAT(formula=cnf, max_steps=10, max_iterations=10000, tabu_max_length=5)
    state, iterations = gsat.run()

    end_time = (time.time() - start_time)

    if state is not None:
        print('Solution found at iteration {0}'.format(iterations, end_time))
    else:
        print('Unable to find a solution')


if __name__ == '__main__':

    for i in range(10):
        p = Process(target=run)
        p.start()
