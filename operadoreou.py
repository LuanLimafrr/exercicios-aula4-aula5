dinheiro = True
senha = True

#   and = &

if dinheiro == True and senha == True:
    print('Sacar.')

elif dinheiro == True and senha == False:
    print('Senha inválida.')
elif dinheiro == False and senha == True:
    print('Saldo insuficiente.')
elif dinheiro == False & senha == False:
    print('Senha inválida.')


"""
dinheiro / senha
      v  |   v
      v  |   f
      f  |   v
      f  |   f

      possíveis possibilidades com 2 condições, sendo que 2² (ELEVADO A 2 POIS SÃO 2 CONDIÇÕES |DINHEIRO E SENHA)
"""