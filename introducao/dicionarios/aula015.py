# Dicionários


elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}
print(f'Elemento:  {elemento['nome']}')
print(f'Denseidade: {elemento['densidade']}')
print(f'O dicionario possui {len(elemento)} elementos')

# Atualizar uma entrada
elemento['grupos'] = 'Alcalinos'
print(f'Elemento:  {elemento['grupos']}')

# Adicionar uma entrada
elemento['período'] = 1
print(elemento)

# Exclusão de itens em dicionários
del elemento['período']
print(elemento)
#-----------------------------------------

#  Usando o metodo .items() para transformar o dicionario em uma lista de tuplas

print(elemento.items())
for i in elemento.items():
     print(i)
# Pegando as chaves do dicionario
print(elemento.keys())
for i in elemento.keys():
    print(i)
# Pegando os valores

print(elemento.values())
for i in elemento.values():
    print(i)

# Desempacotando as chaves e os valores simultaneamente
for i, j in elemento.items():
    print(f'{i}: {j}')
#-----------------------------------------
# Exclusão de todos os itens
elemento.clear()
print(elemento)

# Exclusão do dicionário da memória
# del elemento
# print(elemento)

