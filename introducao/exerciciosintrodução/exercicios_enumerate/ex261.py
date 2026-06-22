product = ['mouse', 'teclado', 'monitor', 'webcam', 'notebook']
for number, product in enumerate(product, start=1):
    if number % 2 == 0:
        simbol = '🔵'
    else:
        simbol = '🟢'
    print(f'{simbol} {number}: {product}')