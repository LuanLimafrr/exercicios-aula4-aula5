#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

print('Digite uma sequência de três números diferentes.')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

ns = [n1, n2, n3]

ns.sort(reverse=True)
print(ns)