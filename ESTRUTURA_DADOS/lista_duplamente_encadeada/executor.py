from lista_encadeada import *    #Instancia de um lista encadeada vazia == None
if __name__ == "__main__":
    #Criada uma lista encadeada vazia
    lista = ListaEncadeada()
    #Tentando remover item de uma lista vazia
    lista.remove(2)

    #Inserindo um elemento qualquer no incio 
    lista.insere_no_inicio(1.1)
    print(lista)
    print("------------------------------------")

    #Inserindo um elemento qualquer no incio 
    lista.insere_no_inicio(1.0)
    print(lista)
    print("------------------------------------")

    #Inserindo um elemento qualquer depois da cabeça da lista 
    lista.insere_depois(2.0)
    print(lista)
    print("------------------------------------")

    #Printando o indice que se encontra o valor
    print(lista.index(2.0))
    print("------------------------------------")

    #Removendo um valor pelo seu valor
    lista.remove(2.0)
    print(lista)
    print("------------------------------------")

    #Buscando um valor
    #Retorna True se encontrado e False se não
    print(lista.busca(1.1))
    print("------------------------------------")