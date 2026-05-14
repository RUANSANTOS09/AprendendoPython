numero = int(input('Digite um número: '))

for x in range(1,11):
    calc = numero * x
    print(f'{numero} x {x} = {calc}')
    x += 1