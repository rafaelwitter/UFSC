class Node:
    def __init__(self, dado, pe, pd):
        self.dado = dado
        self.proximo_esquerda = pe
        self.proximo_direita = pd
        
    @property
    def dado(self):
        return self.dado

    @dado.setter
    def dado(self, dado: int):
        self.dado = dado

    @property
    def proximo_esquerda(self):
        return self.proximo_esquerda

    @proximo_esquerda.setter
    def proximo_esquerda(self, dado: int):
        self.proximo_esquerda = dado

    @property
    def proximo_direita(self):
        return self.proximo_direita

    @proximo_direita.setter
    def proximo_esquerda(self, dado: int):
        self.proximo_direita = dado

    def __str__(self):
        if self.proximo_direita != None:
            if self.proximo_esquerda != None:
                return str(self.dado) + "\n" + str(self.proximo_esquerda) + "   " + str(self.proximo_direita)
        else:
                return str(self.dado) + "\n" + str(self.proximo_esquerda) + "   " + str(self.proximo_direita)

