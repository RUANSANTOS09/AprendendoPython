with open('product.txt', 'r', encoding='utf-8') as manipulator:
    r = manipulator.readlines()
    with open('product.enumerate', 'w', encoding='utf-8') as file:
       for index, value in enumerate(r, start = 1):
           file.write(f'{index}: {value.rstrip()}\n')
