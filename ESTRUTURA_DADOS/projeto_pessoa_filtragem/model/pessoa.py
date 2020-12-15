import random


class Pessoa:

    def __init__(self, nome: str, idade: int, nacionalidade: str, raça: str):
        self.id = random.randrange(1, 999, step=1)
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.raca = raça

    def __repr__(self):
        return f'ID: {str(self.id)}, Nome: {self.nome}, Idade: {str(self.idade)}, ' \
               f'Nacionalidade: {self.nacionalidade}, Raça/Cor: {self.raca}'
