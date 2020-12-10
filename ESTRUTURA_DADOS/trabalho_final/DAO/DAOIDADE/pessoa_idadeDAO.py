from ESTRUTURA_DADOS.trabalho_final.DAO.abstract_DAO import DAO
from ESTRUTURA_DADOS.trabalho_final.model.pessoa import Pessoa


class PessoaIDADE(DAO):
    def __init__(self):
        super().__init__('DAO/DAOIDADE/pessoa_idade.pkl')

    def inclui(self, pessoa: Pessoa):
        if (pessoa is not None) and (isinstance(pessoa.idade, int)) and isinstance(pessoa, Pessoa):
            super().add(pessoa.idade, pessoa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
