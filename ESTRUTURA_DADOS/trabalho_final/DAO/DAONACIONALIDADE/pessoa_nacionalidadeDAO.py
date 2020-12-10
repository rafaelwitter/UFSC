from ESTRUTURA_DADOS.trabalho_final.DAO.abstract_DAO import DAO
from ESTRUTURA_DADOS.trabalho_final.model.pessoa import Pessoa


class PessoaNTN(DAO):
    def __init__(self):
        super().__init__('DAO/DAONACIONALIDADE/pessoa_nacionalidade.pkl')

    def inclui(self, pessoa: Pessoa):
        if (pessoa is not None) and (isinstance(pessoa.nacionalidade, str)) and isinstance(pessoa, Pessoa):
            super().add(pessoa.nacionalidade, pessoa)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
