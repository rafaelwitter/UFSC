##############################################################################################
#Dado um numero inteiro positivo verifique se o mesmo possui dois numeros consecutivos iguais#
##############################################################################################
a = int(input("Insira um numero aqui: "))
x = a % 10
y = a // 10
if x == y:
    print(x+y)
else:
    print("Não possui digitos iguais")

#################################################################################################
#Dado um numero inteiro n > 0 e as médias de n alunos, determinar quantos alunos ficaram de rec.#
#################################################################################################
n_alunos = int(input("Insira a quantia de alunos na sala: "))
tam = n_alunos
n_alunos_aprov = 0
n_alunos_reprov = 0
while tam != 0:
    media = float(input("Insira as medias dos alunos: "))
    tam -= 1
    if media >= 3.5:
        n_alunos_aprov += 1
    if media < 3.5:
        n_alunos_reprov += 1
print("A quantia de alunos que foram aprovados é" , n_alunos_aprov)
print("A quantia de alunos que foram reprovados é", n_alunos_reprov)