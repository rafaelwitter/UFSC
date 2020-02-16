#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:59:44 2019

@author: giuffra
"""
from Movimentacoes import Movimentacao

class Conta:
    def __init__(self, ag, nro, senha=1234):
        self.agencia = ag
        self.nroConta = nro
        self.saldo = 0
        self.senha = senha
        self.listaMov = []
        
    def informarAgencia(self):
        return self.agencia
    
    def informarNroConta(self):
        return self.nroConta
    
    def informarSaldo(self):
        return print(self.saldo)
    
    def informarSeSaldoNegativo(self):
        if (self.saldo < 0):
            return True
        else:
            return False
        
    def informarSenha(self):
        return self.senha
    
    def trocarSenha(self, senhaNova):
        self.senha = senhaNova
        
    def sacar(self, valor, tipo):
        if (valor < self.saldo):
            self.saldo = self.saldo - valor
            mov = Movimentacao("saque", valor, tipo)
            self.listaMov.append(mov)
            return True, "O saque foi realizado com sucesso"
        else:
            return False, "O saldo é insuficiente"
        
    def depositar(self, valor, tipo):
        self.saldo = self.saldo + valor
        mov = Movimentacao("deposito", valor, tipo)
        self.listaMov.append(mov)
        return True
    
    def emitirExtrato(self):
        for elem in self.listaMov:
            print(elem.informarInformacao(), " ", elem.informarValor(), " ", elem.informarDescricao())
        
    def __eq__(self, conta):    
        return self.nroConta == conta.nroConta
class ContaCorrente(Conta):
    def __init__(self,ag, nro, chequeEspecial, limiteSaqueDiario, senha=1234):
        super().__init__(ag,nro)
        self.chequeEspecial = chequeEspecial
        self.limiteSaqueDiario = limiteSaqueDiario
    def saca(self,valor,tipo):
        if self.limiteSaqueDiario > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.limiteSaqueDiario -= valor
            mov = Movimentacao()
            mov = Movimentacao("saque", valor, tipo)
            self.listaMov.append(mov)
            return True, "O saque foi realizado com sucesso"
        elif self.limiteSaqueDiario == 0:
            return False, "O limite diario de saque foi extrapolado."
        elif valor > self.saldo and self.limiteSaqueDiario > 0:
            if self.saldo == 0:
                self.chequeEspecial -= valor
                self.limiteSaqueDiario -= valor
            if self.saldo > 0:
                print(self.chequeEspecial, "saldo cheque inicial.")
                self.chequeEspecial += (self.saldo - valor)
                self.saldo += (self.saldo - valor + 10)
                self.limiteSaqueDiario -= valor
                print(self.chequeEspecial, "saldo cheque final.")
    def verificaLimiteSaque(self):
        return print(self.limiteSaqueDiario, "este é seu limite disponível para saque hoje.")    