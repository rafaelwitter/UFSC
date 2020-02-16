from Pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, endereco, telefone, email, nroSala, salario, dataContrato):
        super().__init__(nome,endereco,telefone,email)
        self.nroSala = nroSala
        self.salario = salario
        self.dataContrato = dataContrato
    def __str__(self):
        s = ''
        s += 'meu nome é: ' + self.nome + ' e eu sou um funcionario desde ' 
        s += self.dataContrato + 'Meu escritorio é: '
        s += self.nroSala + ' com salário de: ' + self.salario 
        return s