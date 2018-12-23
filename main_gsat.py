import time
from src import Utils
from src import GSAT
from multiprocessing import Process, cpu_count
import sys

cnf = Utils.load_dimacs_cnf_file('./datasets/{0}'.format(sys.argv[1]))

f = open('./experiments/gsat/{0}.csv'.format(sys.argv[1]), 'w')
f.write('{0}, {1}, {2}, {3}\n'.format("Iterations", "Restarts", "Time", "Found"))
f.close()


def run():
    start_time = time.time()

    gsat = GSAT(formula=cnf, max_steps=10, max_iterations=1000, tabu_max_length=5)
    state, restarts, iterations = gsat.run()

    end_time = (time.time() - start_time)

    f = open('./experiments/gsat/{0}.csv'.format(sys.argv[1]), 'a')

    if state is not None:
        print('Solution found at iteration {0} in {1} seconds'.format(iterations, end_time))
        f.write('{0}, {1}, {2}, {3}\n'.format(iterations, restarts, end_time, "True"))
    else:
        print('Unable to find a solution with {0} iterations in {1} seconds'.format(i, end_time))
        f.write('{0}, {1}, {2}, {3}\n'.format(iterations, restarts, end_time, "False"))

    f.close()


if __name__ == '__main__':
    total_process = cpu_count()

    if len(sys.argv) > 2:
        total_process = int(sys.argv[2])

    for i in range(total_process):
        p = Process(target=run)
        p.start()
