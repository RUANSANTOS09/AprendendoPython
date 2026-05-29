produtos = {
    'keyboard': 5,
    'mouse': 5,
    'motherboard': 6,
    'ram_memory': 2
}
print('======== Estoque Original ========')
for product, quantity in produtos.items():
    print(f'{product}: {quantity}')

print('======== Estoque Atualizado ========')
produtos['ssd'] = 3
del produtos['keyboard']
for product, quantity in produtos.items():
    print(f'{product}: {quantity}')