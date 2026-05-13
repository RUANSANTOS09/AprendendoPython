soma = 0
while True:
    num = int(input('Digite um número(Digite 0 para sair): '))
    if(num == 0):
        break
    soma += num

print(f'Soma de todos os números digitados. {soma}')