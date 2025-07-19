print('Olá, vou precisar que você me diga sua nota nos 4 últimos bimestres!')

n1 = float(input('bimestre 1: '))
n2 = float(input('bimestre 2: '))
n3 = float(input('bimestre 3: '))
n4 = float(input('bimestre 4: '))

soma = n1 + n2 + n3 + n4 
divisao = soma / 4

print(f"Sua média é : ", divisao)
