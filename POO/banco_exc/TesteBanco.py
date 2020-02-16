#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:29:40 2019

@author: giuffra
"""

from Banco import Banco

banco = Banco()

print(banco.criarConta())
print(banco.criarConta())
print ("----- Contas -----")
for i in range(0,len(banco.listaContas),1):
    print(banco.listaContas[i].informarAgencia(), " - ", banco.listaContas[i].informarNroConta())
print ("----- Fim Contas -----")
print()
print("saldo inicial conta1",banco.listaContas[0].informarSaldo())
print("saldo inicial conta2",banco.listaContas[1].informarSaldo())
print()
print ("------ Deposito ------")
banco.listaContas[0].depositar(100, "deposito em dinheiro")
print("saldo primeira conta apos deposito",banco.listaContas[0].informarSaldo())
print ("------ Fim Deposito ------")
print()
print ("------ Transferência ------")
banco.transferir(banco.listaContas[0], banco.listaContas[1], 50)
print("saldo primeira conta apos transferencia",banco.listaContas[0].informarSaldo())
print("saldo segunda conta apos transferencia",banco.listaContas[1].informarSaldo())
print ("------ Fim Transferência ------")
print()
print ("------ Extrato ------")
print("----Conta 1---- ")
banco.listaContas[0].emitirExtrato()
print("----Conta 2---- ")
banco.listaContas[1].emitirExtrato()
print ("------ Fim Extrato ------")
print()
print ("------ Exclusão Conta 1 ------")
print(banco.excluirConta(banco.listaContas[0]))
print("conta 1 excluida, conta no banco:")
for i in range(0,len(banco.listaContas),1):
    print(banco.listaContas[i].informarAgencia(), " - ", banco.listaContas[i].informarNroConta())
print ("------ Fim Exclusão Conta 1 ------")

