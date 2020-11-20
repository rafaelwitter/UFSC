from ESTRUTURA_DADOS.fila_pilha.node.node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def entrar(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = Node
        else:
            self.last.next = node
            self.last = node
        if self.vazia():
            self.first = node
        self._size += 1

    def sair(self):
        if self.vazia():
            raise IndexError('Lista vazia.')
        else:
            elem = self.first.item
            self.first = self.first.next
            self._size -= 1
            return elem

    def vazia(self):
        if self._size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.vazia():
            raise IndexError("Lista vazia.")
        else:
            return self.first.item

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.vazia():
            r = ""
            pointer = self.first
            while pointer:
                r += str(pointer.item) + "\n"
                pointer.next
            return r
        raise IndexError("Lista vazia.")

    def __str__(self):
        return self.__repr__()


q = Queue()
q.entrar(2)
q.entrar(4)
q(fila)
