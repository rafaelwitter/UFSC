class Pilha:

    def __init__(self, dados: []):
        self.dados = dados
    
    def empilha(self, elemento):
        self.dados.append(elemento)
        self.printa()

    def vazia(self):
        return len(self.dados) == 0

    def desempilha(self):
        if not self.vazia():
            self.printa()
            print(self.dados.pop(-1))
            self.printa()
        elif self.vazia():
            print("Lista vazia.")

    def printa(self):
        return print(str(self.dados).replace(',', ' ').
            replace('[','').replace(']',''))