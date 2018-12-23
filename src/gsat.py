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
        """
        Run the GSAT algorithm

        :return:
            - The current best state, or None if no solution is found
            - The current iteration number
        """

        # Loop for n iterations
        for i in range(self.max_steps):

            # Chose a random starting point
            state = Utils.generate_random_starting_point(self.variables)

            # Reset tabu list
            self.tabu.reset()

            for x in range(self.max_iterations):
                # Check if solution found
                solution_found, unsat_clause = self.solution_status(self.formula, state)

                # If true then return the state and current iteration number
                if solution_found is True:
                    return state, x

                # Update start with new best state
                state = self.choose_best_variable(state, unsat_clause)

        return None, self.max_iterations

    def choose_best_variable(self, state, current_unsat_clause):
        """
        Find the best variable to flip

        :param state: The current state
        :param current_unsat_clause: The current total unsatisfied clauses
        :return: The best count of unsatisfied variables
        """
        best_flip = current_unsat_clause
        best = state.copy()

        # Loop through all variables
        for i in range(len(self.variables)):

            # Check if variable is in tabu list, if it is then continue to next iteration
            if self.tabu.is_item_in_queue(self.variables[i]):
                continue

            tmp_state = state.copy()

            # Flip the variable
            Utils.flip_variable(tmp_state, self.variables[i])

            # Compute the solution
            _, unsat_clause = self.solution_status(self.formula, tmp_state)

            # If this solution is better than the current best, then make this solution the new best
            if unsat_clause < best_flip:
                best_flip = unsat_clause
                best = tmp_state

                # Add new best solution flip variable to tabu list
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
