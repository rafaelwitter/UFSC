def main():
    n = int(input("Digite o numero de provas: ")) 
    media(n)
def media(n):
    soma = 0
    ponderada = 0
    for i in range(n):
        peso = int(input("Digite o peso: "))
        nota = float(input("Digite a uma nota: "))
        soma += peso * nota 
        ponderada += peso
    media = soma / ponderada
    print("a media do aluno foi de {} e {}").format(media, situacao(media))
def situacao(media):   
    if media >= 6:
        return "o mesmo foi aprovado."
    elif media <= 4:
        return "o mesmo foi reprovado."
    else: return "o mesmo esta em rec."
main()