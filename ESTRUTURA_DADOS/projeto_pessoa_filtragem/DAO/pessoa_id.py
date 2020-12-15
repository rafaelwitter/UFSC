from DAO.abstract_DAO import DAO
from model.pessoa import Pessoa


class PessoaID(DAO):
    def __init__(self):
        super().__init__('DAO/pessoa_id.pkl')

    def inclui(self, pessoa: Pessoa):
        if (pessoa is not None) and (isinstance(pessoa.id, int)) and isinstance(pessoa, Pessoa):
            super().add(pessoa.id, pessoa)
