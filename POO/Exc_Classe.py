class Carro:  
    def __init__(self ,modelo, marca, cor):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor     
    def getCor(self):
        return self.cor
    def getModelo(self):
        return self.modelo
    def getMarca(self):
        return self.marca
    def listaCarro(self):
        listaCarro = []
        listaCarro.append(self.modelo)
        return listaCarro
class Pessoa:
    def __init__(self, nome, endereco, cpf, telefone):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone
    def getNome(self):
        return self.nome
    def getEndereco(self):
        return self.endereco
    def getCpf(self):
        return self.cpf
    def getTelefone(self):
        return self.telefone
class Relogio:
    def __init__(self, marca, cor, formato):
        self.marca = marca
        self.cor = cor
        self.formato = formato
    def getMarca(self):
        return self.marca
    def getCor(self):
        return self.cor
    def getFormato(self):
        return self.formato
    def listaRelogio(self):
        listaRelogio = []
        listaRelogio.append(self.marca)
        listaRelogio.append(self.cor)
        listaRelogio.append(self.formato)
        return listaRelogio
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def cordX(self):
        return self.x
    def cordY(self):
        return self.y
new_carro = Carro("A3", "Audi","Preto")
old_carro = Carro("Uno", "Fiat", "Rosa")
carro_do_vinicius = Carro("Ethos", "Toyota", "Azul")
print(Carro.listaCarro(old_carro), Carro.listaCarro(carro_do_vinicius))