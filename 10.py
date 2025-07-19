#10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.



print('Olá, em qual turno você estuda?\nM - Matutino\nV - Vespertino\nN - Noturno.')

hora = (input('DIGITE AQUI => ')).strip().lower()

if hora == "m":
    print('Bom dia!')


elif hora == "v":
    print('Boa tarde!')


elif hora == "n":
    print('Boa noite!')


 