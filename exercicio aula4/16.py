#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

m2 = int(input('Digite quantos metros² tem a área a ser pintada: '))
m2 = round(m2)




if m2 <= 54:
  print('Uma lata de 18 litros será suficiente. Custo R$80,00')

elif m2 > 54:
  print('')