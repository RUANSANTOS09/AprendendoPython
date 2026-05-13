contador = 1
soma = 0
while(contador <= 4):
    nota = float(input('Digite a nota do aluno: '))
    contador += 1
    soma += nota

resultado = soma / 4
print(f'A média das notas é igual a {resultado} ')