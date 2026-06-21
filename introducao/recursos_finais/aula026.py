# Trocar valores entre duas variaveis
var1 = 12
var2 = 31
# var2, var1 = var1, var2
# print(f'var1: {var1}, var2: {var2}')

# Operador Condicional Ternário

# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2, var1)[var1 < var2]}')

# Generators

# valores = [1,3,5,6,7,9,12,13,15]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()
# bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
# for i,bebida in enumerate(bebidas, start= 1):
#   print(f'{i} - {bebida}')
#
#
# temperaturas = [-1,34,-12,3,6,8,1,-5,10]
# total = 0
# for i, t in enumerate(temperaturas, start= 1):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t}°C.')

# Gerenciamento de contexto com with

try:
   a = open('frutas.txt', 'r', encoding='utf8')
   print(a.read())
except IOError:
    print('Não foi possível encontrar o arquivo')
else:
    a.close()


with open('frutas.txt', 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        print(linha, end = '')