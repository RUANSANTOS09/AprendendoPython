numero = int(input('Digite um número: '))
for numero in range(1, numero + 1):
    if numero % 2 == 0:
        print(f'{numero} - Par')
    else:
        print(f'{numero} - impar')
