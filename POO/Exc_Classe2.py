class Pessoa:
    def __init__(self, nome, idade, endereco, rg, cpf):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.rg = rg
        self.cpf = cpf
    def getAll(self):
        a = self.nome
        b = self.idade
        c = self.endereco
        d = self.rg
        e = self.cpf
        print(('O nome da pessoa é {}, sua idade {}, seu endereco {}, seu rg {} e seu cpf {}').format(a,b,c,d,e))
    def getIdade(self):
        return self.idade
    def alteraEndereco(self, endereco):
        self.endereco = endereco
class Funcionario:
    def __init__(self, salario):
        self.salario = salario
    def calculaImposto(self, imposto):
        imposto = (self.salario * (imposto / 100))
        return imposto
    def ferias(self):
        '''
        Dias de ferias corridos proporcional a 2% do salario
        '''
        ferias = self.salario * 0.02
        return ferias
    def alteraSalario(self, salario):
        self.salario = salario
    def aumentaSalario(self, porcentagem):
        aumento = (self.salario * (porcentagem/100))
        new_salario = self.salario + aumento
        self.salario = new_salario
    def getSalario(self):
        return self.salario
a = Funcionario(2000)
print(a.getSalario())
print(a.ferias())
print(a.calculaImposto(11))
a.aumentaSalario(20)
print(a.getSalario())
print(a.ferias())
print(a.calculaImposto(11))
a.alteraSalario(900)
print(a.getSalario())
print(a.calculaImposto(20))
b = Pessoa("Rafael", 18, "Protenor vidal")
b.getAll()