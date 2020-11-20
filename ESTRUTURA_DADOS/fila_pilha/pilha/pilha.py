from ESTRUTURA_DADOS.fila_pilha.node.node import Node


# insert na pilha
# remover da pilha
# observar o top da pilha
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # return o top sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """Return o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.item) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


p = Stack()
p.push(5)
print(p)
