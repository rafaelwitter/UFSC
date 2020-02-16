#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by Rafael Nilson Witt
"""
from Campo_Minado import CampoMinado
def main():
    n_l = int(input("Digite o numero de linhas para formar o campo minado: "))
    n_c = int(input("Digite o numero de colunas para formar o campo minado: "))
    campo = CampoMinado(n_l,n_c) #Cria o campo do tamanho desejado
    campo.criaTabuleiro() #Aqui é gerado o tabuleiro somente com 0
    campo.criaCampo() #Gera o campo(0 e -1) automaticamente e cria a nova tabela oculta com a quantia de bombas
    print(campo.contaMinas()) #Mostra quantas minas há no campo todo
    print(campo) #Representação inicial do campo
    while campo.estaJogando == True:
        campo.selecionaPosicao() #Interação
main()