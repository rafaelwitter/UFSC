from fila import *

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
        ponteiro = None
        x = self.raiz
        while x:
            ponteiro = x
            if elem < x.dado:
                x = x.esquerda
            else:
                x = x.direita
        if ponteiro is None:
            self.raiz = Node(elem)
        elif elem < ponteiro.dado:
            ponteiro.esquerda = Node(elem)
        else:
            ponteiro.direita = Node(elem)

    def inserir2(self, elem):
        ponteiro = None
        self.raiz = x = nd(elem)
        while x:
            ponteiro = x
            if elem < x.value:
                x = x.left
            else:
                x = x.right
        if ponteiro is None:
            self.raiz = nd(elem)
        elif elem < self.raiz.value:
            nd(self.raiz.value, left=nd(elem))
        else:
            ponteiro = nd(self.raiz.value, right=nd(elem))

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


def monta_arvore(arvore, indc_atual, index=False, delimiter='-'):
    if arvore is None:
        return [], 0, 0, 0

     linha1 = []
    linha2 = []
    if index:
        node_repr = '{}{}{}'.format(indc_atual, delimiter, arvore)
    else:
        node_repr = str(arvore.dado)

    # direita, esquerda = arvore.pos_ordem()
    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        monta_arvore(arvore.esquerda, 2 * indc_atual + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        monta_arvore(arvore.direita, 2 * indc_atual + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        linha1.append(' ' * (l_root + 1))
        linha1.append('_' * (l_box_width - l_root))
        linha2.append(' ' * l_root + '/')
        linha2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    linha1.append(node_repr)
    linha2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        linha1.append('_' * r_root)
        linha1.append(' ' * (r_box_width - r_root + 1))
        linha2.append(' ' * r_root + '\\')
        linha2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(linha1), ''.join(linha2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


def pprint(arvore, index=False, delimiter='-'):
    lines = monta_arvore(arvore, 0, index, delimiter)[0]
    print('\n' + '\n'.join((line.rstrip() for line in lines)))


a = ArvoreBinariaBusca()
a.inserir(5)
a.inserir(20)
a.inserir(1)
a.inserir(2)
a.inserir(1421)
a.inserir(3)
a.inserir(4)
a.inserir(7)
a.inserir(9)
a.inserir(11)
a.inserir(6)
a.inserir(-1)
print(a.altura())
# a.pos_ordem()
# print(f'\nA altura da arvore criada acima é de: {a.altura()}')
# a.in_order()
# print('\n--------------')
# print('\n--------------')
# a.remove(2)
# print("apos a remoçao da raiz:")
# a.in_order()
# print(f'\n------------\nA nova raiz agora é {a.raiz}')
# print(f'A altura da arvore é de: {a.altura()} \n-----------')
pprint(a.raiz)
