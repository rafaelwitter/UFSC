from Funcionario import Funcionario
class Professor(Funcionario):
    def __init__(self, nome, endereco, telefone, email, nroSala, salario, dataContrato, hrsAula, hrsPesquisa):
        super().__init__(nome,endereco,telefone,email, nroSala, salario, dataContrato)
        self.hrsAula = hrsAula
        self.hrsPesquisa = hrsPesquisa
    def __str__(self):
        s = 'Classe professor. \n'
        s += 'meu nome é: ' + self.nome + ' e eu sou um professor desde ' 
        s += self.dataContrato + 'Meu escritorio é: '
        s += self.nroSala + ' com salário de: ' + self.salario 
        return s