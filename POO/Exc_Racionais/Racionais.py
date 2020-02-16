class Racionais:
    def __init__(self, n=0, d=1):
        self.num = n
        self.den = d

    def __str__(self):
        return "%d/%d"%(self.num, self.den)