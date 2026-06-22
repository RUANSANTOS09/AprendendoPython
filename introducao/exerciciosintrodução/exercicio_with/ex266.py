r = input('Digite um termo: ')
with open('product.txt', 'r', encoding='utf-8') as file:
    for index, value in enumerate(file,start=1):
        if r in value:
         print(f'Encontrado na posição {index}: {value}')