class Matriz:
    """
    Uma matriz com tipos abstratos de dados.
    """
    def __init__(self, linha, coluna):
        self.coluna = coluna
        self.linha = linha
        self.matriz = []
        self.cria()
    
    def cria(self):
        for i in range(self.linha):
            l = [0] * self.coluna
            self.matriz.append(l)
            for j in range(self.coluna):
                self.matriz[i][j] = 0
    
    def atribui(self, l: int, c: int, nmr: int):
        if l <= self.linha and c <= self.coluna:
            self.matriz[l][c] = nmr
    
    def __str__(self):
        print(str(self.matriz))


def main():
    matriz = Matriz(3,3)
    matriz.atribui(1,2,3)
    print(matriz)
main()
