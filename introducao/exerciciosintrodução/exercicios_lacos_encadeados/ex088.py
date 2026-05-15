numero_pulados = 0
for cont_ex in range(1,4):
    print(f'\nRodada {cont_ex}')
    numero = int(input('Digite um número: '))
    for cont_in in range(1,11):
        calc = numero * cont_in
        if calc >= 50:
            numero_pulados += 1
            continue
        print(f'{numero} x {cont_in} = {calc}')
    print(f'Pulados: {numero_pulados}')
