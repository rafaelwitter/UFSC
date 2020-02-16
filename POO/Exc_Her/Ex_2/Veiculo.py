class Veiculo:
    def __init__(self):
        self.__nome = ''
        self.__bancos = 0
        self.__carga = 0
    def setNome(self,nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    def setBancos(self,bancos):
        self.__bancos = bancos
    def getBancos(self):
        return self.__bancos
    def setCarga(self,carga):
        self.__carga = carga
    def getCarga(self):
        return self.__carga
    def __str__(self):
        s = 'O veiculo é um ' + self.__nome
        return s
class Automovel(Veiculo):
    def __init__(self,nome,bancos,carga,fabrica,modelo,ano,valorFabrica,desvalorizacao,motor,combustivel,tanque,consumo):
        super().__init__()
        self.__nome = nome
