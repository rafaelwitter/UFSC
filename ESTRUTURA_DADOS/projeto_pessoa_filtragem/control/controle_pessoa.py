from model.pessoa import Pessoa
from DAO.pessoa_id import PessoaID


class ControladorPessoa:
    """Essa classe cria um Objeto do Tipo Pessoa e inclui no BD Pickle"""
    def __init__(self, controlador_geral):
        self.controlador = controlador_geral
        self.idDAO = PessoaID()

    def cria_pessoa(self, nome, idade, nacionalidade, raca):
        """Adiciona no arquivo .pkl uma pessoa com id aleatorio"""
        self.idDAO.inclui(Pessoa(nome, idade, nacionalidade, raca))

    def remove_pessoa(self, key):
        """Remove uma pessoa do arquivo .pkl"""
        self.idDAO.remove(key)

    def busca_todas(self):
        """Retorna todas as pessoas do arquivo .pkl"""
        return self.idDAO.get_all()
