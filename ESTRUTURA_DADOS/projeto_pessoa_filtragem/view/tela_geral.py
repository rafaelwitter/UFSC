import PySimpleGUI as sg


class TelaPrincipal:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.window = None
        self.window_pessoas = None
        self.window_inclui = None
        self.window_pesquisa = None
        self.window_pesquisa_multipla = None

    def tela_inicio(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Text("Ola\n Escolha uma opção")],
                  [sg.Button("Ver todas as pessoas"), sg.Button("Adicionar pessoa"),
                   sg.Button("Pesquisas unicas"),
                   sg.Button("Pesquisas multiplas")],
                  [sg.Button("Sair")]]
        self.window = sg.Window("Tela Principal").layout(layout)

    def open_inicio(self):
        buttons, values = self.window.Read()
        return buttons, values

    def tela_inclui_pessoa(self):
        sg.ChangeLookAndFeel('Reddit')
        nacionalidades = ["Brasil", "Espanha", "Alemanha", "Estado Unidos", "França", "Portugal", "Canada"]
        raca = ["Branco", "Negro", "Pardo"]
        layout = [
            [sg.Text('Nome:  ', size=(40, 1)), sg.InputText()],
            [sg.Text('Idade:  ', size=(40, 1)), sg.InputText()],
            [sg.Text('Nacionalidade: ', size=(40, 1)), sg.Combo(nacionalidades, size=(40, 1), text_color='black')],
            [sg.Text('Raça/Cor: ', size=(40, 1)), sg.Combo(raca, size=(40, 1), text_color='black')],
            [sg.Button("Adicionar"), sg.Button("Voltar")]
        ]
        self.window_inclui = sg.Window("Inclui pessoa").Layout(layout)

    def open_inclui(self):
        self.window.hide()
        button, value = self.window_inclui.Read()
        return button, value

    def close_inclui(self):
        self.window_inclui.close()

    def tela_todas_pessoas(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = []
        self.window.hide()
        if self.__controlador.lista_todas_pessoa():
            for pessoa in self.__controlador.lista_todas_pessoa():
                layout += [
                    [sg.Checkbox("", key=pessoa.id), sg.Text("ID: " + str(pessoa.id)), sg.Text("Nome: " + pessoa.nome),
                     sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                     sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça/Cor: " + pessoa.raca)]]
            layout += [[sg.Button("Excluir"), sg.Exit("Sair"), sg.Button("Voltar")]]
            self.window_pessoas = sg.Window("Pessoas").layout(layout)
        else:
            self.window_pessoas = sg.Popup("Nao existem pessoas cadastradas")
            self.window.un_hide()

    def open_pessoas(self):
        button, values = self.window_pessoas.Read()
        return button, values

    def close_pessoas(self):
        self.window_pessoas.close()

    def multipla_pesquisa(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Radio('Procurar uma pessoa com todos os atributos', group_id=1, key='all'),
                   sg.Radio('Procurar por idade e nacionalidade', group_id=1, key='idade_nacionalidade'),
                   sg.Radio('Procurar por nome e idade', group_id=1, key='nome_idade'),
                   sg.Radio("Procurar por nome e nacionalidade", group_id=1, key='nome_nacionalidade')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_multipla = sg.Window("Filtro de pessoas").layout(layout)

    def open_multipla_escolha(self):
        self.window.hide()
        b, v = self.window_pesquisa_multipla.Read()
        return b, v

    def close_multipla(self):
        self.window_pesquisa_multipla.close()
        self.window.hide()

    def pesquisa_pessoas(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Radio('Procurar por nacionalidade', group_id='1', key='nacionalidade'),
                   sg.Radio('Procurar por idade', group_id='1', key='idade'),
                   sg.Radio('Procurar por nome', group_id='1', key='nome'),
                   sg.Radio('Procurar por raça/cor', group_id='1', key='cor')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa = sg.Window("Filtro de pessoas").layout(layout)

    def close_pesquisa_pessoas(self):
        self.window_pesquisa.close()

    def open_pesquisa(self):
        button, value = self.window_pesquisa.Read()
        return button, value


class TelaPesquisa:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.window_pesquisa_nome = None
        self.window_pesquisa_idade = None
        self.window_pesquisa_nacionalidade = None
        self.window_pesquisa_cor = None
        self.window_mostra_pesquisa_nome = None
        self.window_mostra_pesquisa_cor = None
        self.window_mostra_pesquisa_nacionalidade = None
        self.window_mostra_pesquisa_idade = None
        self.window_pesquisa_idade_nome = None
        self.window_pesquisa_nacionalidade_idade = None
        self.window_pesquisa_all = None
        self.window_mostra_pesquisa_all = None
        self.window_pesquisa_nacionalidade_nome = None

    def pesquisa_nome(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Text("Digite o nome a ser pesquisado: "), sg.InputText(key='nome')], [sg.Button("Ok"),
                                                                                            sg.Button("Voltar")]]
        self.window_pesquisa_nome = sg.Window("Pesquisa por nome").Layout(layout)

    def open_pesquisa_nome(self):
        b, v = self.window_pesquisa_nome.Read()
        return b, v

    def close_pesquisa_nome(self):
        self.window_pesquisa_nome.close()

    def mostra_pesquisa_nome(self, nome):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        if self.__controlador.lista_todas_pessoa():
            for pessoa in self.__controlador.lista_todas_pessoa():
                if pessoa.nome.upper() == str(nome.upper()):
                    layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                                 sg.Text("Idade: " + str(pessoa.idade))]]
            layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        else:
            sg.popup("Nao existem pessoas cadastradas")
        self.window_mostra_pesquisa_nome = sg.Window("Pesquisa por nomes").Layout(layout2)

    def open_mostra_pesquisa_nome(self):
        b, v = self.window_mostra_pesquisa_nome.Read()
        return b, v

    def close_mostra_pesquisa_nome(self):
        self.window_mostra_pesquisa_nome.close()

    def pesquisa_nacionalidade(self):
        sg.ChangeLookAndFeel('Reddit')
        nacionalidades = ["Brasil", "Espanha", "Alemanha", "Estado Unidos", "França", "Portugal", "Canada"]
        layout = [[sg.Text("Escolha uma nacionalidade para ser pesquisada: "), sg.Combo(nacionalidades)],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_nacionalidade = sg.Window("Pesquisa por nacionalidade").Layout(layout)

    def open_pesquisa_nacionalidade(self):
        b, v = self.window_pesquisa_nacionalidade.Read()
        return b, v

    def close_pesquisa_nacionalidade(self):
        self.window_pesquisa_nacionalidade.close()

    def mostra_pesquisa_nacionalidade(self, nacionalidade):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.nacionalidade.upper() == nacionalidade.upper():
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade))]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_mostra_pesquisa_nacionalidade = sg.Window("Pesquisa por nacionalidade").Layout(layout2)

    def open_mostra_pesquisa_nacionalidade(self):
        b, v = self.window_mostra_pesquisa_nacionalidade.Read()
        return b, v

    def close_mostra_pesquisa_nacionalidade(self):
        self.window_mostra_pesquisa_nacionalidade.close()

    def pesquisa_cor(self):
        sg.ChangeLookAndFeel('Reddit')
        raca = ["Branco", "Negro", "Pardo"]
        layout = [[sg.Text("Escolha uma cor para ser pesquisada: "), sg.Combo(raca, key='cor')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_cor = sg.Window("Pesquisa por cor").Layout(layout)

    def open_pesquisa_cor(self):
        b, v = self.window_pesquisa_cor.Read()
        return b, v

    def close_pesquisa_cor(self):
        self.window_pesquisa_cor.close()

    def mostra_pesquisa_cor(self, cor):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.raca.upper() == cor.upper():
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça: " + pessoa.raca)]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_mostra_pesquisa_cor = sg.Window("Pesquisa por cor").Layout(layout2)

    def open_mostra_pesquisa_cor(self):
        b, v = self.window_mostra_pesquisa_cor.Read()
        return b, v

    def close_mostra_pesquisa_cor(self):
        self.window_mostra_pesquisa_cor.close()

    def pesquisa_idade(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Text("Digite a idade a ser pesquisada: "), sg.InputText(key='idade')], [sg.Button("Ok"),
                                                                                              sg.Button("Voltar")]]
        self.window_pesquisa_idade = sg.Window("Pesquisa por idade").Layout(layout)

    def open_pesquisa_idade(self):
        b, v = self.window_pesquisa_idade.Read()
        return b, v

    def close_pesquisa_idade(self):
        self.window_pesquisa_idade.close()

    def mostra_pesquisa_idade(self, idade):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.idade == int(idade):
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade))]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_mostra_pesquisa_idade = sg.Window("Pesquisa por nomes").Layout(layout2)

    def open_mostra_pesquisa_idade(self):
        b, v = self.window_mostra_pesquisa_idade.Read()
        return b, v

    def close_mostra_pesquisa_idade(self):
        self.window_mostra_pesquisa_idade.close()

    def pesquisa_idade_nome(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [[sg.Text("Digite a idade a ser pesquisada: "), sg.InputText(key='idade')],
                  [sg.Text("Digite o nome a ser pesquisada: "), sg.InputText(key='nome')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_idade_nome = sg.Window("Pesquisa por idade e nome").Layout(layout)

    def open_pesquisa_idade_nome(self):
        b, v = self.window_pesquisa_idade_nome.Read()
        return b, v

    def close_pesquisa_idade_nome(self):
        self.window_pesquisa_idade_nome.close()

    def mostra_pesquisa_idade_nome(self, idade, nome):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.idade == int(idade) and pessoa.nome.upper() == nome.upper():
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça/Cor: " + pessoa.raca)]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_pesquisa_idade_nome = sg.Window("Pesquisa composta Idade e Nome").Layout(layout2)

    def open_mostra_pesquisa_idade_nome(self):
        b, v = self.window_pesquisa_idade_nome.Read()
        return b, v

    def close_mostra_pesquisa_idade_nome(self):
        self.window_pesquisa_idade_nome.close()

    def pesquisa_nacionalidade_nome(self):
        sg.ChangeLookAndFeel('Reddit')
        nacionalidades = ["Brasil", "Espanha", "Alemanha", "Estado Unidos", "França", "Portugal", "Canada"]
        layout = [[sg.Text("Escolha a nacionalidade: "), sg.Combo(nacionalidades, key='nacionalidade')],
                  [sg.Text("Digite o nome a ser pesquisada: "), sg.InputText(key='nome')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_nacionalidade_nome = sg.Window("Pesquisa composta").Layout(layout)

    def open_pesquisa_nacionalidade_nome(self):
        b, v = self.window_pesquisa_nacionalidade_nome.Read()
        return b, v

    def close_pesquisa_nacionalidade_nome(self):
        self.window_pesquisa_nacionalidade_nome.close()

    def mostra_pesquisa_nacionalidade_nome(self, nacionalidade, nome):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.nome.upper() == nome.upper() and pessoa.nacionalidade == nacionalidade:
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça/Cor: " + pessoa.raca)]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_pesquisa_nacionalidade_nome = sg.Window("Pesquisa Compostta").Layout(layout2)

    def open_mostra_pesquisa_pesquisa_nacionalidade_nome(self):
        b, v = self.window_pesquisa_nacionalidade_nome.Read()
        return b, v

    def close_mostra_pesquisa_nacionalidade_nome(self):
        self.window_pesquisa_nacionalidade_nome.close()

    def pesquisa_nacionalidade_idade(self):
        sg.ChangeLookAndFeel('Reddit')
        nacionalidades = ["Brasil", "Espanha", "Alemanha", "Estado Unidos", "França", "Portugal", "Canada"]
        layout = [[sg.Text("Escolha a nacionalidade: "), sg.Combo(nacionalidades, key='nacionalidade')],
                  [sg.Text("Digite a idade a ser pesquisada: "), sg.InputText(key='idade')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_nacionalidade_idade = sg.Window("Pesquisa composta").Layout(layout)

    def open_pesquisa_nacionalidade_idade(self):
        b, v = self.window_pesquisa_nacionalidade_idade.Read()
        return b, v

    def close_pesquisa_nacionalidade_idade(self):
        self.window_pesquisa_nacionalidade_idade.close()

    def mostra_pesquisa_nacionalidade_idade(self, nacionalidade, idade):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.idade == int(idade) and pessoa.nacionalidade == nacionalidade:
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça/Cor: " + pessoa.raca)]]
        layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
        self.window_pesquisa_nacionalidade_idade = sg.Window("Pesquisa Composta").Layout(layout2)

    def open_mostra_pesquisa_pesquisa_nacionalidade_idade(self):
        b, v = self.window_pesquisa_nacionalidade_idade.Read()
        return b, v

    def close_mostra_pesquisa_nacionalidade_idade(self):
        self.window_pesquisa_nacionalidade_idade.close()

    def pesquisa_all(self):
        sg.ChangeLookAndFeel('Reddit')
        nacionalidades = ["Brasil", "Espanha", "Alemanha", "Estado Unidos", "França", "Portugal", "Canada"]
        raca = ["Branco", "Negro", "Pardo"]
        layout = [[sg.Text("Escolha a nacionalidade: "), sg.Combo(nacionalidades, key='nacionalidade')],
                  [sg.Text("Digite a idade a ser pesquisada: "), sg.InputText(key='idade')],
                  [sg.Text("Digite o nome a ser pesquisado: "), sg.InputText(key='nome')],
                  [sg.Text("Escolha a raça/cor a ser pesquisada: "), sg.Combo(raca, key='raca')],
                  [sg.Button("Ok"), sg.Button("Voltar")]]
        self.window_pesquisa_all = sg.Window("Pesquisa composta").Layout(layout)

    def open_pesquisa_all(self):
        b, v = self.window_pesquisa_all.Read()
        return b, v

    def close_pesquisa_all(self):
        self.window_pesquisa_all.close()

    def mostra_pesquisa_all(self, nacionalidade, idade, nome, raca):
        sg.ChangeLookAndFeel('Reddit')
        layout2 = []
        for pessoa in self.__controlador.lista_todas_pessoa():
            if pessoa.idade == int(idade) and pessoa.nacionalidade == nacionalidade \
                    and pessoa.nome.upper() == nome.upper() and pessoa.raca == raca:
                layout2 += [[sg.Text("Nome: " + pessoa.nome), sg.Text("Nacionalidade: " + pessoa.nacionalidade),
                             sg.Text("Idade: " + str(pessoa.idade)), sg.Text("Raça/Cor: " + pessoa.raca)]]
                layout2 += [[sg.Exit("Sair"), sg.Button("Voltar")]]
                self.window_mostra_pesquisa_all = sg.Window("Pesquisa Composta").Layout(layout2)
            else:
                layout = [sg.Popup("Nao existem pessoas cadastradas")]
                self.window_mostra_pesquisa_all = sg.Window.layout(layout)


    def open_mostra_pesquisa_all(self):
        b, v = self.window_mostra_pesquisa_all.Read()
        return b, v

    def close_mostra_pesquisa_all(self):
        self.window_mostra_pesquisa_all.Close()
