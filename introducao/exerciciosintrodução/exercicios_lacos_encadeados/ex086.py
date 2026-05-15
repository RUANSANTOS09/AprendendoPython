numeros_pulados = 0
for cont_ex in range(1,5):
    print(f'\nRodada {cont_ex}')
    for cont_in in range(1,11):
        if cont_in % 4 == 0:
            numeros_pulados += 1
            continue
        print(cont_in)
    print(f'Pulados: {numeros_pulados}')