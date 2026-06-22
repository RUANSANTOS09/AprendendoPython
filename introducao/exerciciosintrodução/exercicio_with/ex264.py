product =  ['notebook\n', 'mouse\n', 'teclado\n', 'monitor']
with open('product.txt', 'w', encoding='utf-8') as manipulator:
    manipulator.writelines(product)