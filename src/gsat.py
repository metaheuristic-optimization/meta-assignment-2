from src.tabu_queue import Tabu
from src.utils import Utils


class GSAT:
    """
    GSAT Implementation
    """

    def __init__(self, formula, max_steps, max_iterations, tabu_max_length):
        self.formula = formula
        self.max_steps = max_steps
        self.max_iterations = max_iterations
        self.tabu_max_length = tabu_max_length
        self.variables = formula[0]
        self.tabu = Tabu(tabu_max_length)

    def run(self):
        for i in range(self.max_steps):

            state = Utils.generate_random_starting_point(self.variables)
            self.tabu.reset()

            for x in range(self.max_iterations):
                solution_found, unsat_clause = self.solution_status(self.formula, state)

                if solution_found is True:
                    print('Solution found')
                    return state

                state = self.choose_best_variable(state, unsat_clause)

    def choose_best_variable(self, state, current_unsat_clause):
        best_flip = current_unsat_clause
        best = state.copy()

        for i in range(len(self.variables)):
            if self.tabu.is_item_in_queue(self.variables[i]):
                continue

            tmp_state = state.copy()

            Utils.flip_variable(tmp_state, self.variables[i])

            _, unsat_clause = self.solution_status(self.formula, tmp_state)

            if unsat_clause < best_flip:
                best_flip = unsat_clause
                best = tmp_state
                self.tabu.add_to_queue(self.variables[i])

        return best

    def solution_status(self, instance, sol):
        """
        Checks if the solution satisfies all the clauses
        :param instance: The current state
        :param sol: The solution to check
        :return:
            - True if all clauses have been satisfied, otherwise False
            - The number of clauses that are unsatisfied
        """
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
            # print("UNSAT Clauses: ", unsat_clause)
            return False, unsat_clause
        return True, unsat_clause
