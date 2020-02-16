import random
class CampoMinado:
    def __init__(self,nro_linha,nro_coluna):
        self.nro_linha = nro_linha
        self.nro_coluna = nro_coluna
    def cria_campo_minado(n_linha, n_coluna):  # Cria tabuleiro
        '''
        Essa funçao cria um tabuleiro de campo minado com todos os elementos iguais a 0
        '''
        A = []
        for i in range(n_linha):
            l = [0] * n_coluna
            A.append(l)
        return A
    
    def le_matriz(A):  # Cria bombas
        '''
        Essa função serve para criar as bombas do tabuleiro.
        '''
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                elem = random.randrange(-1,1)
                A[i][j] = elem
    
    def imprime_matriz(A):  # Imprime o tabuleiro
        n_linhas = len(A)
        n_colunas = len(A[0])
        for i in range(n_linhas):
            for j in range(n_colunas):
                print("%5d" % A[i][j], end=' ')
            print()  
    
    def conta_minas(A): # Conta quantas minas há no tabuleiro.
        contador = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    pass
                elif A[i][j] == -1:
                    contador += 1
        return print('existem', contador, 'bombas no tabuleiro.')
    
    def verificaBomba(A): # Verifica se a posição escolhida é bomba
        '''
        Nessa função é perguntado ao usuario que posição do tabuleiro ele deseja virar
        se é bomba retorna o valor True, se não é retorna False
        '''
        eh_bomba = False
        i = int(input("Digite a posiçao do elemento na linha: "))
        j = int(input("Digite a posiçao do elemento na coluna: "))
        if A[i][j] == -1:
            eh_bomba = True
        elif A[i][j] == 0:
            A[i][j] = 1
    
    def jogo(A):
        CampoMinado.verificaBomba(A)
        while CampoMinado.verificaBomba(A)== False:
            CampoMinado.verificaBomba(A)        
            return CampoMinado.imprime_matriz(A)
    def verifica_redor(A): # Conta quantas minas há envolta do numero 0
        if verificaBomba(A) == False:
            pass
        
def main():
    A = CampoMinado.cria_campo_minado(5,5)
    CampoMinado.le_matriz(A)
    CampoMinado.imprime_matriz(A)
    CampoMinado.conta_minas(A)
    CampoMinado.jogo(A)

main()