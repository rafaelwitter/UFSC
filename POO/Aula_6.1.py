####################################################################################
#Faça um programa que lê um numero inteiro n (n>0) e, para cada número entre 1 e n,#
#           indique se ele é a soma de dois numeros primos                         #
#####################################################################################
def main():
    n = int(input("Digite um valor maior que 0: "))

    k = 1
    while k <= n:
        l = Eh_soma_de_dois_numeros_primos(k) 
        if l[0] == True:
            print (k, "é soma de dois numero primos, pois", l[1], "+", l[2], "=", k, "são primos" )
        else:
            print (k, "nao é soma de dois numeros primos.")
        k += 1
        
def primo (n):
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

def Eh_soma_de_dois_numeros_primos(k):
    n1 = k
    n2 = 0
    prova_n1 = -1 #valor qualquer para q as variaveis estejam definidas
    prova_n2 = -1

    dois_primos = False
    
    while n2 <= k:
        if primo(n1) == True and primo(n2) == True:
            dois_primos = True
            prova_n1 = n1
            prova_n2 = n2
        n2 += 1
        n1 -= 1
        
    l = [dois_primos, prova_n1, prova_n2]
    return l
main()
