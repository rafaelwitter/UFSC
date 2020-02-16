class AjudanteMatematico:
    def ehPar():
        '''
        Verificar se um numero é par.
        '''
        nmr = int(input("Digite o numero para verificar se é par: "))
        if nmr % 2 == 0:
            return True
        else: return False
    def ehImpar(nmr):
        '''
        Verificar se o numero informado é impar.
        '''
        if nmr % 2 != 0 and nmr == 2:
            return False
        else: return True
    def somaQuadrado(n1,n2,n3,n4):
        pass
    def maiorNumero(n1,n2,n3):
        '''
        Encontrar o maior numero entre 3.
        '''
        if n1 > n2 and n1 >n3:
            print(('{} eh o maior numero.').format(n1))
        elif n2 > n1 and n2 > n3:
            print(('{} eh o maior numero.').format(n2))
        else: print(('{} eh o maior numero.').format(n3))
    def areaCirc(raio):
        '''
        Calcular area de uma circunferencia informando seu raio.
        '''
        area = (3,14159 * (raio ** 2))
    def ehPrimo(nmr):
        '''
        Verificar se um numero eh primo.
        '''
        contador = 0
        div = 1
        while div <= nmr:
            if nmr % div == 0:
                contador += 1
            div += 1   
        if contador == 2:
            return True
        else:
            return False 