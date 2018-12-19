from src import Utils
from src import NoveltyPlus


def run():
    cnf = Utils.load_dimacs_cnf_file('./datasets/uf20-020.cnf')
    novelty_plus = NoveltyPlus(formula=cnf, wp=0.4, p=0.3, max_iterations=100000)
    solution = novelty_plus.run()

    print(solution)


run()
