global_next_id = 1


class Pessoa:
    def __init__(self, nome: str, idade: int, nacionalidade: str):
        global global_next_id
        self.iden = global_next_id
        global_next_id += 1
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    def __repr__(self):
        return f'ID: {str(self.iden)}, Nome: {self.nome}, Idade: {str(self.idade)}, Nacionalidade: {self.nacionalidade}'
