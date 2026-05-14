numero = int(input('Digite um número: '))
for x in range(1, numero + 1):
    if(x % 2 == 0 and x % 3 == 0 ):
        print(f'{x} - múltiplo de 2 e 3')
    elif( x % 2 == 0):
        print(f'{x} - múltiplo de 2')
    elif(x % 3 == 0):
        print(f'{x} - mútiplo de 3')
    else:
        print(x)