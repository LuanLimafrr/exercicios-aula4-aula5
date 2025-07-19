#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

L = input('Digite alguma letra: ')
L = L.upper()#função maiúsculo

vogais = ['A','E','I','O','U']
cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']


if L in vogais:
    print(f'{L} é uma vogal!')

elif L in cons:
    print(f'{L} é uma consoante! ')

else:
    print('Digite Alguma letra.')
    