from ESTRUTURA_DADOS.trabalho_final.DAO.abstract_DAO import DAO
from ESTRUTURA_DADOS.trabalho_final.model.pessoa import Pessoa


class PessoaNOME(DAO):
    def __init__(self):
        super().__init__('DAO/DAONOME/pessoa_nome.pkl')

    def inclui(self, pessoa: Pessoa):
        if (pessoa is not None) and (isinstance(pessoa.nome, str)) and isinstance(pessoa, Pessoa):
            super().add(pessoa.nome, pessoa)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
