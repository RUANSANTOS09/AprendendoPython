numero_inicial = int(input('Digite um número: '))
numero_final = int(input('Digite um número final: '))
quantidade_par = 0
quantidade_impar = 0
for x in range(numero_inicial,numero_final + 1):
    if(x % 2 == 0):
        print(f'{x} - par')
        quantidade_par += 1
    else:
        print(f'{x} - ímpar')
        quantidade_impar += 1

print(f'Pares: {quantidade_par}\nÍmpares: {quantidade_impar}')