from ESTRUTURA_DADOS.arvore_binaria.fila import Queue

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

    def in_order(self, node=None):
        """retorna da menor folha para a maior. Ordem crescente"""
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.in_order(node.esquerda)
        print(node, end=' ')
        if node.direita:
            self.in_order(node.direita)

    def pos_ordem(self, node=None):
        """Percorre a esquerda, depois a direita entao visita a raiz"""
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
        h_dir = 0
        if node.esquerda:
            h_esq = self.altura(node.esquerda)
        if node.direita:
            h_dir = self.altura(node.direita)
        if h_dir > h_esq:
            return h_dir + 1
        return h_esq + 1

    def ordem_transversal(self, node=RAIZ):
        """Retorna os valores dos níveis das arvores"""
        if node == RAIZ:
            node = self.raiz
        fila = Queue()
        fila.push(node)
        while len(fila):
            node = fila.pop()
            if node.esquerda:
                fila.push(node.esquerda)
            if node.direita:
                fila.push(node.direita)
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

    def min(self, node=RAIZ):
        if node == RAIZ:
            node = self.raiz
        while node.esquerda:
            node = node.esquerda
        return node.dado

    def max(self, valor=RAIZ):
        if valor == RAIZ:
            node = self.raiz
        while node.direita:
            node = node.direita
        return node.dado

    def remove(self, valor, node=RAIZ):
        # Se for o valor padrão, executa a partir da raiz
        if node == RAIZ:
            node = self.raiz
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if valor < node.dado:
            node.esquerda = self.remove(valor, node.esquerda)
        # Se o valor for maior, desce à direita
        elif valor > node.dado:
            node.direita = self.remove(valor, node.direita)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                # Substituto é o sucessor do valor a ser removido
                substituto = self.min(node.direita)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.dado = substituto
                # Depois, remove o substituto da subárvore à direita
                node.direita = self.remove(substituto, node.direita)
        return node
