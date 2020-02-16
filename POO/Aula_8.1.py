######################################################
#Dado uma sequencia determine a soma de seus fatorias#
######################################################
def main():
    try:
        n = int(input("Insira um numero: "))
        n1 = int(input("Insira um numero: "))
    except(ValueError):
        n = int(input("Insira um numero inteiro: "))
        n1 = int(input("Insira um numero inteiro: "))        
    print(sum((fatorial(n), fatorial(n1))))
    
def fatorial(n):
    contador = n
    while contador != 0:
        if contador == n:
            contador -= 1
        else:
            fatorial = n * contador
            n = fatorial
            contador -= 1
    return fatorial
    
main()
