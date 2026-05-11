idade = int(input('Qual a sua idade? '))
altura = float(input('Qual a sua altura? '))
verificador = (idade >= 12) and (altura >= 1.40)
print('Pode entrar no evento? {}'.format(verificador))