import random
from src.utils import Utils


class WalkSAT:

    def __init__(self, formula, variable):
        self.formula = formula
        self.variable = variable

    def run(self, state):

        solution_found, unsat_clause, unsat_clause_list = self.solution_status(self.formula, state)

        random_clause = random.choice(unsat_clause_list)

        random_variable_in_clause = random.choice(random_clause)

        Utils.flip_variable(state, abs(random_variable_in_clause))

        return state

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
