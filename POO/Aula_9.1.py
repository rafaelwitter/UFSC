###############################################
#Recebe um numero x e potencializa ao numero y#
###############################################
def main():
    x = int(input("Digite um numero para ser potencializado: "))
    y = int(input("Digite o numero de potencia: "))
    print(potencia(x,y))
def potencia(x, y):
    a = x ** y
    print(a)
main()