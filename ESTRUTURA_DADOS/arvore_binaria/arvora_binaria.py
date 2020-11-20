from node import Node


class ArvoreBinaria:
    def __init__(self, data=None, node=None):
        if node:
            self.raiz = node
        elif data:
            node = Node(data)
            self.raiz = node
        else:
            self.raiz = data

    def percurso_simetrico(self, node=None):
        """return symmetric values"""
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.percurso_simetrico(node.esquerda)
        print(node, end=' ')
        if node.direita:
            self.percurso_simetrico(node.direita)

    def percurso_posordem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.percurso_posordem(node.esquerda)
        if node.direita:
            self.percurso_posordem(node.direita)
        print(node)

    def altura(self, node=None):
        if node is None:
            node = self.raiz
        h_esq = 0
        if node.esquerda:
            h_esq = self.altura(node.esquerda)
        h_dir = 0
        if node.direita:
            h_dir = self.altura(node.direita)
        if h_dir > h_esq:
            return h_dir + 1
        return h_esq + 1


if __name__ == "__main__":
    array = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    arvore = ArvoreBinaria(61)
