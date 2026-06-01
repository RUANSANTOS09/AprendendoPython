numbers = 0
user_numbers_set = set()

while numbers <= 9:
    user_numbers = int(input('Digite um número: '))
    user_numbers_set.add(user_numbers)
    numbers += 1
print(f'Numeros digitados {len(user_numbers_set)}')
print(f'Números reptidos {numbers - len(user_numbers_set)}')