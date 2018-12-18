import numpy as np


class GSAT:

    def run(self, formula, max_steps):
        variables = formula[0]

        for i in range(max_steps):
            best_flip = 1000000

            state = self.generate_random_starting_point(variables)

            for x in range(1000):
                solution_found, unsat_clause = self.solution_status(formula, state)

                if solution_found is True:
                    print('Solution found')
                    return state

                random_flip_index = np.random.randint(1, 20)

                # Flip variable
                self.flip_variable(state, random_flip_index)

                if unsat_clause > best_flip:
                    self.flip_variable(state, random_flip_index)

    def flip_variable(self, item, index):
        if item[index] == 0:
            item[index] = 1
        elif item[index] == 1:
            item[index] = 0

    def generate_random_starting_point(self, variables):
        variable_dict = {}

        for i in variables:
            variable_dict[variables[i - 1]] = int(np.random.randint(2))
        return variable_dict

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
            # print("UNSAT Clauses: ", unsat_clause)
            return False, unsat_clause
        return True, unsat_clause
