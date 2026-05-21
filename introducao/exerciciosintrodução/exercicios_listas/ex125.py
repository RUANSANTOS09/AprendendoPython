par = []
impar = []

for i in range(6):
    numero_digitado = int(input('Digite um número: '))
    if(numero_digitado % 2 == 0):
        par.append(numero_digitado)
    else:
        impar.append(numero_digitado)
print(f'Números pares: {par}')
print(f'Números impares: {impar}')