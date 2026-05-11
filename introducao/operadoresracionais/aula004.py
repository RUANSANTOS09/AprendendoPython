numero  = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))
compara1 = numero == numero2 #Comparação
compara2 = numero != numero2 #Diferente
compara3 = numero < numero2 #Menor que
compara4 = numero > numero2 #Maior que
compara5 = numero <= numero2 #Menor ou igual
compara6 = numero >= numero2 #Maior ou igual
print('Os numeros {} e {} são iguais? {}'.format(numero, numero2, compara1))
print('Os numeros {} e {} são diferentes? {}'.format(numero, numero2, compara2))
print('O numero {} é menor que {}? {}'.format(numero, numero2, compara3))
print('O numero {} é maior que {}? {}'.format(numero, numero2, compara4))
print('O numero {} é menor ou igual a {}? {}'.format(numero, numero2, compara5))
print('O numero {} é maior ou igual a {}? {}'.format(numero, numero2, compara6))



