from arvora_binaria import ArvoreBinaria, Node


class ArvoreBinariaBusca(ArvoreBinaria):
    def inserir(self, elem):
        parent = None
        x = self.raiz
        while x:
            parent = x
            if elem < x.dado:
                x = x.esquerda
            else:
                x = x.direita
        if parent is None:
            self.raiz = Node(elem)
        elif elem < parent.dado:
            parent.esquerda = Node(elem)
        else:
            parent.direita = Node(elem)

    def busca(self, valor):
        return self._busca(valor, self.raiz)

    def _busca(self, valor, node):
        if node is None:
            return node
        if node.dado == valor:
            return ArvoreBinariaBusca(node)
        if valor < node.dado:
            return self._busca(valor, node.esquerda)
        return self._busca(valor, node.direita)
