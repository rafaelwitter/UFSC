#PROBLEMA 1

# somar dois numeros inteiros, inseridos pelo usuario
n1 = int(input("Poem um numero: "))
n2 = int(input("Poem outro: "))
print(n1, ", n1")
print(n2, ", n2")
print(n1+n2)

#concatene é somar string
n3 = str(input("Uma string: "))
n4 = str(input("Outra string: "))
concatene = n3 + n4
print(concatene)

#PROBLEMA 2

#Escreva a tabela verdade para os operadores lógicos AND e OR
A = True #bool(input("True or False: "))
B = False #bool(input("True or False: "))
C = A and B
D = A or B
print("A é:", A, ", B é: ", B)
print(C, D)
if A is True and B is True:
    print("Ambos são verdadeiros")
if A is True and B is False:
    print("A é verdade")
    print("B é falso")