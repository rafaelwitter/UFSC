#Copiar uma lista que o usuario digitou
def main():
    n = int(input("Digite o tamanho da lista: "))
    list = []
    for elem in range(n):
        lista = int(input("Digite um numero para lista: "))
        list.append(lista)
    for i in list:
        copia = copia_lista(list)
    print(list)
    print(copia, "essa eh uma copia.")

def copia_lista(l):
    copia = []
    for i in l:
        copia.append(i)
    return copia
main()     