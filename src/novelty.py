import heapq
import random
from src.utils import Utils


class Novelty:
    """
    Novelty heuristic implementation
    """

    def __init__(self, formula, variables, p):
        self.formula = formula
        self.variables = variables
        self.p = p

    def run_heuristic(self, state, current_flip_variable, random_clause):
        """
        Run the heuristic

            - Check of the randomly selected variable appears in the randomly selected clause
            - If it does then return the variable
            - If it does not then proceed to find the best variable to flip
        :param state: The current state
        :param current_flip_variable: the random variable to flip
        :param random_clause: The randomly selected clause
        :return:
        """

        if current_flip_variable not in random_clause:
            return current_flip_variable
        else:
            return self.choose_best_or_second_best_variable_in_clause(state)

    def choose_best_or_second_best_variable_in_clause(self, state):
        """
        Finds the best and second best variable and return one or the other depending on a defined noise
        :param state:
        :return:
        """
        tmp_state = state.copy()

        # Temporary variable for tallying up the score of each solution to find best and second best
        scores = {}

        # Loop through the variables
        for i in range(len(self.variables)):
            Utils.flip_variable(tmp_state, self.variables[i])

            # Check the solution
            _, unsat_clauses = self.solution_status(self.formula, tmp_state)

            # Add the solution to the list of scores
            scores[self.variables[i]] = unsat_clauses

            # Reverse the flip to avoid carrying the flip forward to the next iteration
            Utils.flip_variable(tmp_state, self.variables[i])

        # Find best and second best using heapq
        sorted = heapq.nsmallest(2, scores, key=scores.get)

        best = sorted[0]
        second_best = sorted[1]

        # Generate a random noise between 0 and 1
        noise = random.uniform(0, 1)

        # Check if we will return the best or second best based on the provided p value
        if noise < self.p:
            return second_best
        else:
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
            return False, unsat_clause
        return True, unsat_clause
