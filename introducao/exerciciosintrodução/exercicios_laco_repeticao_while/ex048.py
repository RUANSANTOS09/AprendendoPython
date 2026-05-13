contador_dias = 1
soma_total = 0
while(contador_dias <= 7):
    gasto = float(input(f'Digite o total gasto do dia {contador_dias} R$ '))
    contador_dias += 1
    soma_total += gasto

media_total = soma_total / 7
print(f'O gasto total da semana é igual a R${soma_total:.2f}\nO gasto médio por dia é igual a R${media_total:.2f}')