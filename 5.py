#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#- A mensagem "Reprovado", se a média for menor do que sete;
#- A mensagem "Aprovado com Distinção", se a média for igual a dez.

try:

    n1 = float(input('Digite sua nota do 1º Bimestre: '))

    n2 = float(input('Digite sua nota do 2º Bimestre: '))

    n3 = float(input('Digite sua nota do 3º Bimestre: '))

    n4 = float(input('Digite sua nota do 4º Bimestre: '))

    med = (n1 + n2 + n3 + n4)/4


if med == 10.0:
    print(f'Sua média é {med} e você está APROVADO COM DISTINÇÃO!')


elif med >= 7.0:
    print(f'Sua média é {med} e você está APROVADO!')


else:
    print(f'Sua média é {med} e você está REPROVADO!')



except:
