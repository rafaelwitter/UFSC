class Matriz:
    
    def __init__(self, linha, coluna):
        self.coluna = coluna
        self.linha = linha
        self.cria()
        self.matriz = []
    
    def cria(self):
        for i in range(self.linha):
            for j in range(self.coluna):
                self.matriz[i][j] = 0
    
    def atribui(self, l: int, c: int, nmr: int):
        if self.linha <= l and self.coluna <= c:
            self.matriz[l][c] = nmr


