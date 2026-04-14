#Algoritmo serie  N! / 1 + (N - 1)! / 3 + (N - 2)! / 5 .... + (1)! / x
#Declarar
N: int = 0
cta: int = 0
fat: int = 1
serie: float = 0.0
impar: int = 1


def somar_serie(sr, imp):
    global fat
    global N

    sr = (fat / imp) + sr
    imp = imp + 2
    N = N - 1

    return sr , imp



def fatoriador(Núm):
    conta: int = Núm
    fatorial: int = 1

    while (conta > 1):
        fatorial = fatorial * conta
        conta = conta - 1

    return fatorial


def comparador(Num):
    while (Num < 2 or Num > 7):
        Num = int(input("VALOR INVÁLIDO. Digite novamente, dentro da condição estabelecida: "))
    return Num


def main():
    global N
    global fat
    global serie
    global impar
    
    N = int(input("Digite um valor para N entre 2 e 7: "))
    if (N < 2 or N > 7):
        N = comparador(N)
    while (N != 0):
        fat = fatoriador(N)
        serie, impar = somar_serie(serie, impar)

    print("O valor da série é de: " , serie)

    
    
        






if (__name__ == '__main__'):
    main()