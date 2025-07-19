def somar(a,b):
    print('resultado(+):', a+b)

def somar1(a,b,c):
    print('resultado (+):', a+b+c)

def subtrair(x,y):
    print('resultado(-):', x-y)
    
def multiplicacao(n,m):
    resultado = n * m
    print('Multiplicação:',resultado)


def porcentagem(o, i,):
    print('resultado (%):',o*i/100)


def entrada():
    n = input('digite seu nome: ')
    print('Boa noite,',n)



#chamada de função
    
somar(5,2)

somar1(1,4,6)

subtrair(5,2)

multiplicacao(5,2)

porcentagem(50, 100)

entrada()
