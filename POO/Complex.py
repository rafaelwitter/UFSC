class Complex:
    def __init__(self, a=0, bi=0):
        self.a = a
        self.bi = bi
    
    def __str__(self):
        s = str(self.a) + ' + ' + str(self.bi) + 'i'
        return s
    
    def somaComplex(self, c):
        parte_real = self.a + c.a
        parte_imaginaria = (self.bi + c.bi) 
        soma = Complex(parte_real, parte_imaginaria)
        return soma

    def __add__(self, c):
        C_novo = Complex()
        C_novo.a = self.a + c.a
        C_novo.bi = self.bi + c.bi
        return C_novo

    def subtraiComplex(self, c):
        parte_real = self.a - c.a
        parte_imaginaria = (self.bi - c.bi) 
        sub = Complex(parte_real, parte_imaginaria)
        return sub

    def __sub__(self, c):
        c_sub = Complex()
        c_sub.a = self.a - c.a
        c_sub.bi = self.bi - c.bi
        return c_sub


    def multiplicaComplex(self, c):
        parte_real = (self.a*c.a) - (self.bi*c.bi)
        parte_imaginaria = ((self.a*c.bi) + (c.a*self.bi)) 
        mult = Complex(parte_real, parte_imaginaria)
        return mult

    def __mul__(self, c):
        c_mult = Complex()
        c_mult.a = (self.a*c.a) - (self.bi*c.bi)
        c_mult.bi = ((self.a*c.bi) + (c.a*self.bi)) 
        return c_mult


def main():
    c1 = Complex(4, 5.4)
    c2 = Complex(4.5, 7.2)
    print(c1)
    print(c2)
    c3 = c2.somaComplex(c1)
    print(c3)
    


main()