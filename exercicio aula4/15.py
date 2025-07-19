h = float(input('digite quantas horas você trabalha no mês: '))
s = float(input('Digite quanto você ganha por hora: '))

bruto = h*s

ir = (11 * bruto) / 100

inss = (8 * bruto) / 100

sind = (5 * bruto) / 100

liq = bruto - ir - inss - sind


print(f'Salário Bruto : R${bruto}.\nIr (11%) : R${ir}.\nInss (8%) : R${inss}.\nSindicato (5%) : R${sind}.\nSalário líquido : R${liq} ')
