###########################################################
#Dado uma sequencia com 2 numeros inteiros e maior que 0, #
#     determine o maximo divisor comum entre eles         #
###########################################################
def main():
    n1 = int(input("Digite um numero, n1, maior que 0: "))
    n2 = int(input("Digite um numero, n2, maior que 0: "))
    M = mdc(n1, n2)
    print("O mdc(", n1, ",", n2, ") =", M)

def mdc(n1, n2):
    M = n1 #É um palpite inicial, será corrigido na proxima linha, se necessario.
    if n2 > M:
        M = n2
    while not (n1 % M == 0 and n2 % M == 0): 
        M -= 1
    return M #Neste ponto M é de fato o mdc de n1 e n2
    
main()