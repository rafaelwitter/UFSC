#####################################################
#Retorna True se numero == primo e False se != primo#
#####################################################
def main():
    n = int(input("Insira o tamanho da sequencia: "))
    for i in range(1, n+1):
        nmr = int(input("Digita ai fdp: "))
        if eh_Primo(nmr) == True:
            print(eh_Primo(nmr), nmr)
        else:
            print(eh_Primo(nmr), nmr)
    print(eh_Primo(n))
def eh_Primo(n):
    contador = 0
    div = 1
    while div <= n:
        if n % div == 0:
            contador += 1
        div += 1   
    if contador == 2:
        return True
    else:
        return False

main()