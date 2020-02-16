##########################################################################################
#Dado dois numeros naturais, n > 0 e m > 0. Determine todos os pares de numeros inteiros,#
#                            x, y tais que 0 > x < n                                     #
##########################################################################################
def main():
    n = int(input("Digite um valor para n: "))
    m = int(input("Digite um valor para m: "))
    maximo = (-m)**2
    x_max = -1
    y_max = -1

    #gera todos os pares (x,y) tais que 0 <= k <= n e 0 <=y <=m
    for x in range(0, n+1): 
        for y in range(0, m+1):
             #encontra o par (x,y) que maximixa x*y - y**2 + y
             res = x*y - y**2 + y
             if res > maximo:
                 maximo = res
                 x_max = x
                 y_max = y
    print("O par que maximiza a expressao eh:","(",x,y,")",", o valor maximo eh: ", maximo)
main()