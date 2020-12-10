from ESTRUTURA_DADOS.trabalho_final.view.main import Geral
from ESTRUTURA_DADOS.trabalho_final.control.controle_pessoa import ControladorPessoa
import PySimpleGUI as sg


class ControladorGeral:
    def __init__(self):
        self.controlador_pessoas = ControladorPessoa(self)
        self.tela = Geral(self)
        self.abre_tela()

    def abre_tela(self):
        self.tela.tela_inicio()
        while True:
            buttons, values = self.tela.open_inicio()
            if buttons == "Ver todas as pessoas":
                self.switch_case(1)
            elif buttons == "Adicionar pessoa":
                self.switch_case(2)
            elif buttons == "Pesquisas unicas":
                self.switch_case(3)
            elif buttons == "Pesquisas multiplas":
                self.switch_case(4)
            else:
                exit(0)

    def incluir_pessoa(self, nome, idade, nacionalidade):
        self.controlador_pessoas.criar_pessoa(nome, idade, nacionalidade)

    def lista_pessoas_nacionalidade(self):
        return self.controlador_pessoas.busca_todas_nacionalidade()

    def lista_todas_pessoa(self):
        return self.controlador_pessoas.busca_todas()

    def lista_por_idade(self):
        return self.controlador_pessoas.busca_por_idade()

    def lista_por_nome(self):
        return self.controlador_pessoas.busca_por_nome()

    def lista_pesquisa_unica(self, nmr, nome):
        t = {1: self.tela.mostra_pesquisa_nome, 2: self.tela.mostra_pesquisa_nacionalidade,
             3: self.tela.mostra_pesquisa_idade}
        o = {1: self.tela.open_mostra_pesquisa_nome, 2: self.tela.open_mostra_pesquisa_nacionalidade,
             3: self.tela.open_mostra_pesquisa_idade}
        self.tela.window_pesquisa.hide()
        if nmr == 1:
            t[nmr](nome)
            b, v = o[nmr]()
            if b == "Sair" or sg.Exit():
                exit(0)
            if b == "Voltar":
                self.tela.window_pesquisa.un_hide()
                self.tela.close_mostra_pesquisa_nome()
        elif nmr == 2:
            t[nmr](nome)
            b, v = o[nmr]()
            if b == "Sair" or sg.Exit():
                exit(0)
            if b == "Voltar":
                self.tela.window_pesquisa.un_hide()
                self.tela.close_mostra_pesquisa_nacionalidade()
        elif nmr == 3:
            t[nmr](nome)
            b, v = o[nmr]()
            if b == "Sair" or sg.Exit():
                exit(0)
            if b == "Voltar":
                self.tela.window_pesquisa.un_hide()
                self.tela.close_mostra_pesquisa_idade()

    def pesquisa_switch(self, nmr):
        t = {1: self.tela.pesquisa_nome, 2: self.tela.pesquisa_idade,
             3: self.tela.pesquisa_nacionalidade}
        o = {1: self.tela.open_pesquisa_nome, 2: self.tela.open_pesquisa_idade,
             3: self.tela.open_pesquisa_nacionalidade}
        if nmr == 1:
            t[nmr]()
            button, value = o[nmr]()
            if button == "Ok":
                self.lista_pesquisa_unica(1, value['nome'])
            else:
                self.tela.window.un_hide()
        elif nmr == 2:
            t[nmr]()
            button, value = o[nmr]()
            if button == "Ok":
                self.lista_pesquisa_unica(3, int(value['idade']))
        elif nmr == 3:
            t[nmr]()
            button, value = o[nmr]()
            if button == "Ok":
                self.lista_pesquisa_unica(2, str(value[0]))

    def lista_pesquisa_multipla(self, nmr, idade=None, nome=None, nacionalidade=None):
        t = {1: self.tela.mostra_pesquisa_idade_nome, 2: self.tela.mostra_pesquisa_nacionalidade_nome,
             3: self.tela.mostra_pesquisa_nacionalidade_idade, 4: self.tela.mostra_pesquisa_all}
        o = {1: self.tela.open_mostra_pesquisa_idade_nome, 2: self.tela.open_pesquisa_nacionalidade_nome,
             3: self.tela.open_mostra_pesquisa_pesquisa_nacionalidade_idade, 4: self.tela.open_mostra_pesquisa_all}
        if nmr == 1:
            t[nmr](idade, nome)
            b, v = o[nmr]()
        elif nmr == 2:
            t[nmr](idade)
            b, v = o[nmr]()
        elif nmr == 3:
            t[nmr](nacionalidade, idade)
            b, v = o[nmr]()
        elif nmr == 4:
            t[nmr](nacionalidade, idade, nome)
            b, v = o[nmr]()

    def pesquisa_mutipla_switch(self, nmr):
        t = {1: self.tela.pesquisa_idade_nome, 2: self.tela.pesquisa_nacionalidade_nome,
             3: self.tela.pesquisa_nacionalidade_idade, 4: self.tela.pesquisa_all}
        o = {1: self.tela.open_pesquisa_idade_nome, 2: self.tela.open_pesquisa_nacionalidade_nome,
             3: self.tela.open_pesquisa_nacionalidade_idade, 4: self.tela.open_pesquisa_all}
        if nmr == 1:
            t[nmr]()
            button, value = o[nmr]()
            if button == "Ok":
                self.lista_pesquisa_multipla(1, idade=int(value['idade']), nome=str(value['nome']))
            else:
                self.tela.window_pesquisa_multipla.un_hide()
                self.tela.close_mostra_pesquisa_idade_nome()
        elif nmr == 2:
            t[nmr]()
            button, value = o[nmr]()
            if button == "Ok":
                self.tela.mostra_pesquisa_nacionalidade_nome(str(value['nacionalidade']), str(value['nome']))
            else:
                self.tela.window_pesquisa_multipla.un_hide()
                self.tela.close_pesquisa_nacionalidade_idade()
        elif nmr == 3:
            t[nmr]()
            b, v = o[nmr]()
            if b == "Ok":
                self.lista_pesquisa_multipla(3, nacionalidade=str(v['nacionalidade']), idade=int(v['idade']))
            else:
                self.tela.window_pesquisa_multipla.un_hide()
                self.tela.close_pesquisa_nacionalidade_idade()
        elif nmr == 4:
            print("OI")
            t[nmr]()
            b, v = o[nmr]()
            if b == "Ok":
                self.lista_pesquisa_multipla(4, nacionalidade=str(v['nacionalidade']), idade=int(v['idade']),
                                             nome=str(v['nome']))
            else:
                self.tela.window_pesquisa_multipla.un_hide()
                self.tela.close_pesquisa_all()

    def switch_case(self, nmr):
        m = {1: self.tela.tela_todas_pessoas, 2: self.tela.tela_inclui_pessoa, 3: self.tela.pesquisa_pessoas,
             4: self.tela.multipla_pesquisa}
        o = {1: self.tela.open_pessoas, 2: self.tela.open_inclui, 3: self.tela.open_pesquisa,
             4: self.tela.open_multipla_escolha}
        if nmr == 1:
            m[1]()
            button, value = o[1]()
            if button == "Voltar":
                self.tela.window.un_hide()
                self.tela.window_pessoas.Close()
            else:
                exit(0)
        elif nmr == 2:
            m[2]()
            button, value = o[2]()
            if button == "Adicionar":
                nome = str(value[0])
                idade = int(value[1])
                nacionalidade = str(value[2])
                self.incluir_pessoa(nome, idade, nacionalidade)
                sg.Popup("Pessoa cadastrada")
                self.tela.close_inclui()
                self.tela.window.un_hide()
            elif button == "Voltar":
                self.tela.window.un_hide()
                self.tela.close_inclui()
        elif nmr == 3:
            self.tela.window.hide()
            m[3]()
            button, value = o[3]()
            if button == "Ok":
                if value['nacionalidade']:
                    self.pesquisa_switch(3)
                elif value['idade']:
                    self.pesquisa_switch(2)
                elif value['nome']:
                    self.pesquisa_switch(1)
            else:
                self.tela.window.un_hide()
        elif nmr == 4:
            m[4]()
            button, value = o[4]()
            if button == "Ok":
                if value['nome_idade']:
                    self.pesquisa_mutipla_switch(1)
                elif value['all']:
                    self.pesquisa_mutipla_switch(4)
                elif value['idade_nacionalidade']:
                    self.pesquisa_mutipla_switch(3)
                elif value['nome_nacionalidade']:
                    self.pesquisa_mutipla_switch(2)
            else:
                self.tela.window_pesquisa_multipla.Close()
                self.tela.window.un_hide()