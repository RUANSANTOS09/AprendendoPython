numero = int(input('Digite um número: '))
for numero in range(0, numero + 1):
    if numero % 2 == 1:
        continue
    print(numero)