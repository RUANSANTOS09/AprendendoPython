planetas = ('Mercúrio','Vênus','Terra','Marte')
for planeta in planetas:
    print(f'\n{planeta}')
    for cont_in in range(1,6):
        if cont_in > 1:
         print(f'{cont_in} Anos')
        else:
            print(f'{cont_in} Ano')