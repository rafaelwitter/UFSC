class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self._tamanho = 0

    def vazia(self):
        if self.inicio is None:
            return True
        return False

    def add_inicio(self, valor):
        no = No(valor)
        if self.vazia():
            self.inicio = self.final = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            no.anterior = None
            self.inicio = no
        self._tamanho += 1

    def add_fim(self, valor):
        no = No(valor)
        if self.vazia():
            self.inicio = self.final = no
        else:
            self.final.proximo = no
            no.anterior = self.final
            no.proximo = None
            self.final = no
        self._tamanho -= 1

    def insere(self, indice, valor):
        metade = self._tamanho / 2
        if indice > self._tamanho:
            raise IndexError("Lista menor do que o indice informado")
        elif indice == self._tamanho:
            self.add_fim(valor)
        elif indice == 0:
            self.add_inicio(valor)
        else:
            no = No(valor)
            if indice <= metade:
                perc = self.inicio
                cont = 0
                while cont < indice - 1:
                    perc = perc.proximo
                    cont += 1
                no.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = no
            else:
                perc = self.final
                cont = self.get_tamanho()
                while cont > indice:
                    perc = perc.anterior
                    cont -= 1
                no.proximo = perc.proximo
                perc.proximo.anterior = no
                perc.proximo = no
                no.anterior = perc
            self._tamanho += 1

    def remove_inicio(self):
        if self.vazia():
            raise IndexError("Lista vazia")
        elif self._tamanho == 1:
            self.inicio = None
            self.final = None
        else:
            self.final = self.final.anterior
            self.final.proximo = None
        self._tamanho -= 1

    def remove_final(self):
        if self.vazia():
            raise IndexError("Lista vazia")
        elif self._tamanho == 1:
            self.inicio = None
            self.final = None
        else:
            self.final = self.final.anterior
            self.final.proximo = None
        self._tamanho -= 1

    def remove_indice(self, indice):
        if self.vazia():
            raise TypeError("Lista vazia")
        elif indice == 0:
            self.remove_inicio()
        else:
            pointeiro = self.inicio
            cont = 0
            while cont < indice - 1:
                pointeiro = pointeiro.proximo
                cont += 1
            aux = pointeiro.proximo
            pointeiro.proximo = aux.proximo
            aux = None
            pointeiro.proximo = aux
            self._tamanho -= 1

    def remove_valor(self, valor):
        if self._tamanho == 0:
            return None
        ponteiro = self.inicio
        cont = 0
        while ponteiro.dado != valor:
            ponteiro = ponteiro.proximo
            cont += 1
        self.remove_indice(cont)

    def busca_indice(self, indice):
        if self.vazia():
            raise TypeError("Lista vazia")
        elif indice > self._tamanho:
            raise IndexError("Indice maior que o suportado")
        else:
            ponteiro = self.inicio
            cont = 0
            while cont < self._tamanho:
                if cont == indice:
                    return f'No indice {indice} tem valor de {ponteiro.dado}'
                ponteiro.proximo
                cont += 1

    def busca_valor(self, valor):
        if self.vazia():
            raise TypeError("Lista vazia")
        else:
            ponteiro = self.inicio
            cont = 0
            while ponteiro:
                if ponteiro.dado == valor:
                    return f'{valor} esta no indice {cont}'
                ponteiro = ponteiro.proximo
                cont += 1
            raise ValueError(f'{valor} nao esta na lista')

    def altera_valor(self, indice, valor):
        if self.vazia():
            raise TypeError("Lista vazia")
        elif indice > self.get_tamanho():
            raise IndexError("Indice maior que o esperado")
        else:
            ponteiro = self.inicio
            cont = 0
            while cont != indice:
                ponteiro = ponteiro.proximo
                cont += 1
            ponteiro.dado = valor

    def get_tamanho(self):
        return self._tamanho

    def get_index(self, indice):
        if self.vazia():
            raise TypeError("Lista vazia")
        elif indice > self.get_tamanho():
            raise IndexError("Indice maior que o esperado")
        else:
            ponteiro = self.inicio
            cont = 0
            while cont < self._tamanho:
                if cont == indice:
                    return ponteiro.dado
                ponteiro = ponteiro.proximo
                cont += 1

    def conta_valores(self, valor):
        """retorna quantas vezes o valor indicado foi encontrado"""
        pass

    def __str__(self):
        valor = '['
        if self.inicio is not None:
            ponteiro = self.inicio
            valor += str(ponteiro.dado)
            while ponteiro.proximo is not None:
                ponteiro = ponteiro.proximo
                valor += ', '
                valor += str(ponteiro.dado)
        valor += ']'
        return valor

    def __len__(self):
        return self.get_tamanho()

    def __getitem__(self, item):
        """retorna os valores ---> lista[índice]"""
        if item >= self._tamanho:
            raise StopIteration
        return self.get_index(item)

    def __setitem__(self, indice, valor):
        return self.altera_valor(indice, valor)
