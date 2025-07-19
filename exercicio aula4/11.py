#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#•	o produto do dobro do primeiro com metade do segundo .
#•	a soma do triplo do primeiro com o terceiro.
#•	o terceiro elevado ao cubo.

n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite um número inteiro: '))
n3 = float(input('digite um número Real: '))

soma = n1*2 + (n2/2)

soma2 = n1*3 + n3*3

soma3 = n3*n3*n3

print('o produto do dobro do primeiro com metade do segundo é: ', soma)

print('a soma do triplo do primeiro com o terceiro é: ', soma2)

print('o terceiro elevado ao cubo é: ', soma3)