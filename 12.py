#12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#- Desconto do IR:
#- Salário Bruto até 900 (inclusive) - isento
#- Salário Bruto até 1500 (inclusive) - desconto de 5%
#- Salário Bruto até 2500 (inclusive) - desconto de 10%
#- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#  Salário Bruto: (5 * 220)        : R$ 1100,00
#  (-) IR (5%)                     : R$   55,00  
#  (-) INSS ( 10%)                 : R$  110,00
#  FGTS (11%)                      : R$  121,00
#  Total de descontos              : R$  165,00
#  Salário Liquido                 : R$  935,00
"""
try:

    h = float(input('digite quantas horas você trabalha no mês: '))
    s = float(input('Digite quanto você ganha por hora: '))


    bruto = h*s

    ir5 = (5 * bruto) / 100
    ir10 = (10 * bruto) / 100
    ir20 = (20 * bruto) / 100

    inss = (10 * bruto) / 100

    sind = (3 * bruto) / 100

    fgts = (11 * bruto) / 100

    totaldesc = [ir5, ir10, ir20] + inss + sind 

    liq = bruto - totaldesc

    if bruto <= 900:
        print(f'Salário bruto: R${bruto}\n(-) IR (Isento): R$00\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')

    elif 900 < bruto <= 1500:
        print(f'Salário bruto: R${bruto}\n(-) IR (5%): R${ir5}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')

    elif 1500 < bruto <= 2500:
        print(f'Salário bruto: R${bruto}\n(-) IR (10%): R${ir10}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')

    elif bruto > 2500:
        print(f'Salário bruto: R${bruto}\n(-) IR (20%): R${ir20}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')



except:
    print('Digite um valor contábil.')


    """

h = float(input('digite quantas horas você trabalha no mês: '))
s = float(input('Digite quanto você ganha por hora: '))


bruto = h*s

ir5 = (5 * bruto) / 100
ir10 = (10 * bruto) / 100
ir20 = (20 * bruto) / 100

inss = (10 * bruto) / 100

sind = (3 * bruto) / 100

fgts = (11 * bruto) / 100

totaldesc =  + inss + sind 

liq = bruto - totaldesc

if bruto <= 900:
    print(f'Salário bruto: R${bruto}\n(-) IR (Isento): R$00\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: ISENTO \n Salário líquido: R${bruto} ')

elif 900 < bruto <= 1500:
    print(f'Salário bruto: R${bruto}\n(-) IR (5%): R${ir5}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')

elif 1500 < bruto <= 2500:
    print(f'Salário bruto: R${bruto}\n(-) IR (10%): R${ir10}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')

elif bruto > 2500:
    print(f'Salário bruto: R${bruto}\n(-) IR (20%): R${ir20}\n(-) INSS (10%): R${inss}\nFGTS (11%): R${fgts}\nTotal de descontos: R${totaldesc}\n Salário líquido: R${liq} ')
