import random
from arvoreB_busca import *

random.seed(77)
values = random.sample(range(1,1000), 42)

bst = ArvoreBinariaBusca()
for v in values:
    bst.inserir(v)

bst.percurso_simetrico()

itens_busca = [30, 90, 543, 300, 4, 532, 23, 1432]
for item in itens_busca:
    r = bst.busca(item)
    if r is None:
        print(item, ": Não encontrado.")
    else:
        print(r.raiz.dado, ": Encontrado")