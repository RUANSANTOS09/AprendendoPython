def create_product(name,price):
    return {'name': name, 'price':price}

def apply_discount(product,discount):
    product['price'] = product['price'] * (1 - discount / 100)
    return product


new_product = create_product(name = 'TV',price = 2995.99)
product_with_discount = apply_discount(new_product,15)
print(product_with_discount)
