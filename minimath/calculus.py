import re

class Calculus:
    def __init__(self, form):
        self.form = form
        self.resultForm = ""

    def _tokenize(self):
        """this will convert the formula into coeff and power of variable x"""
        formula = self.form.replace(" ", "")
        pattern = r'([+-]?\d*)x\^?(\d*)|([+-]?\d+)'
        matches = re.findall(pattern, self.form)
        tTable = []
        for i in matches:
            if i[2] != '':
                tTable.append((int(i[2]), 0))
            else:
                tTable.append((int(i[0]), int(i[1])))
        return tTable  # [(coeff, power),(coeff, power), ...] 
    
    def integrate(self):
        pass

    def differentiate(self):
        pass

    def make_function(self, string=False):
        pass

df = Calculus('-3x^2 + 3')
print(df._tokenize())

