import random
from arvora_binaria import ArvoreBinariaBusca


def random_tree(size=10):
    random.seed(5)
    values = random.sample(range(1, 1000), size)
    arv = ArvoreBinariaBusca()
    for v in values:
        arv.inserir(v)
    return arv


def arvore_exemplo():
    valores = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 90, 100]
    arv = ArvoreBinariaBusca()
    for v in valores:
        arv.inserir(v)
    return arv


def teste_arvore_exemplo():
    bst = arvore_exemplo()

    print("Arvore em ordem crescente")
    bst.in_order()
    print("\n-------------")

    # print("Arvore em ordem reversa.")
    # bst.pos_ordem()
    # print("\n-------------")

    print("Ordem transversal")
    bst.ordem_transversal()
    print("\n-------------")

    print("Altura da arvore: ", bst.altura())
    print("-------------")

    print("Máximo:", bst.max(), " Mínimo: ", bst.min())
    print("-------------")

    itens_busca = [11, 22, 54, 89]
    s = ""
    for item in itens_busca:
        r = bst.busca(item)
        if r is None:
            s += str(item) + ": Não encontrado; "
        else:
            s += str(r.raiz.dado) + ": Encontrado; "
    print(s)
    print("-------------")

    v = 61
    bst.remove(v)
    print("Valor {} removido com sucesso".format(v))
    print("-------------")

    print("Arvore em ordem crescente apos remoção")
    bst.in_order()
    print("\n-------------")

    print("Arvore em ordem reversa apos remoção")
    bst.pos_ordem()
    print("\n-------------")

    print("Ordem transversal apos remoção")
    bst.ordem_transversal()
    print("\n-------------")

    print("Altura da arvore: ", bst.altura())
    print("-------------")


teste_arvore_exemplo()



