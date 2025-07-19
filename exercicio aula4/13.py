#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas:
#•	Para homens: (72.7*h) - 58
#•	Para mulheres: (62.1*h) - 44.7

alt = float(input('Digite sua altura: '))

peso1 = (72.7*alt) - 58
peso2 = (62.1*alt) - 44.7


sexo = input('Voce é homem ou mulher? ')
sexo = sexo.lower()

if sexo == 'homem':
    print(peso1)

elif sexo == 'mulher':
    print(peso2)








