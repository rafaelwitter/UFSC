from computador import Computador

pc = Computador('DELL', 12, "INTEL", True, 1)
pc.insere_sistema_operacional('Linux')
print(pc)
pc.sistemas_operacionais()
pc.boot(0)
pc.liga()

pc2 = Computador('Acer', 12, "Intel", True, 1)
pc2.insere_sistema_operacional('windows')
print(pc2)
pc2.sistemas_operacionais()
pc2.boot(0)
pc2.liga()

pc.escrever_mensagem("Teste")
pc.escrever_mensagem("teste2")
pc.enviar_mensagem(pc2)
pc2.receber_mensagem()
pc2.ler_mensagens()
