price_product = [10, 25, 8, 42, 15]
g = (round(price * 0.90,2) for price in price_product)

for price in g:
    print(f'R$ {price}')