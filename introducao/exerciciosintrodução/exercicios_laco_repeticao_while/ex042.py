par = 0
impar = 0
while True:
    num = int(input('Digite números, ao final você descubrirá quantos foram par e quantos foram impares, digite 0 para sair: '))
    if(num == 0):
        break
    elif(num % 2 == 0):
        par += 1
    else:
        impar += 1

print(f'Total de números pares: {par}\nTotal de númros impares: {impar}')