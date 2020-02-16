####################
# Estudando funções#
####################
####################
#Entendendo funções#
####################
def soma(x,y):
    '''
    Insira um numero x e y, para que seja feita a soma dos mesmos
    '''
    return(x+y)
def multi(z,w):
    '''
    Recebe dois numeros inteiros e multiplica-os
    '''
    return z * w
print(soma(4,5))
print(multi(5,5))

def fatorial(a):
    '''
    Realiza o fatorial de um numero inteiro
    '''
    fat = 1
    while a >= 1:
        fat *= a
        a -= 1
    return fat
print(fatorial(5))

###################################################################################################
#Escreva uma função que recebe dois numeros inteiros, e faça o coeficiente binomial deles usando a#
#                          função fatorial ja escrita                                             #
###################################################################################################
def coef_binomial(m, n):
    '''
    Recebe dois numeros inteiros m>=0 e n>= 0 e m>n
    Devolve o coeficiente binomail de m e n
    '''
    return fatorial(m)//(fatorial(m-n)) * fatorial(n)
print(coef_binomial(5,3))

#############################################################################################
#Escreva uma funçao que lê um numero inteiro k>0 e imprime com k linhas do triang. de Pascal#
#############################################################################################
def triangulo_pascal(k):
    i = 0
    while i < k:
        #imprima linha i do triangulo de pascal
        m = i
        n = 0
        while n <= m:
            print(coef_binomial(m,n), end = " ")
            n+=1
        print()
        #---------------------------------------
        i += 1
k=int(input("Entre com o numero de linhas do triangulo de pascal: "))
triangulo_pascal(k)