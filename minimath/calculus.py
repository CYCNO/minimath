# don't use this in production, you have been warned

import re

class Calculus:
    def __init__(self):
        pass

    @staticmethod
    def _tokenize(formula):
        """this will convert the formula floato coeff and power of variable x"""
        formula = formula.replace(" ", "")
        pattern = r'([+-]?\d+(?:\.\d+)?)x(?:\^?(\d+(?:\.\d+)?))?|([+-]?\d+(?:\.\d+)?)' 
        matches = re.findall(pattern, formula)
        tTable = []
        for i in matches:
            if i[2] == '':
                if i[1]!="":
                    tTable.append([float(i[0]), float(i[1])])
                else:
                    tTable.append([float(i[0]), 1])
            else:
                tTable.append([float(i[2]), 0])
        return tTable  # [(coeff, power),(coeff, power), ...] 

    def differentiate(self, formula):
        tTable = self._tokenize(formula)
        # convert the table of coeff and power for differntiation
        for i in range(len(tTable)):
            tTable[i][0] = tTable[i][0] * tTable[i][1]
            tTable[i][1] = tTable[i][1] - 1

        # let's make the function string
        resultForm = ""
        for i in tTable:
            if i[0] != 0:
                resultForm += "+" if i[0] > 0 else ""
                resultForm += f"{i[0]}x^{i[1]} " if i[1] != 0 else f"{i[0]}"
        return resultForm

    def integrate(self, formula, digits=4):
        tTable = self._tokenize(formula)
        # convert the table of coeff and power for differntiation
        for i in range(len(tTable)):
            tTable[i][0] = round(tTable[i][0] / (tTable[i][1] + 1), digits)
            tTable[i][1] = round(tTable[i][1] + 1, digits)

        # let's make the function string
        resultForm = ""
        for i in tTable:
            if i[0] != 0:
                resultForm += "+" if i[0] > 0 else ""
                resultForm += f"{i[0]}x^{i[1]} "

        return resultForm

