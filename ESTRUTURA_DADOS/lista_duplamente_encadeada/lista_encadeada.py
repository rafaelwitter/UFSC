from no_lista import NodoLista

class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0
    
    def vazia(self):
        if self._tamanho == 0:
            return True
        else: return False

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, novo_dado):
        # 1) Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = NodoLista(novo_dado)

        # 2) Faz com que o novo nodo seja a cabeça da lista.
        novo_nodo.proximo = self.cabeca

        # 3) Faz com que a cabeça da lista referencie o novo nodo.
        self.cabeca = novo_nodo
        self._tamanho += 1
    
    def insere_depois(self, novo_dado):
        """Essa função insere no final da lista"""
        #Define a cabeça como velha
        nodo_anterior = self.cabeca
        # Cria um novo nodo com o dado desejado.
        novo_nodo = NodoLista(novo_dado)

        # Faz o próximo do novo nodo ser o próximo do nodo anterior.
        novo_nodo.proximo = nodo_anterior.proximo

        # Faz com que o novo nodo seja o próximo do nodo anterior.
        nodo_anterior.proximo = novo_nodo
        self._tamanho += 1
    
    def busca(self, valor):
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
            if corrente.dado == valor:
                return str(True) + ": elemento excluido"
            else: return str(False) + ": elemento nao encontrado"
    
    def remove(self, valor):
        #Testa lista vazia
        if self.vazia():
            return print("Não se pode remover elementos de uma lista vazia")
        # Nodo a ser removido é a cabeça da lista.
        elif self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
            self._tamanho -= 1
        else:
            # Encontra a posição do elemento a ser removido.
            antecessor = self.cabeca
            ponteiro = self.cabeca
            while ponteiro:
                if ponteiro.dado == valor:
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                    print("O elemento: " + str(valor) + " foi removido da lista")
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
                self._tamanho -= 1
                
        
    def index(self, elem):
        """Retorna o indice de um valor na lista"""
        ponteiro = self.cabeca
        i = 0 
        while ponteiro:
            if ponteiro.dado == elem:
                return "o valor " + str(elem) + " esta no indice: " + str(i)
            ponteiro = ponteiro.proximo
            i+=1
        raise ValueError("{} o elemento nao esta na lista".format(elem))

    def __getitem__(self, index):
        """Objtem um item através do seu indice"""
        ponteiro = self._getnode(index)
        if ponteiro:
            return ponteiro.dado
        else: raise IndexError("Esse indice nao foi encontrado")
    
    def __setitem__(self, index, elem):
        """Seta um item em um indice existente"""
        ponteiro = self._getnode(index)
        if ponteiro:
            ponteiro.dado = elem
        else:
            return IndexError("Error")

    def insert(self, indice, valor):
        """Insere um elemento no indice indicado"""
        no = NodoLista(valor)
        if indice == 0:
            no = NodoLista(valor)
            no.proximo = self.cabeca
            self.cabeca = no
        else: 
            ponteiro = self._getnode(indice-1)
            no.proximo = ponteiro.proximo
            ponteiro.proximo = no
        self._tamanho += 1

    def _getnode(self, index):
        ponteiro = self.cabeca
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError("O index não existe")
        return ponteiro

