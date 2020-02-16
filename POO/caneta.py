class Caneta:
    def __init__(self, cor, tampa, transparencia, tem_tinta):
        self.cor = cor
        self.tampa = tampa
        self.transparencia = transparencia
        self.tem_tinta = tem_tinta
    def __str__(self): #É usada para print(objeto), listar todos os itens criados
        s = ""
        s += "A cor da caneta é " + self.cor + '\n'
        if self.tampa == True:
            s+= "A caneta tem tampa." + '\n'
        else: s+= "A caneta não tem tampa." + '\n'
        if self.transparencia == True:
            s+= "A caneta é transparente." + '\n'
        else: s+= "A caneta não é transparente." + '\n'
        if self.tem_tinta == True:
            s += "A caneta ainda pode ser usada." 
        else: s += "A caneta não pode mais ser utilizada." 
        return s
    def abre_fecha(self):
        if self.tampa == True:
            b = input("A tampa está fechada, deseja abrir? (Y/N): ")
            if (str.upper(b) == "y"):
                self.tampa = False
                print("A tampa foi aberta.")
            elif (str.upper(b) == "n"):
                self.tampa = self.tampa
                print("A tampa continua fechada.")
        else:
            b = str(input("A tampa está aberta, deseja fechar? (Y/N): "))
            if (str.upper(b) == "y"):
                self.tampa = True
                print("A tampa está fechada.")
            elif (str.upper(b) == "n"):
                print("A tampa continua aberta.")
        
def main():
    bic = Caneta("Azul", True, True, True)
    bic.abre_fecha()
    print(bic)
main()