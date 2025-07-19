

n1 = float(input('digite um número entre 0 e 100: '))
n2 = float(input('digite outro número diferente do anterior: '))


if n1 > n2:
    print(f'{n1} é maior que {n2}')

elif n1 < n2:
    print(f'{n2} é maior que {n1}')

else:
    print('por favor, digite um número.')