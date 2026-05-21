lista_numeros = [1,2,3,4,5]
while lista_numeros != []:
    numero_digitado = int(input('Digite um número para remové-lo da lista: '))
    if(numero_digitado in lista_numeros):
        lista_numeros.remove(numero_digitado)
        print(lista_numeros)
