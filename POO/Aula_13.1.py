#Escreva uma funcao que cria matriz com inputacao em todos os numeros
def main():
    n_linha = int(input("Digite numero de linhas: "))
    n_coluna = int(input("Digite numero de colunas: "))
    elem = int(input("Digite o valor da matriz: "))
    A = cria_matriz(n_linha,n_coluna,elem)
    imprime_matriz(A)
def cria_matriz(n_linha, n_coluna, elem):
    A = []
    for i in range(n_linha):
        l = [elem] * n_coluna 
        A.append(l)
    return A    
def imprime_matriz(A):
    n_linhas = len(A)
    n_colunas = len(A[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            print(A[i][j], end = ' ')
        print()
main()