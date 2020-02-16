class Matrizes:
    def conta_minas(A, i, j): #Conta minas do campo minado.
        contador = 0
        n_linhas = len(A)
        n_colunas = len(A[0])
        if i - 1 >= 0 and A[i-1][j] is -1:
            contador += 1
        if i - 1 >= 0 and j + 1 < n_colunas and A[i-1][j+1] is -1:
            contador += 1
        if j + 1 < n_colunas and A[i][j+1] is -1:
            contador += 1
        if i + 1 < n_linhas and j + 1 < n_colunas and A[i+1][j+1] is -1:
           contador += 1
        if i + 1 < n_linhas and A[i+1][j] is -1:
            contador += 1
        if i + 1 < n_linhas and j - 1 >= 0 and A[i+1][j-1] is -1:
            contador += 1
        if j - 1 >= 0 and A[i][j-1] is -1:
            contador += 1
        if i - 1 >= 0 and j - 1 >= 0 and A[i-1][j-1] is -1:
            contador += 1
        print(contador)
    def quadradoMagico(A): #Exercicio_4 Dizemos que uma matriz quadrada inteira é um quadrado mágico se a
        #soma dos elementos de cada linha, a soma dos elementos de cada coluna e a soma dos elementos das
        #diagonais principal e secundária são todas iguais.
        n_linhas = len(A)
        n_colunas = len(A[0])
        valores_somados = []

        for i in range(n_linhas): #soma das linhas
            soma_linhas = 0
            for j in range(n_colunas):
                soma_linhas +=  A[i][j]
            valores_somados.append(soma_linhas)

        for j in range(n_colunas): #soma das colunas
            soma_colunas = 0
            for i in range(n_linhas):
                soma_colunas += A[i][j]
            valores_somados.append(soma_colunas)

        soma_diagonal_principal = 0
        for i in range(n_linhas): #soma da diagonal principal
            soma_diagonal_principal += A[i][i]
        valores_somados.append(soma_diagonal_principal)

        soma_diagonal_secundaria = 0
        i = 0
        j = n_colunas - 1
        while i < n_linhas: #soma da diagonal secundaria
            soma_diagonal_secundaria += A[i][j]
            i += 1
            j -= 1
        valores_somados.append(soma_diagonal_secundaria)
        print(valores_somados)
        eh_qd_magico = True
        index = 1
        while eh_qd_magico and index < len(valores_somados): #verifica se eh qdd mag
            if valores_somados[index] != valores_somados[0]: #todos os valores da lista tem q ser iguais, entao da pra ficar comparando sempre com o mesmo
                eh_qd_magico = False
            index += 1
        print(eh_qd_magico)
    def verificaNulidade(A): #Exercicio_2 Verifca se tem linhas e/ou colunas nulas
        cont_linha_nula = 0
        cont_coluna_nula = 0
        n_linhas = len(A)
        n_colunas = len(A[0])
        for i in range(n_linhas):
            n = True
            for j in range(n_colunas):
                if A[i][j] != 0:
                    n = False
            if n is True:
                cont_linha_nula += 1
        print(('Existem {} linhas nulas').format(cont_linha_nula))
        for j in range(n_colunas):
            k = True
            for i in range(n_linhas):
                if A[i][j] != 0:
                    k = False
            if k is True:
                cont_coluna_nula += 1
        print(('Existem {} colunas nulas').format(cont_coluna_nula))
    def verificaPermutacao(A): #Exercicio_3 lista_3 verificar se ocorre permutação
        linhas = len(A)
        colunas = len(A[0])
        cont1 = 0
        cont2 = 0
        for i in range(linhas):
            for j in range(colunas):
                if A[i][j] == 1:
                    cont1 += 1
                if A[j][i] == 0:
                    cont2 += 1
            if cont1 == 1 and cont2 == (linhas-1):
                print("Deu bom")
            else:
                print("Deu ruim")

            cont1 = 0
            cont2 = 0

        return print("Deu bom")
    def tem_repetido(A): #Exercicio_1 Lunardi resolução menos complexa
        elemento = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                elemento.append(A[i][j])
        for nmr in elemento:
            if elemento.count(nmr) > int(1):
                return True
            else: return False             
    def getRepeticao(A):  # Exercicio_1 lista_3 Obter_Repeticoes
        elemento = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                elemento.append(A[i][j])
        elemento = sorted(elemento, key=int)
        repeticao = []
        for nmr in elemento:
            if elemento.count(nmr) <= int(1):
                pass
            else: repeticao.append(nmr)
            if repeticao.count(nmr) > int(1):
                repeticao.remove(nmr) 
        for x in repeticao:   
            print(('O elemento {} se repete {} vezes.').format(x, elemento.count(x)))
    def multiplica_matriz(A, B):  # Funcao para multiplicar duas matrizes
        nmr_linha = len(A)
        nmr_coluna = len(A[0])
        C = cria_matriz(nmr_linha, nmr_coluna)
        for i in range(nmr_linha):
            for j in range(nmr_coluna):
                valor = 0
                for k in range(len(B[0])):
                    valor += (A[i][k] * B[k][j])
                C[i][j] = valor
        return C
    def soma_matriz(A, B):  # Funcao para somar duas matrizes
    # As matrizes obrigatoriamente precisam ser quadradas, sem excecao
        nmr_linha = len(A)  # Conta quantas linhas existem
        nmr_coluna = len(A[0])  # Conta quantos elementos têm em uma linha
        C = Matrizes.cria_matriz(nmr_linha, nmr_coluna)
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print("Não é possivel somar as matrizes. Elas não são quadradas.")     
        else:
            for i in range(nmr_linha):
                for j in range(nmr_coluna):
                    C[i][j] = A[i][j] + B[i][j]
            Matrizes.imprime_matriz(C)
    def imprime_matriz(A):  # O nome ja diz tudo, PRINT(MATRIZ)
        n_linhas = len(A)
        n_colunas = len(A[0])
        for i in range(n_linhas):
            for j in range(n_colunas):
                print("%5d" % A[i][j], end=' ')
            print()          
    def le_matriz(A):  # Funcao para deixar a matriz em forma de matriz
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                print("Entre com o valor para A[", i,
                      "][", j, "] da matriz: ", end="")
                elem = int(input())
                A[i][j] = elem
    def cria_matriz_quadrada(n_linha_coluna):  # Funcao para criar a matriz, cria em listas
        A = []
        for i in range(n_linha_coluna):
            l = [0] * n_linha_coluna
            A.append(l)
        return A
    def cria_matriz(n_linha, n_coluna):  # Funcao para criar a matriz, cria em listas

        A = []
        for i in range(n_linha):
            l = [0] * n_coluna
            A.append(l)
        return A