soma = 0
while True:
    numero = int(input('Digite um número (0 para encerrar): '))
    if( numero == 0):
        break
    else:
        soma += numero


print(f'Soma de todos números digitados: {soma}')
