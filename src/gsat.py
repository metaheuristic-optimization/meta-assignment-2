import random

class GSAT:

    def run(self, formula, max_steps):

        print(formula[0])
        starting = self.generate_random_starting_point(formula[0])

        print(starting)
        ## for i in range(max_steps):

        # return self.solution_status(formula, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 0})

    def generate_random_starting_point(self, vars):
        dict = {}

        for i in vars:
            dict[vars[i - 1]] = random.getrandbits(1)

        return dict



    def solution_status(self, instance, sol):
        print(instance)
        clause = instance[1]
        unsat_clause = 0
        for clause_i in clause:
            print(clause_i)
            cStatus = False
            tmp = []
            for var in clause_i:
                print(clause_i)
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
            print("UNSAT Clauses: ", unsat_clause)
            return False
        return True
