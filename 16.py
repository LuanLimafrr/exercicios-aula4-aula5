#16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# #O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve 
# fazer pedir os demais valores, sendo encerrado;
#- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

print('Vamos calcular as raízes de uma equação do 2º grau! Digite abaixo os valores para a seguinte fórmula; ax2 + bx + c.')

a = float(input('Digite o valor de [A]: '))

if a == 0:
    print('Equação não é do segundo grau. Encerrando programa.')

else:
    b = float(input('Digite o valor de [B]: '))
    c = float(input('Digite o valor de [C]: '))


delta = b**2 - 4 * a * c

if delta < 0:
    print('A equação não tem raizes reais. Encerrando programa.')

elif delta == 0:
    raiz = - b / (2 * a)
    print(f'A equação possui apenas uma raiz real: {raiz}')

else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"A equação possui duas raízes reais: {raiz1:.2} e {raiz2:.2}")