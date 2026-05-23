numero = (1,2,3,4,5,6)
lista = list(numero)
for i in range(len(lista)):
    if i % 2 == 0:
        lista[i] = 0

tupla = tuple(lista)
print(tupla)

