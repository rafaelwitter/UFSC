class Calculadora:
    def somaNmr(n1,n2): 
        return n1+n2
    def multiplicaNmr(n1,n2):
        return n1*n2
def main():
    n1 = int(input())
    n2 = int(input())
    print(Calculadora.somaNmr(n1,n2))
    print(Calculadora.multiplicaNmr(n1,n2))
main()