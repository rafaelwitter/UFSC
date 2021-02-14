from view.tela_geral import *
from control.controle_pessoa import *
import PySimpleGUI as sg


class ControladorGeral:
    def __init__(self):
        self.controlador_pessoas = ControladorPessoa(self)
        self.tela = TelaPrincipal(self)
        self.tela_pesquisa = TelaPesquisa(self)
        print(self.controlador_pessoas.interseccao(cor="Branco", nacio="Brasil"))
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

    def incluir_pessoa(self, nome, idade, nacionalidade, raca):
        self.controlador_pessoas.cria_pessoa(nome, idade, nacionalidade, raca)

    def lista_todas_pessoa(self):
        return self.controlador_pessoas.busca_todas()

    def lista_pesquisa_unica(self, nmr, nome):
        t = {1: self.tela_pesquisa.mostra_pesquisa_nome,
             2: self.tela_pesquisa.mostra_pesquisa_nacionalidade,
             3: self.tela_pesquisa.mostra_pesquisa_idade,
             4: self.tela_pesquisa.mostra_pesquisa_cor}
        o = {1: self.tela_pesquisa.open_mostra_pesquisa_nome,
             2: self.tela_pesquisa.open_mostra_pesquisa_nacionalidade,
             3: self.tela_pesquisa.open_mostra_pesquisa_idade,
             4: self.tela_pesquisa.open_mostra_pesquisa_cor}
        while True:
            self.tela.window_pesquisa.hide()
            if nmr == 1:
                t[nmr](nome)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_mostra_pesquisa_nome()
                    break
                elif b == "Sair" or sg.Exit():
                    exit(0)
            elif nmr == 2:
                t[nmr](nome)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_pesquisa_nacionalidade()
                    self.tela_pesquisa.close_mostra_pesquisa_nacionalidade()
                    break
                elif b == "Sair" or sg.Exit():
                    exit(0)
            elif nmr == 3:
                t[nmr](nome)
                b, v = o[nmr]()
                if b == "Sair" or sg.Exit():
                    exit(0)
                if b == "Voltar":
                    self.tela_pesquisa.close_mostra_pesquisa_idade()
                    self.tela.window_pesquisa.un_hide()
                    break
            elif nmr == 4:
                t[nmr](nome)
                b, v = o[nmr]()
                if b == "Sair" or sg.Exit():
                    exit(0)
                if b == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_pesquisa_cor()
                    break

    def pesquisa_switch(self, nmr):
        t = {1: self.tela_pesquisa.pesquisa_nome, 2: self.tela_pesquisa.pesquisa_idade,
             3: self.tela_pesquisa.pesquisa_nacionalidade, 4: self.tela_pesquisa.pesquisa_cor}
        o = {1: self.tela_pesquisa.open_pesquisa_nome, 2: self.tela_pesquisa.open_pesquisa_idade,
             3: self.tela_pesquisa.open_pesquisa_nacionalidade, 4: self.tela_pesquisa.open_pesquisa_cor}
        while True:
            if nmr == 1:
                self.tela.window_pesquisa.hide()
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.tela_pesquisa.close_pesquisa_nome()
                    self.lista_pesquisa_unica(1, value['nome'])
                elif button == "Voltar":
                    self.tela_pesquisa.close_mostra_pesquisa_nome()
                    self.tela.window_pesquisa.un_hide()
                    break
                else:
                    self.tela.window.un_hide()
                    break
            elif nmr == 2:
                self.tela.window_pesquisa.hide()
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.lista_pesquisa_unica(3, int(value['idade']))
                elif button == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_pesquisa_idade()
                    break
            elif nmr == 3:
                self.tela.window_pesquisa.hide()
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.lista_pesquisa_unica(2, str(value[0]))
                elif button == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_pesquisa_nacionalidade()
                    break
            elif nmr == 4:
                self.tela.window_pesquisa.hide()
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.lista_pesquisa_unica(4, str(value['cor']))
                elif button == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_pesquisa_cor()
                    break
            else:
                break

    def lista_pesquisa_multipla(self, nmr, idade=None, nome=None, nacionalidade=None, raca=None):
        t = {1: self.tela_pesquisa.mostra_pesquisa_idade_nome,
             2: self.tela_pesquisa.mostra_pesquisa_nacionalidade_nome,
             3: self.tela_pesquisa.mostra_pesquisa_nacionalidade_idade,
             4: self.tela_pesquisa.mostra_pesquisa_all,
             5: self.tela_pesquisa.mostra_pesquisa_cor_nacionalidade}
        o = {1: self.tela_pesquisa.open_pesquisa_idade_nome,
             2: self.tela_pesquisa.open_pesquisa_nacionalidade_nome,
             3: self.tela_pesquisa.open_pesquisa_nacionalidade_idade,
             4: self.tela_pesquisa.open_pesquisa_all,
             5: self.tela_pesquisa.open_pesquisa_cor_nacionalidade}
        while True:
            if nmr == 1:
                t[nmr](idade, nome)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela_pesquisa.close_mostra_pesquisa_idade_nome()
                    break
                if b == "Ok":
                    self.tela.window_pesquisa_multipla.hide()
            elif nmr == 2:
                self.tela_pesquisa.window_pesquisa_nacionalidade_idade.hide()
                t[nmr](idade)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela_pesquisa.window_pesquisa_nacionalidade_idade.un_hide()
                    self.tela_pesquisa.close_mostra_pesquisa_nacionalidade_nome()
                    break
            elif nmr == 3:
                t[nmr](nacionalidade, idade)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela.window_pesquisa.un_hide()
                    self.tela_pesquisa.close_mostra_pesquisa_nacionalidade_idade()
                    break
            elif nmr == 4:
                t[nmr](nacionalidade, idade, nome, raca)
                b, v = o[nmr]()
                if b == "Voltar":
                    self.tela_pesquisa.close_pesquisa_all()
                    self.tela.window.un_hide()
                    break
            elif nmr == 5:
                pessoas = self.controlador_pessoas.interseccao(cor=raca, nacio=nacionalidade)
                t[nmr](pessoas)
                b, v = o[nmr]()
                if b == "Ok":
                    self.tela.window_pesquisa_multipla.hide()
                elif b == "Voltar":
                    self.tela_pesquisa.close_pesquisa_all()
                    self.tela.window.un_hide()
                    break
            else:
                self.tela.window_pesquisa.un_hide()

    def pesquisa_mutipla_switch(self, nmr):
        t = {1: self.tela_pesquisa.pesquisa_idade_nome, 2: self.tela_pesquisa.pesquisa_nacionalidade_nome,
             3: self.tela_pesquisa.pesquisa_nacionalidade_idade, 4: self.tela_pesquisa.pesquisa_all,
             5: self.tela_pesquisa.pesquisa_cor_nacionalidade}
        o = {1: self.tela_pesquisa.open_pesquisa_idade_nome, 2: self.tela_pesquisa.open_pesquisa_nacionalidade_nome,
             3: self.tela_pesquisa.open_pesquisa_nacionalidade_idade, 4: self.tela_pesquisa.open_pesquisa_all,
             5: self.tela_pesquisa.open_pesquisa_cor_nacionalidade}
        while True:
            if nmr == 1:
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.tela_pesquisa.window_pesquisa_idade_nome.hide()
                    self.lista_pesquisa_multipla(1, idade=int(value['idade']), nome=str(value['nome']))
                else:
                    self.tela.window_pesquisa_multipla.hide()
                    self.tela_pesquisa.close_mostra_pesquisa_idade_nome()
                    break
            elif nmr == 2:
                t[nmr]()
                button, value = o[nmr]()
                if button == "Ok":
                    self.tela_pesquisa.mostra_pesquisa_nacionalidade_nome(str(value['nacionalidade']), str(value['nome']))
                else:
                    self.tela.window_pesquisa_multipla.un_hide()
                    self.tela_pesquisa.close_pesquisa_nacionalidade_idade()
                    break
            elif nmr == 3:
                t[nmr]()
                b, v = o[nmr]()
                if b == "Ok":
                    self.lista_pesquisa_multipla(3, nacionalidade=str(v['nacionalidade']), idade=int(v['idade']))
                else:
                    self.tela.window_pesquisa_multipla.un_hide()
                    self.tela_pesquisa.close_pesquisa_nacionalidade_idade()
                    break
            elif nmr == 4:
                t[nmr]()
                b, v = o[nmr]()
                if b == "Ok":
                    self.lista_pesquisa_multipla(4, nacionalidade=str(v['nacionalidade']), idade=int(v['idade']),
                                                 nome=str(v['nome']))
                else:
                    self.tela.window_pesquisa_multipla.un_hide()
                    self.tela_pesquisa.close_pesquisa_all()
                    break
            elif nmr == 5:
                t[nmr]()
                b, v = o[nmr]()
                if b == "Ok":
                    self.lista_pesquisa_multipla(5, nacionalidade=str(v['nacionalidade']), raca=str(v['cor']))
                else:
                    self.tela_pesquisa.close_pesquisa_cor_nacionalidade()
                    break
            else:
                break

    def switch_case(self, nmr):
        m = {1: self.tela.tela_todas_pessoas, 2: self.tela.tela_inclui_pessoa, 3: self.tela.pesquisa_pessoas,
             4: self.tela.multipla_pesquisa}
        o = {1: self.tela.open_pessoas, 2: self.tela.open_inclui, 3: self.tela.open_pesquisa,
             4: self.tela.open_multipla_escolha}
        while True:
            if nmr == 1:
                m[1]()
                button, value = o[1]()
                if button == "Voltar":
                    self.tela.window.un_hide()
                    self.tela.close_pessoas()
                    break
                elif button == "Excluir":
                    for pessoa in self.controlador_pessoas.busca_todas():
                        if value[pessoa.id]:
                            self.controlador_pessoas.idDAO.remove(pessoa.id)
                            sg.Popup("Cliente removido!")
                            self.tela.window_pessoas.close()
                else:
                    exit(0)
            elif nmr == 2:
                m[2]()
                button, value = o[2]()
                if button == "Adicionar":
                    nome = str(value[0])
                    idade = int(value[1])
                    nacionalidade = str(value[2])
                    self.incluir_pessoa(nome, idade, nacionalidade, str(value[3]))
                    sg.Popup("Pessoa cadastrada")
                    self.tela.close_inclui()
                    self.tela.window.un_hide()
                elif button == "Voltar":
                    self.tela.window.un_hide()
                    self.tela.close_inclui()
                    break
            elif nmr == 3:
                self.tela.window.hide()
                m[3]()
                button, value = o[3]()
                if button == "Ok":
                    if value['nacionalidade']:
                        self.pesquisa_switch(3)
                        self.tela.close_pesquisa_pessoas()
                    elif value['idade']:
                        self.pesquisa_switch(2)
                        self.tela.close_pesquisa_pessoas()
                    elif value['nome']:
                        self.pesquisa_switch(1)
                        self.tela.close_pesquisa_pessoas()
                    elif value['cor']:
                        self.pesquisa_switch(4)
                else:
                    self.tela.window.un_hide()
                    self.tela.close_pesquisa_pessoas()
                    break
            elif nmr == 4:
                m[4]()
                button, value = o[4]()
                if button == "Ok":
                    if value['nome_idade']:
                        self.tela.window_pesquisa_multipla.hide()
                        self.pesquisa_mutipla_switch(1)
                    elif value['all']:
                        self.tela.window_pesquisa_multipla.hide()
                        self.pesquisa_mutipla_switch(4)
                    elif value['idade_nacionalidade']:
                        self.tela.window_pesquisa_multipla.hide()
                        self.pesquisa_mutipla_switch(3)
                    elif value['nome_nacionalidade']:
                        self.tela.window_pesquisa_multipla.hide()
                        self.pesquisa_mutipla_switch(2)
                    elif value['raca_nacionalidade']:
                        self.tela.window_pesquisa_multipla.hide()
                        self.pesquisa_mutipla_switch(5)
                else:
                    self.tela.window_pesquisa_multipla.un_hide()
                    break

    def get_pessoa(self, pessoa):
        return self.controlador_pessoas.busca_especifica(pessoa)
