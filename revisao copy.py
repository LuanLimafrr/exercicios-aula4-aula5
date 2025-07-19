# módulo
#print(12 %4 == 0)

n = float(input('digite um valor numérico '))
n = round(n)


if n == 0:
  print('número inválido')

elif n %2 == 1:
  print('o número é ímpar.')

else:
  n %2 == 0
  print(f'o número é par')

