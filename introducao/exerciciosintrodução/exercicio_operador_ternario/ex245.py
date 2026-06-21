age1 = int(input('Qual a sua idade? '))
age2 = int(input('Qual a sua idade? '))

older = age1 if age1 > age2 else age2
print(f' O mais velho possui: {older} anos')