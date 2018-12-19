from src.utils import Utils


class NoveltyPlus:

    def __init__(self, formula, wp, p, max_iterations):
        self.formula = formula
        self.wp = wp
        self.p = p
        self.max_iterations = max_iterations
        self.variables = formula[0]

    def run(self):

        for i in range(self.max_iterations):
            state = Utils.generate_random_starting_point(self.variables)

            solution_found, unsat_clause = self.solution_status(self.formula, state)

    def solution_status(self, instance, sol):
        clause = instance[1]
        unsat_clause = 0
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

        if unsat_clause > 0:
            return False, unsat_clause
        return True, unsat_clause
