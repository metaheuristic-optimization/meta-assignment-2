import random
from src.utils import Utils

"""
    An implementation of the walk sat algorithm
"""


class WalkSAT:

    def __init__(self, formula, variable):
        self.formula = formula
        self.variable = variable

    def run(self, state):
        """
        Run the walk sat algorithm as outlined below

            - Get a list of unsatisfied clauses
            - Select a random clause
            - Select a random variable from the selected clause
            - Flip the selected random variable
        :param state: The current state
        :return: The new state with the flipped variable
        """

        # Get a list of unsatisfied clauses
        _, _, unsat_clause_list = self.solution_status(self.formula, state)

        # Chose a random clause
        random_clause = random.choice(unsat_clause_list)

        # Chose a random variable from the selected clause
        random_variable_in_clause = random.choice(random_clause)

        # Flip variable. Make sure the variable is a plus value as the clause may contain negative values
        Utils.flip_variable(state, abs(random_variable_in_clause))

        return state

    def solution_status(self, instance, sol):
        """
            Check the solution status

        :param instance: The current state of variables
        :param sol: Returns
                - If the solution satisfies all clauses
                - The total number of unsatisfied clauses
                - A list of unsatisfied clauses
        :return:
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
