most_sold = 0
best_selling_product = ''
product = {
    'notebook': 20,
    'keyboard': 30,
    'motherboard': 40,
    'phone': 45
}
for name_product, quantity in product.items():
   print(f'{name_product}: {quantity}')
   if quantity > most_sold:
       most_sold = quantity
       best_selling_product = name_product
print(f'{best_selling_product} foi o produto mais vendido com {most_sold} vendas')