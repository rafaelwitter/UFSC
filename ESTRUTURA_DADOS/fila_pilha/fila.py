class Fila:
    def __init__(self, dados: []):
        if type(dados) == list:
            self.dados = dados
            print(self.dados)
        else:
            return print("Adicione uma lista.")

    def insere(self, elemento):
        self.dados.append(elemento)
        print(self.dados)
    
    def retira(self):
        if self.vazia() is not True:
            print(self.dados.pop(0))
            print(self.dados)

    def vazia(self):
        if len(self.dados) == int(0):
            print('A fila esta vazia.')
            return True
        else:
            return False
            

    