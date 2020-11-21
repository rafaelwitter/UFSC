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
    valores = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    arv = ArvoreBinariaBusca()
    for v in valores:
        arv.inserir(v)
    return arv


def main():
    bst = arvore_exemplo()

    print("Arvore em ordem crescente")
    bst.ordem_simetrica()
    print("\n-------------")

    print("Arvore em ordem reversa.")
    bst.pos_ordem()
    print("\n-------------")

    print("Ordem transversal")
    bst.ordem_transversal()
    print("\n-------------")

    print("Altura da arvore: ", bst.altura())
    print("-------------")

    itens_busca = [262, 2, 668, 954]
    s = ""
    for item in itens_busca:
        r = bst.busca(item)
    if r is None:
        s += str(item) + ": Não encontrado; "
    else:
        s += str(r.raiz.dado) + ": Encontrado; "
    print(s)


main()
