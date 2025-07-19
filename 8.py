#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão 
#é sempre pelo mais barato.


preco1 = float(input('Digite o valor do item: ')) 
preco2 = float(input('Digite o valor do item: '))
preco3 = float(input('Digite o valor do item: '))


barato = [preco1, preco2, preco3]
baratinho = min(barato)


print(f'o produto mais indicado é o {baratinho}')