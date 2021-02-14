from typing import List, Any

from model.pessoa import Pessoa
from DAO.pessoa_id import PessoaID


class ControladorPessoa:
    """Essa classe cria um Objeto do Tipo Pessoa e inclui no BD Pickle"""

    def __init__(self, controlador_geral):
        self.controlador = controlador_geral
        self.lista_nacionalidades = {"Brasil": [], "Espanha": [], "Alemanha": [], "Estado Unidos": [],
                                     "França": [], "Portugal": [], "Canada": []}
        self.lista_cor = {"Branco": [], "Negro": [], "Pardo": []}
        self.idDAO = PessoaID()
        self.inclui_nacionalidades()
        self.inclui_raca()

    def cria_pessoa(self, nome, idade, nacionalidade, raca):
        """Adiciona no arquivo .pkl uma pessoa com id aleatorio"""
        self.idDAO.inclui(Pessoa(nome, idade, nacionalidade, raca))

    def remove_pessoa(self, key):
        """Remove uma pessoa do arquivo .pkl"""
        self.idDAO.remove(key)

    def busca_todas(self):
        """Retorna todas as pessoas do arquivo .pkl"""
        return self.idDAO.get_all()

    def busca_especifica(self, key):
        return self.idDAO.get(key)

    def inclui_nacionalidades(self):
        for pessoa in self.busca_todas():
            if pessoa.nacionalidade == "Brasil":
                self.lista_nacionalidades["Brasil"].append(pessoa.id)
            elif pessoa.nacionalidade == "Espanha":
                self.lista_nacionalidades["Espanha"].append(pessoa.id)
            elif pessoa.nacionalidade == "Alemanha":
                self.lista_nacionalidades["Alemanha"].append(pessoa.id)
            elif pessoa.nacionalidade == "Estado Unidos":
                self.lista_nacionalidades["Estado Unidos"].append(pessoa.id)
            elif pessoa.nacionalidade == "França":
                self.lista_nacionalidades["França"].append(pessoa.id)
            elif pessoa.nacionalidade == "Portugal":
                self.lista_nacionalidades["Portugal"].append(pessoa.id)
            else:
                self.lista_nacionalidades["Canada"].append(pessoa.id)

    def inclui_raca(self):
        for pessoa in self.busca_todas():
            if pessoa.raca == "Branco":
                self.lista_cor["Branco"].append(pessoa.id)
            if pessoa.raca == "Negro":
                self.lista_cor["Negro"].append(pessoa.id)
            if pessoa.nacionalidade == "Pardo":
                self.lista_cor["Pardo"].append(pessoa.id)

    def interseccao(self, cor=None, nacio=None):
        raca = self.lista_cor[cor]
        nac = self.lista_nacionalidades[nacio]
        intersec = [r for r in raca if r in nac]
        return intersec
