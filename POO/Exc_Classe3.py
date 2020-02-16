import datetime
class Historico:  
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
class Conta:
    def __init__(self, agencia, conta, cliente, saldo):
        self.agencia = agencia
        self.conta = conta
        self.titular = cliente
        self.saldo = saldo
        self.historico = Historico()
    def saca(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return "Saque concluido."
        else: return "Saldo insuficiente."
    def getSaldo(self):
        return self.saldo
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {}".format(valor))
    def verificaNegativade(self):
        if self.saldo < 0:
            return "sua conta esta negativada."
        else: return "sua conta esta tudo ok."
    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return "Nao foi possivel transferir."
        else:
            self.historico.transacoes.append("Transferencia de {}".format(valor))
            destino.deposita(valor)
            return "Valor transferido com sucesso."
cliente = Cliente('João', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', '09821-7' ,cliente, 120.0)
