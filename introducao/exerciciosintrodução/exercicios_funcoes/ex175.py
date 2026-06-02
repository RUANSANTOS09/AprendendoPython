def classify_sales(val):
    if(val <= 500):
        return 'Venda baixa'
    elif(val >= 500 and val <= 2000):
        return 'Média'
    else:
        return 'Venda alta'

sales_list = [500,1000,4000,5000,3000,2000]
for num in sales_list:
  print(f'{num} - {classify_sales(num)}')
print(f'Ao todo foram feitas {len(sales_list)} vendas, totalizando R${sum(sales_list):.2f}')