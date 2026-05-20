contador_maiorquedez = 0
for i in range(5):
    numeros = int(input('Digite um número: '))
    if(numeros > 10):
        contador_maiorquedez += 1
print(contador_maiorquedez)