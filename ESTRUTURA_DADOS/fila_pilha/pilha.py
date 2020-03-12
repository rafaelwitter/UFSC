class Pilha:

    def __init__(self, dados: []):
        self.dados = dados
    
    def empilha(self, elemento):
        self.dados.append(elemento)

    def vazia(self):
        if len(self.dados) == 0:
            return True
        else: return False

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
        else: return print("A pilha esta vazia")