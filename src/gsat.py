import numpy as np


class GSAT:

    def run(self, formula, max_steps):
        variables = formula[0]
        best_state = self.generate_random_starting_point(variables)

        for i in range(max_steps):
            best_flip = 1000000
            tmp_state = best_state.copy()
            current_best = tmp_state.copy()

            for x in range(1000):
                tmp = tmp_state.copy()

                random_flip_index = np.random.randint(1, 20)

                # Flip variable
                if tmp[random_flip_index] == 0:
                    tmp[random_flip_index] = 1
                elif tmp[random_flip_index] == 1:
                    tmp[random_flip_index] = 0

                solution_found, unsat_clause = self.solution_status(formula, tmp)

                if solution_found is True:
                    print('Solution found')
                    return tmp

                if unsat_clause < best_flip:
                    best_flip = unsat_clause
                    current_best = tmp.copy()

            best_state = current_best.copy()

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
