def main():
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    if n1 == n2:
        print("Eles sao iguais.")
    elif n1 > n2:
        print(n1, "eh o maior.")
    else: print(n2, "eh o maior.")
main()