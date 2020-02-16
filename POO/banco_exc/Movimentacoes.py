#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:08:52 2019

@author: giuffra
"""

class Movimentacao:
    def __init__(self, infoSaqueDep, valor, descricao):
        self.__informacao = infoSaqueDep
        self.__valor = valor
        self.__descricao = descricao
    
    def informarInformacao(self):
        return self.__informacao
    
    def informarValor(self):
        return self.__valor
    
    def informarDescricao(self):
        return self.__descricao
    
    