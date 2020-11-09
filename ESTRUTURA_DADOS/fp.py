import heapq

class FilaDePrioridade:

    def __init__(self):
        self._fila = []

    def inserir(self, item, prioridade):
        heapq.heappush(self._fila, (item, prioridade))

    def remover(self):
        return heapq.heappop(self._fila)[-1]
    
    def __repr__(self):
        return self._fila

    def __str__(self):
        return str(self._fila)

fila = FilaDePrioridade()
fila.inserir(4,2)
fila.inserir(2,1)
print(fila)
fila.remover()
print(fila)
fila.inserir(4,1)
print(fila)
