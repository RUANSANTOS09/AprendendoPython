for cont_ex in range(1,11):
    print(f'\nTabuada do {cont_ex}')
    for cont_in in range(1,11):
        calc = cont_ex * cont_in
        if calc % 2 == 0:
          print(f'{cont_ex} x {cont_in} = {calc}')