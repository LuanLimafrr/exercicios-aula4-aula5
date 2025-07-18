#6. Faça um Programa que leia três números e mostre o maior deles.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('Digite um outro número: '))


if n1 == n2 == n3:
    print('Digite três números diferentes! ')


elif n1 > n2 and n3:
    print(f'{n1} é maior que {n2} e {n3}')

elif n2 > n1 and n3:
    print(f'{n2} é maior que {n1} e {n3}')

elif n3 > n2 and n1:
    print(f'{n3} é maior que {n2} e {n1}')
