class Utils:

    def load_dimacs_cnf_file(self, cnf_file):
        """
        Reads and parses Dimacs CNF formatted files. Note some of this code was taken from stack-overflow

        https://stackoverflow.com/questions/28890268/parse-dimacs-cnf-file-python

        :param cnf_file: The path to the cnf file
        :return: Parsed cnf file
        """
        with open(cnf_file) as file:
            content = file.readlines()

        cnf = list()
        cnf.append(list())
        max_var = 0

        for line in content:
            tokens = line.split()
            if len(tokens) != 0 and tokens[0] not in ("p", "c", "%"):
                for token in tokens:
                    lit = int(token)
                    max_var = max(max_var, abs(lit))
                    if lit == 0:
                        cnf.append(list())
                    else:
                        cnf[-1].append(lit)

        assert len(cnf[-1]) == 0

        cnf.pop()

        return cnf, max_var
