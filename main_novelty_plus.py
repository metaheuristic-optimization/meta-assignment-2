import time
from src import Utils
from src import NoveltyPlus
from multiprocessing import Process, cpu_count
import sys

"""
Starting point for the Novelty+ experiment
"""

# Load the data
cnf = Utils.load_dimacs_cnf_file('./datasets/{0}'.format(sys.argv[1]))

# Write initial headers to the csv file for storing results
f = open('./experiments/novelty_plus/{0}.csv'.format(sys.argv[1]), 'w')
f.write('{0}, {1}, {2}\n'.format("Iterations", "Time", "Found"))
f.close()


def run():
    # Record the starting time
    start_time = time.time()

    # Create and run a new Novelty+ instance
    novelty_plus = NoveltyPlus(formula=cnf, wp=0.4, p=0.3, max_iterations=100000)
    state, iterations = novelty_plus.run()

    # Record the end point time
    end_time = (time.time() - start_time)

    # Open csv file to record results
    f = open('./experiments/novelty_plus/{0}.csv'.format(sys.argv[1]), 'a')

    # Check if a solution was found
    if state is not None:
        print('Solution found at iteration {0} in {1} seconds'.format(iterations, end_time))

        # Add a new entry to the results csv file
        f.write('{0}, {1}, {2}\n'.format(iterations, end_time, "True"))
    else:
        print('Unable to find a solution with {0} iterations in {1} seconds'.format(i, end_time))

        # Add a new entry to the results csv file
        f.write('{0}, {1}, {2}\n'.format(iterations, end_time, "False"))

    # Close the file
    f.close()


if __name__ == '__main__':
    """
    Runs the run function on multiple threads to speed up the process of data collection
    """
    # Get total cpus
    total_process = cpu_count()

    # If a user provides a thread count then use that instead of total cpus
    if len(sys.argv) > 2:
        total_process = int(sys.argv[2])

    # Run the threads
    for i in range(total_process):
        p = Process(target=run)
        p.start()
