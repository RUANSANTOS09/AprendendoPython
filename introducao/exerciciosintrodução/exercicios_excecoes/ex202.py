try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print(f'O número tem que ser inteiro!!!!!!!')
else:
    print(num)
finally:
    print('Fim')