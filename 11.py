#11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
#e lhe contraram para desenvolver o programa que calculará os reajustes.

#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#- salários até R$ 280,00 (incluindo) : aumento de 20%
#- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#- o salário antes do reajuste;
#- o percentual de aumento aplicado;
#- o valor do aumento;
#- o novo salário, após o aumento.



try:
    print('Olá, vamos calcular seu aumento')

    sal = int(input('Digite aqui o seu salário: R$'))
    

    p1 = (5*sal) / 100
    p2 = (10*sal) / 100
    p3 = (15*sal) / 100
    p4 = (20*sal) / 100

    sal1 = sal+p1
    sal2 = sal+p2
    sal3 = sal+p3
    sal4 = sal+p4



    if sal <= 280:
        print(f'Salário antes do reajuste: {sal}\nPercentual de aumento aplicado: 20%\nValor do aumento: R${p4}\nSalário após o aumento: R${sal4}')

    elif 280 < sal < 700:
        print(f'Salário antes do reajuste: {sal}\nPercentual de aumento aplicado: 15%\nValor do aumento: R${p3}\nSalário após o aumento: R${sal3}')

    elif 700 < sal < 1500:
        print(f'Salário antes do reajuste: {sal}\nPercentual de aumento aplicado: 10%\nValor do aumento: R${p2}\nSalário após o aumento: R${sal2}')

    elif sal >= 1500:
        print(f'Salário antes do reajuste: {sal}\nPercentual de aumento aplicado: 5%\nValor do aumento: R${p1}\nSalário após o aumento: R${sal1}')


except:
    print('Digite um valor contábil.')

