soma = 0
while True:
    num = int(input('Digite um número (0 para encerrar): '))
    if( num == 0):
        break
    soma += num

print(f'A soma de todos os número digitados é igual a {soma}')