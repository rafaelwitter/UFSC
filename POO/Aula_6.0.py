########################################
#Esqueleto programa python by professor#
########################################
def main():
    n = int(input("Insira o numero para contagem progressiva: "))
    contagem_prog(n)

def contagem_prog(n):
    for i in range(n):
        print(i)
    print("Bum!")
def comp_numb():
    x = int(input("Insira um numero: "))
    y=int(input("Insira outro numero: "))
    
    if x > y:
        print(x, "é maior que", y)
    elif x < y:
        print(x, "é menor que", y)
    else:
        print("Os numeros são iguais.")

main()