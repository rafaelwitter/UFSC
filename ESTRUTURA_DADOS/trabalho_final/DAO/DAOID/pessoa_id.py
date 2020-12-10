from ESTRUTURA_DADOS.trabalho_final.DAO.abstract_DAO import DAO
from ESTRUTURA_DADOS.trabalho_final.model.pessoa import Pessoa


class PessoaID(DAO):
    def __init__(self):
        super().__init__('DAO/DAOID/pessoa_id.pkl')

    def inclui(self, pessoa: Pessoa):
        if (pessoa is not None) and (isinstance(pessoa.iden, int)) and isinstance(pessoa, Pessoa):
            super().add(pessoa.iden, pessoa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
