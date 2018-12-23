import sys
import numpy as np


class Utils:
    """
    General re-usable utility methods
    """

    @staticmethod
    def load_dimacs_cnf_file(cnf_file):
        """
        Reads and parses a CNF Dimacs formatted file

        :param cnf_file: The location of the file to load
        :return: The parsed file
        """
        file = open(cnf_file, 'r')

        tVariables = -1
        tClauses = -1
        clause = []
        variables = []

        current_clause = []

        for line in file:
            data = line.split()

            if len(data) == 0:
                continue
            if data[0] == 'c':
                continue
            if data[0] == 'p':
                tVariables = int(data[2])
                tClauses = int(data[3])
                continue
            if data[0] == '%':
                break
            if tVariables == -1 or tClauses == -1:
                print("Error, unexpected data")
                sys.exit(0)

            for var_i in data:
                literal = int(var_i)
                if literal == 0:
                    clause.append(current_clause)
                    current_clause = []
                    continue
                var = literal
                if var < 0:
                    var = -var
                if var not in variables:
                    variables.append(var)
                current_clause.append(literal)

        if tVariables != len(variables):
            print("Unexpected number of variables in the problem")
            print("Variables", tVariables, "len: ", len(variables))
            print(variables)
            sys.exit(0)
        if tClauses != len(clause):
            print("Unexpected number of clauses in the problem")
            sys.exit(0)
        file.close()
        return [variables, clause]

    @staticmethod
    def generate_random_starting_point(variables):
        """
        Generates a random starting point
        :param variables: A list of variables
        :return: A dictionary of randomly selected variables
        """
        variable_dict = {}

        for i in variables:
            variable_dict[variables[i - 1]] = int(np.random.randint(2))
        return variable_dict

    @staticmethod
    def flip_variable(item, index):
        """
        Flips a variable in place.
        :param item: A dictionary
        :param index: An index in the dictionary to flip
        :return:
        """
        if item[index] == 0:
            item[index] = 1
        elif item[index] == 1:
            item[index] = 0
