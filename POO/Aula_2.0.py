####################################
#Determine se X > 0 é PAR ou ÍMPAR.#
####################################
X=int(input("Insira um número maior que 0: "))
if X % 2 == 0 and X == 2:
    print("O valor", X ,"é par.")
else:
    print("O valor", X, "é impar")

######################################
#Determine o maior numero entre A e Z#
######################################
A=int(input("Insira um numero: "))
Z=int(input("Insira um numero: "))
if A < Z:
    print(A, "é menor que", Z)
if A == Z:
    print(A, "é igual à", Z)
if A > Z:
    print(A, "é maior que", Z)

######################
#Determine se é primo#
######################
n = int(input()) 
def prime(n):

    if n < 2:
        return False
    if n > 2:
        is_Prime = True
        k=2
        while k <= n // 2:
            if n % k == 0:
                is_Prime = False
            k+=1
        return is_Prime
print(prime(n))

############################################
#Dado 3 valores reais a, b e c, determine:##
#As duas raizes, se Delta > 0             ##
#A unica raiz, se Delta = 0               ##
#Se Delta < 0                             ##
############################################
import math #IMPORTAR BIBLIOTECA MATH, PROCURAR EM DOCUMENTARIOS PYTHON
a=float(input("Entre com um valor real a: "))
b=float(input("Entre com um valor real b: "))
c=float(input("Entre com um valor real c: "))
Delta= (b**2)-(4*a*c)
print(Delta)
if Delta < 0:
    print("Não foi possivel achar sua raiz.")
if Delta == 0:
    raiz_3= (-b/(2*a))
    print(raiz_3)
if Delta > 0:
    raiz_1= (-b + math.sqrt(Delta)) / (2*a) #Math.sqrt() faz a raiz quadrada e se usasse math.floor ia arredondar
    raiz_2= (-b - math.sqrt(Delta)) / (2*a)
    print(raiz_1, "e", raiz_2)

#######################
#COMANDOS DE REPETIÇÃO#
############################################
#Eleve o numero 2 por 10 vezes usando WHILE#
############################################
i=0
while i <= 10:
    print("2 elevado a",  i, 2**i)
    i += 1
    break

#########################################################################################################
#Dado uma sequencia de numeros inteiros terminados com 0, devolva a soma dos numeros que estão na seq...#
#########################################################################################################
sum = 0
contador = 2
nmr=int(input("Insira o primeiro valor numerico para a sequencia: "))
while nmr != 0:
    sum = sum + nmr
    print("Insira o ", contador, "º o valor da sequência: ")
    nmr = int(input())
    contador += 1
print("A soma da sequência é: ", sum)

#############################################################################
#Dado uma sequencia de numeros inteiros e positivos, devolva o produto deles#
#############################################################################
produto = 1
contador = 0
tamanho = int(input("Insira o tamanho da sequencia desejada: "))
while contador < tamanho:
    num=int(input("Digite um numero para a sequencia: "))
    produto *= num
    contador +=1
print("O produto da sequencia é:", produto) 

#############################################################
#Dado um numero inteiro positivo, escreva a soma dos digitos#
#############################################################
nmr = input("Digite um número inteiro para somar seus digitos: ")
print(sum(int(i) for i in nmr))