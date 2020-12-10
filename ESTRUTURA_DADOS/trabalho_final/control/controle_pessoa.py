from ESTRUTURA_DADOS.trabalho_final.model.pessoa import Pessoa
from ESTRUTURA_DADOS.trabalho_final.DAO.DAOID.pessoa_id import PessoaID
from ESTRUTURA_DADOS.trabalho_final.DAO.DAOIDADE.pessoa_idadeDAO import PessoaIDADE
from ESTRUTURA_DADOS.trabalho_final.DAO.DAONACIONALIDADE.pessoa_nacionalidadeDAO import PessoaNTN
from ESTRUTURA_DADOS.trabalho_final.DAO.DAONOME.pessoa_nomeDAO import PessoaNOME


class ControladorPessoa:
    """Essa classe cria um Objeto do Tipo Pessoa e inclui em varios bancos de dados (possuindo somente
    a chave diferente"""
    def __init__(self, controlador_geral):
        self.controlador = controlador_geral
        self.idDAO = PessoaID()
        self.idadeDAO = PessoaIDADE()
        self.nacionalidadeDAO = PessoaNTN()
        self.nomeDAO = PessoaNOME()

    def criar_pessoa(self, nome, idade, nacionalidade):
        self.idDAO.inclui(Pessoa(nome, idade, nacionalidade))
        self.idadeDAO.inclui(Pessoa(nome, idade, nacionalidade))
        self.nacionalidadeDAO.inclui(Pessoa(nome, idade, nacionalidade))
        self.nomeDAO.inclui(Pessoa(nome, idade, nacionalidade))

    def busca_todas(self):
        return self.idDAO.get_all()

    def busca_todas_nacionalidade(self):
        return self.nacionalidadeDAO.get_all()

    def busca_por_idade(self):
        return self.idadeDAO.get_all()

    def busca_por_nome(self):
        return self.nomeDAO.get_all()
