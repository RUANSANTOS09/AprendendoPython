numero = int(input('Digite um numero: '))
lista = []
for i in range(11):
    result = numero * i
    lista.append(result)
for i in range(11):
    result = numero * i
    print(f'{numero} x {i} = {result}')
print(lista)
