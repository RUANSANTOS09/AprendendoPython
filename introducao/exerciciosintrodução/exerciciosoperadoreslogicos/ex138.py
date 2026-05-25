idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
verificador = idade > 12 and altura > 1.40
print(f'Pode entrar? {verificador}')