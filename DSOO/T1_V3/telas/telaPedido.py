import PySimpleGUI as sg
class TelaPedido:
    def __init__(self):
        self.__window = None
        self.__window_pedido = None
        self.init_components()

    def init_components(self):
        layout = [
 		[sg.Text('PEDIDO', font=("Helvetica", 25))],
		[sg.Text('Escolha as opcoes desejada: ', font=("Helvetica", 20))],
        [sg.Button('Adicionar arroz'), sg.Button('Adicionar feijao'),
        sg.Button('Adicionar macarrao'), sg.Button('Adicionar carne')],
        [sg.Button('Finalizar pedido'), sg.Button('Cancelar')]
 		]
        self.__window = sg.Window('Larikas', default_element_size=(50,20)).Layout(layout)

        layout_pedido = [
            [sg.Multiline(autoscroll=True, )]
        ]

    def open(self):
        teste = []
        while True:
            eventos, dados = self.__window.Read()
            if eventos != 'Finalizar pedido':
                self.show_msg('Obrigado!', 'Produto adicionado com sucesso.')
                teste.append(eventos)
            else: break
        self.__window.Close()
        return eventos, teste

    def show_msg(self, title: str, msg: str):
        sg.Popup(title, msg)

    def init_pedidos(self, pedidos):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Pedidos cadastrados')],
            [sg.Listbox(values=pedidos, size=(100, 20))],
            [sg.Button('Voltar')]
        ]
        self.__window_pedido = sg.Window('Pedidos', default_element_size=(100,150), resizable=True).Layout(layout)

    def open_pedidos(self, pedidos):
        self.init_pedidos(pedidos)
        botoes, dados = self.__window_pedido.Read()
        if botoes == 'Voltar':
            self.__window_pedido.Close()
