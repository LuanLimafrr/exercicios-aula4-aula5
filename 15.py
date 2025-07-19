#15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# #Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:

#- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#- Triângulo Equilátero: três lados iguais;
#- Triângulo Isósceles: quaisquer dois lados iguais;
#- Triângulo Escaleno: três lados diferentes;

print('Informe abaixo o valor dos 3 lados do triângulo.')

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

triangulo = l1 < l2+l3

if l1 == l2 == l3:
    print('Triangulo equilátero.')

elif l1 != l2 == l3:
    print('Triângulo isósceles.')

elif l3 != l2 == l1:
    print('Triângulo isósceles.')

elif l2 != l1 == l3:
    print('Triângulo isósceles.')

elif l1 != l2 != l3:
    print('Triângulo escaleno.')