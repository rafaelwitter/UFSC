################################
# CALCULAR MDC ENTRE OS NUMEROS#
################################
def main():
    n = int(input("Digite um numero para sequencia: "))
    n1 = int(input("Digite um numero: "))
    
    for i in range(1,n):
        n2 = int(input("Digite um numero: "))
        d = mdc(n1,n2)
        n1= d
    print(n1)

def mdc(n1,n2):
    M = n1
    if n2<M:
        M = n2
    while not (n1 % M == 0 and n2 % M == 0):
        M -=1
    return M
main()    

