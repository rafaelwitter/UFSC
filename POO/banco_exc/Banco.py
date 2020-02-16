#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:30:05 2019

@author: giuffra
"""
from Conta import Conta

class Banco:
    def __init__(self):
        self.agencia = 1234
        self.listaContas = []
        
    def criarConta(self):
        self.listaContas.append(Conta(self.agencia, len(self.listaContas) + 1))
        return "Conta Criada"
    
    def excluirConta(self, conta): 
        self.listaContas.remove(conta)
        return "Conta Removida com Sucesso"
    
    def transferir(self, conta1saque, conta2deposito, valor):
        sacou, texto = conta1saque.sacar(valor, 'transferencia para agencia '
                +str(conta2deposito.informarAgencia())+' conta '
                +str(conta2deposito.informarNroConta()))
        if (sacou):
            conta2deposito.depositar(valor, 'transferencia da agencia '
                +str(conta1saque.informarAgencia())+' conta '
                +str(conta1saque.informarNroConta()))
        else:
            return texto    
    
    