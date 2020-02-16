#############################################################################
# Dado um numero inteiro (n>1), imprimir sua decomposição em fatores primos,#
# indicando também a multiplicidade de cada fator                           #
#############################################################################
def main():
    n = int(input("Digite um numero maior que 1: "))
    p = 2
    multiplicidade_p = 0
    while n != 1:
        if n % p == 0:
            multiplicidade_p += 1
            n = n // p
        elif multiplicidade_p != 0:
            print("Fator", p, "com multiplicidade", multiplicidade_p)
            p += 1
            multiplicidade_p = 0
        else:
            p += 1
    if multiplicidade_p != 0:
        print("Fator", p, "com multiplicidade", multiplicidade_p)

main()