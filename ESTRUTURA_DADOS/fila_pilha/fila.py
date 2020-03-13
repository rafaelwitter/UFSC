class Fila:
    def __init__(self, dados: []):
        if type(dados) == list:
            self.dados = dados
            self.printa()
        else:
            return print("Adicione uma lista.")

    def insere(self, elemento):
        self.dados.append(elemento)
        self.printa()
    
    def retira(self):
        if self.vazia():
            print('Lista vazia.')
        else:
            print(self.dados.pop(0), "Eliminado")
            if self.vazia():
                print("A fila acabou.")
            else: self.printa()

    def vazia(self):
        return len(self.dados) == 0

    def printa(self):
        return print(str(self.dados).replace(',', ' ').
            replace('[','').replace(']',''))

    