from Conta import Conta
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
conta = ContaCorrente(1, 34, 500, 500)
conta.informarSaldo()
print(conta.depositar(20, "transferencia"), "deposito feito.")
conta.informarSaldo()
conta.verificaLimiteSaque()
conta.saca(20, "transferencia")
conta.verificaLimiteSaque()
conta.informarSaldo()
