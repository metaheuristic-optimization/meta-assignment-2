import random
from src.utils import Utils
from src.novelty import Novelty
from src.walk_sat import WalkSAT


class NoveltyPlus:

    def __init__(self, formula, wp, p, max_iterations):
        self.formula = formula
        self.wp = wp
        self.p = p
        self.max_iterations = max_iterations
        self.variables = formula[0]
        self.novelty = Novelty(formula, self.variables, p)
        self.walkSat = WalkSAT(formula, self.variables)

    def run(self):

        state = Utils.generate_random_starting_point(self.variables)

        for i in range(self.max_iterations):

            solution_found, unsat_clause, unsat_clause_list = self.solution_status(self.formula, state)

            if solution_found is True:
                print('Solution found')
                return state

            if self.wp < random.uniform(0, 1):
                state = self.walkSat.run(state)
            else:
                random_flip = random.choice(self.variables)
                random_clause = random.choice(unsat_clause_list)

                best_flip = self.novelty.run_heuristic(state, random_flip, random_clause)

                Utils.flip_variable(state, best_flip)

    def solution_status(self, instance, sol):
        clause = instance[1]
        unsat_clause = 0
        unsat_clause_list = []
        for clause_i in clause:
            cStatus = False
            tmp = []
            for var in clause_i:
                if var < 0:
                    if (1 - sol[-var]) == 1:
                        cStatus = True
                    tmp.append([var, sol[-var]])
                else:
                    tmp.append([var, sol[var]])
                    if sol[var] == 1:
                        cStatus = True
            if not cStatus:
                unsat_clause += 1
                unsat_clause_list.append(clause_i)

        if unsat_clause > 0:
            return False, unsat_clause, unsat_clause_list
        return True, unsat_clause, unsat_clause_list
