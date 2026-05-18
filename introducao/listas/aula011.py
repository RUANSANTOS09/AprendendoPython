# Lista: representa uma sequência de valores
from introducao.exerciciosintrodução.exercicios_lacos_encadeados.ex087 import planetas

# Sintaze: nome_lista = [valores]

#        0    1   2   3   4
#notas = [5.0,7.6,4.7,8.0,9.7]
#print(notas[2])

n1 = [9, 6.6 , 4.7]
n2 = [5.6, 7, 9]
valores = n1 + n2

valores[0] = 6 # Alterando valor da lista
print(type(valores))
print(valores[-1]) # Acessando o ultimo item da lista
print(valores[-2]) # Acessando o penultimo item da lista
print(valores[0: 4]) # Esse comando indica que vai imprimir os valores do indice 0 ate 4
print('Essa lista tem',len(valores), 'elementos') # Mostra o comprimento da lista
print(sorted(valores, reverse=True)) # Ordem decrescente
print(sorted(valores)) # Ordem crescente
print(sum(valores)) # Soma todos os valores da lista
print(min(valores)) # Imprime o valor minimo da lista
print(max(valores)) #  Imprime o valor maximo  da lista

valores.append(10)
valores.pop(3)
print(valores)
print(valores)
valores.insert(3, 10)
print(valores)
print(12 in valores)

planetas = ['Terra','Urano','Plutao','Saturno','Jupiter']
for planeta in planetas:
    print(planeta)
