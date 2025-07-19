n = (input('digite um número: '))

try:
    numero = int(n)

    if(n % 2 == 0):
        print('par')

    elif(n % 2 != 0):
        print('ímpar')


except:
    print("Deu ruim")
