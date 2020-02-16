a = input("Digite uma frase: ")
for i in a:
    print(('caracter {} no valor numerico {}').format(i,ord(i)))

class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome
class Circulo(FiguraGeometrica):
    def __init__(self, nome):
        super().__init__(nome)
        self.area = float
        self.raio = int(input("Digite o raio: "))
    def calcularArea(self):
        self.area = self.raio**2 * 3,1416
        return str(self.area)

c1 = Circulo("Circulo")
print(c1.calcularArea())