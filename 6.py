#6. Faça um Programa que leia três números e mostre o maior deles.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um outro número: '))

numero = [n1, n2, n3]

valor_max = max(numero)

print(f'o valor maior é o {valor_max}')

