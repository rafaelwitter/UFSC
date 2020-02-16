from Funcionario import Funcionario
class Servidor(Funcionario):
    def __init__(self, nome, endereco, telefone, email, nroSala, salario, dataContrato, cargaHoraria, titualacao):
        super().__init__(nome,endereco,telefone,email, nroSala, salario, dataContrato)
        self.cargaHoraria = cargaHoraria
        self.titulacao = titualacao
    def __str__(self):
        s = ''
        s += 'meu nome é: ' + self.nome + ' e eu sou um servidor, titulado a: ' + self.titulacao ', desde ' 
        s += self.dataContrato + 'Meu escritorio é: '
        s += self.nroSala + ' com salário de: ' + self.salario 
        return s