from node import Node
class ArvoreBinaria:
    def __init__(self):
        self.raiz = Node(None, None, None)
        self.raiz = None

    def insere_elemento(self, dado: int):
        novo_no = Node(dado, None, None) #Cria um novo item
        if self.raiz == None:
            self.raiz = novo_no
        else: #Se nao for a raiz
            atual = self.raiz
            while True:
                anterior = atual
                if dado <= atual.dado: #Insere esquerda
                    atual = atual.proximo_esquerda
                    if atual == None:
                        anterior.proximo_esquerda = novo_no
                        return
                else: #Vai para direita
                    atual = atual.proximo_direita
                    if atual == None:
                        anterior.proximo_direita = novo_no
                        return

    def __repr__(self):
        return str(self._raiz)

arvore = ArvoreBinaria(10)
arvore.insere_elemento(8)
arvore.insere_elemento(22)
print(arvore)