from Exercicio3 import Matrizes
def main():
    n_l_c = int(input("Digite o numero de linhas e colunas: "))
    A = Matrizes.cria_matriz_quadrada(n_l_c)
    Matrizes.le_matriz(A)
    Matrizes.imprime_matriz(A)
    print(Matrizes.tem_repetido(A))
    Matrizes.verificaPermutacao(A)
    Matrizes.verificaNulidade(A)
main()