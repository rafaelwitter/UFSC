from collections import deque

RAIZ = "raiz"


class Node:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)


class ArvoreBinaria:
    def __init__(self, data=None, node=None):
        if node:
            self.raiz = node
        elif data:
            node = Node(data)
            self.raiz = node
        else:
            self.raiz = data

    def ordem_simetrica(self, node=None):
        """retorna os valores simétricos"""
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.ordem_simetrica(node.esquerda)
        print(node, end=' ')
        if node.direita:
            self.ordem_simetrica(node.direita)

    def pos_ordem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.pos_ordem(node.esquerda)
        if node.direita:
            self.pos_ordem(node.direita)
        print(node, end=' ')

    def altura(self, node=None):
        """retorna a altura da arvore. O caminho ate sua folha mais extensa"""
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

    def ordem_transversal(self, node=RAIZ):
        """Retorna os valores dos níveis das arvores"""
        if node == RAIZ:
            node = self.raiz
            fila = deque()
            fila.append(node)
        while len(fila):
            node = fila.popleft()
            if node.esquerda:
                fila.append(node.esquerda)
            if node.direita:
                fila.append(node.direita)
            print(node, end=" ")


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
