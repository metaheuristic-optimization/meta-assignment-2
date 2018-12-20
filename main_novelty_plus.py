from src import Utils
from src import NoveltyPlus
from multiprocessing import Process

def run():
    cnf = Utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')
    novelty_plus = NoveltyPlus(formula=cnf, wp=0.4, p=0.3, max_iterations=100000)
    solution = novelty_plus.run()

    print(solution)

if __name__ == '__main__':
    threads = []

    for i in range(100):
        p = Process(target=run)
        p.start()
        threads.append(p)

    for process in threads:
        process.join()
