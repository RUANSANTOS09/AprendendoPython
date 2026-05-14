nomes = input('Digite seu nome: ')
numero = int(input('Digite um numero: '))
for x in range(1, numero + 1):
    if x % 3 == 0:
        continue
    print(f'{x} - {nomes}')
