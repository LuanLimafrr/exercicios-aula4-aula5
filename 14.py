#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo:

#Média de Aproveitamento
#- Entre 9.0 e 10.0 : A
#- Entre 7.5 e 9.0 : B
#- Entre 6.0 e 7.5 : C
#- Entre 4.0 e 6.0 : D
#- Entre 4.0 e zero : E


print('Vamos calcular sua média!')

n1 = float(input('Por favor, digite sua nota em Janeiro: '))
n2 = float(input('Por favor, digite sua nota em Fevereiro: '))
n3 = float(input('Por favor, digite sua nota em Março: '))
n4 = float(input('Por favor, digite sua nota em Abril: '))
n5 = float(input('Por favor, digite sua nota em Maio: '))
n6 = float(input('Por favor, digite sua nota em Junho: '))

media = (n1+n2+n3+n4+n5+n6) / 6

if 9.0 <= media <= 10.0:
    print(f'Sua média é {media:.2F} e sua nota é (A) e você está APROVADO')

elif 7.5 <= media <= 9.0:
    print(f'Sua média é {media:.2F} e sua nota é (B) e você está APROVADO')

elif 6.0 <= media <= 7.5:
    print(f'Sua média é {media:.2F} e sua nota é (C) e você está APROVADO')

elif 4.0 <= media <= 6.0:
    print(f'Sua média é {media:.2F} e sua nota é (D) e você está REPROVADO')  

elif 4.0 <= media <= 0:
    print(f'Sua média é {media:.2F} e sua nota é (E) e você está REPROVADO')

else:
    print('Por favor, informe as notas de forma correta!')