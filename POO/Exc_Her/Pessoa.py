class Pessoa:
    def __init__(self,nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco 
        self.telefone = telefone
        self.email = email
    def getNome(self):
        return print(self.nome)
    def __str__(self):
        s = ''
        s += 'meu nome é: ' + self.nome + ' e eu sou uma pessoa.'
        return s
class Estudante(Pessoa):
    '''
    O objeto estudante possui um atributo diferente da classe Pessoa, a qual ele herda caract
    Que é 'graduacao', recebe só e somente valor de BIXO, VETERANO, QUASE GRADUANDO.
    '''
    def __init__(self,nome,endereco, telefone, email, graduacao):
        super().__init__(nome,endereco,telefone,email)
        self.graduacao = graduacao
    def __str__(self):
        s = ''
        s += 'meu nome é: ' + self.nome + ' e eu sou um estudante de: ' + self.graduacao
        return s