'''
Criado por Rafael Witt 
Projeto CampoMinado 
	Prova III
'''
#Para jogar siga os passos:
#1- Criar um objeto CampoMinado informando o numeros de linhas e colunas desejada.
#2- Criar o campo com o comando cria_campo (para digitar as bombas) ou 
#   cria_campo_automatico
#3- Rodar o meto VERIFICA.
import random
import os
class CampoMinado:
    
    def __init__(self, n_linha, n_coluna):

        self.linha = n_linha
        self.coluna = n_coluna
        self.campo = []
        self.ainda_joga = True
        self.s = []
        self.jogadas = 0
        
    def cria_campo(self): #usuario cria o campo minado

        for i in range(self.linha):
            l = [0] * self.coluna

            self.campo.append(l)

        return (self.campo)
    
    def cria_campo_automatico(self): #cria o campo automaticamente
        for i in range(self.linha):
            l = [0] * self.coluna
            self.campo.append(l)
        for i in range(len(self.campo)):
            for j in range(len(self.campo[0])):
                l = random.randrange(-1,1)
                self.campo[i][j] = l
        self.define_jogadas()

        return (self.campo)
    
    def define_jogadas(self): #
        for i in range(len(self.campo)):
            for j in range(len(self.campo[0])):

                if self.campo[i][j] == 0:
                    self.jogadas += 1

    def le_campo(self):

        print("para adicionar uma bomba entre com o valor -1 e para os esṕacos livre entre com o valor 0.")
        for i in range(len(self.campo)):
            for j in range(len(self.campo[0])):
                print("posicao ", i, j,":", end="")

                elem = int(input())
                if elem == 0:
                    self.jogadas += 1

                if elem == -1 or elem == 0:
                    self.campo[i][j] = elem

                else:
                    print("entre com um valor valido: ")

                    elem2 = int(input())
                    if elem2 == -1 or elem2 == 0:
                        self.campo[i][j] = elem2

        return self.jogadas
                    
    def jogadas_disponiveis(self): #diz quantas bombas tem no campo
        jogadas = 0
        for i in range(len(self.campo)):
            for j in range(len(self.campo[0])):
                if self.campo[i][j] == -1:
                    jogadas += 1
                    
        self.jogadas = jogadas
        return self.jogadas
                        
    def imprime_campo(self):

        for i in range(len(self.campo)):
            for j in range(len(self.campo[0])):
                print("%10d" % self.campo[i][j], end='')
            print()

    def conta_minas_ao_redor(self, campo, i, j): 

        contador = 0
        n_linha = len(self.campo)
        n_coluna = len(self.campo[0])

        if i - 1 >= 0 and campo[i - 1][j] is -1:
            contador += 1

        if i - 1 >= 0 and j + 1 < n_coluna and campo[i - 1][j + 1] is -1:
            contador += 1

        if j + 1 < n_coluna and campo[i][j + 1] is -1:
            contador += 1

        if i + 1 < n_linha and j + 1 < n_coluna and campo[i + 1][j + 1] is -1:
            contador += 1

        if i + 1 < n_linha and campo[i + 1][j] is -1:
            contador += 1

        if i + 1 < n_linha and j - 1 >= 0 and campo[i + 1][j - 1] is -1:
            contador += 1

        if j - 1 >= 0 and campo[i][j - 1] is -1:
            contador += 1

        if i - 1 >= 0 and j - 1 >= 0 and campo[i - 1][j - 1] is -1:
            contador += 1

        return contador

    def fazer_jogada(self): #funcao para o usuario jogar
        
        posicao_linha = int(input("Entre com a posicao da linha que deseja selecionar: "))
        posicao_coluna = int(input("Entre com a posicao da coluna que deseja selecionar: "))

        if self.campo[posicao_linha][posicao_coluna] == -1:            
            self.ainda_joga = False
            self.imprime_campo()
            print(" BOMBA EM -1!! Fim de jogo!")

        else:                  
            self.vira_posicao(posicao_linha, posicao_coluna)
            print(self)
            self.jogadas -= 1

        if self.jogadas == 0:
            print("VOCE GANHOU, OS VALORES EM X REPRESENTAM BOMBAS")
            self.ainda_joga = False
            
    def verifica(self): #verifica se é uma bomba ou posicao livre
        
        self.campo_oculto()
        print(self)
        while self.ainda_joga == True:
            self.fazer_jogada()

    def campo_oculto(self): #oculta as posicoes livres e bombas
        
        for i in range(len(self.campo)):
            l = ['x']* len(self.campo[0])
            self.s.append(l)

        return self.s
            
    def vira_posicao(self, posicao_linha, posicao_coluna):
        
        self.s[posicao_linha][posicao_coluna] = self.conta_minas_ao_redor(self.campo,posicao_linha,posicao_coluna)

        return self.s

    def __str__(self):
        
        s = ''
        for i in range(len(self.campo)):
            s += '\n'
            for j in range(len(self.campo[0])):
                s += '%10s' %str(self.s[i][j])

        return s

def main():
    os.system('pause')
    i = int(input("Digite quantas linhas possuem o campo: "))
    j = int(input("Digite quantas colunas possuem o campo: "))
    
    c1 = CampoMinado(i,j)
    
    criacao = int(input("Você deseja criar seu campo (1) ou deseja que o computador faça isso? (0): "))

    if criacao == 0:
        c1.cria_campo_automatico()
        c1.verifica()

    elif criacao == 1:
        c1.cria_campo()
        c1.le_campo()
        c1.verifica()

    else: print("Opção inválida.")
    
if __name__ == "__main__":
    main()

