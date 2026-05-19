lista = []
for i in range(5):
    numero = int(input('Digite um número: '))
    lista.append(numero)

maior = lista[0]
menor = lista[0]
for numero in lista:
    if(numero > maior):
        maior = numero
    if(numero < menor):
        menor = numero
print(lista)
print(maior)
print(menor)