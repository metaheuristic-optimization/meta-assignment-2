import random
from src.utils import Utils
from src.novelty import Novelty
from src.walk_sat import WalkSAT


class NoveltyPlus:
    """
    Novelty Plus implementation
    """

    def __init__(self, formula, wp, p, max_iterations):
        self.formula = formula
        self.wp = wp
        self.p = p
        self.max_iterations = max_iterations
        self.variables = formula[0]
        self.novelty = Novelty(formula, self.variables, p)
        self.walkSat = WalkSAT(formula, self.variables)

    def run(self):
        """
        Run the novelty plus algorithm
        :return: The found solution or if no solution could be found then return None
        """

        # Generate a random starting point
        state = Utils.generate_random_starting_point(self.variables)

        # Loop for n iterations
        for i in range(self.max_iterations):

            # Check if a solution has been found
            solution_found, unsat_clause, unsat_clause_list = self.solution_status(self.formula, state)

            # If solution is found then return the solution
            if solution_found is True:
                return state, i

            # Randomly chose if we will be doing walk-sat or novelty search based on the value of wp
            if self.wp < random.uniform(0, 1):

                # Perform a walk sat
                state = self.walkSat.run(state)
            else:

                # Chose a random variable to flip
                random_flip = random.choice(self.variables)

                # Chose a random clause
                random_clause = random.choice(unsat_clause_list)

                # Run the novelty heuristic
                best_flip = self.novelty.run_heuristic(state, random_flip, random_clause)

                # Flip the best variable from novelty heuristic
                Utils.flip_variable(state, best_flip)

        return None, self.max_iterations

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
