class Computador:
    def __init__(self,marca,memoria,cpu,gpu,hd):
        self.marca = marca #string
        self.memoria = memoria # int
        self.cpu = cpu #string
        self.gpu = gpu #booleana
        self.hd = hd #int
        self.sos = [] #lista
        self.mensagem = '' #string
        self.caixa_postal = ''
    def liga(self):
        print("Iniciando boot no S.O. " + self.so_utilizado)
    def desliga(self):
        print("Desligando...")
    def execute(self, programa):
        print("Executando " + programa + " no S.O. " + self.so_utilizado)
    def insere_sistema_operacional(self, sistema):
        self.sos.append(sistema)
    def boot(self, n):
        self.so_utilizado = self.sos[n]
    def sistemas_operacionais(self):
        st = ""
        for i in range(len(self.sos)):
            st += self.sos[i] + " instalado" + '\n'
        return st
    def escrever_mensagem(self,texto):
        self.mensagem += texto + '\n'
    def enviar_mensagem(self, destino):
        destino.caixa_postal += self.mensagem
    def receber_mensagem(self):
        self.mensagem += self.caixa_postal
    def ler_mensagens(self):
        print(self.mensagem)
    def __str__(self):
        s = ""
        s += "Computador da marca " + self.marca + '\n'
        s += str(self.memoria) + " GB de memória \n"
        s += "CPU: " + self.cpu + '\n'
        s += "HD de " + str(self.hd) + ' TB de memória \n'
        s += "Sistemas operacionas instalados: \n" + self.sistemas_operacionais() 
        if self.gpu == True:
            s += "Tem GPU"
        else: s += "Não tem gpu"
        return s