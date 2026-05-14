numero = int(input('Digite um número: '))
quantidade_pulados = 0
quantidade_impressos = 0
for x in range(1, numero + 1):
    if x % 5 == 0:
        quantidade_pulados += 1
        continue
    quantidade_impressos += 1
    print(x)
print(f'Impressos: {quantidade_impressos}\nPulados: {quantidade_pulados}')
