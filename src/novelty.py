import heapq
import random
from src.utils import Utils


class Novelty:

    def __init__(self, formula, variables, p):
        self.formula = formula
        self.variables = variables
        self.p = p

    def run_heuristic(self, state, current_flip_variable, random_clause):
        if current_flip_variable not in random_clause:
            return current_flip_variable
        else:
            return self.choose_best_or_second_best_variable_in_clause(state)

    def choose_best_or_second_best_variable_in_clause(self, state):
        tmp_state = state.copy()
        scores = {}

        for i in range(len(self.variables)):
            Utils.flip_variable(tmp_state, self.variables[i])

            _, unsat_clauses = self.solution_status(self.formula, tmp_state)

            scores[self.variables[i]] = unsat_clauses

            Utils.flip_variable(tmp_state, self.variables[i])

        # Find best and second best
        sorted = heapq.nsmallest(2, scores, key=scores.get)

        best = sorted[0]
        second_best = sorted[1]

        noise = random.uniform(0, 1)

        if noise < self.p:
            return second_best
        else:
            return best

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
