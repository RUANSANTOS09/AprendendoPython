dishes = {
    'coxinha': 10,
    'pizza': 18,
    'lasagna': 34
}
order = str(input('Digite um prato: ')).strip().lower()
if order in dishes:
    dish_value = dishes[order]
    print(f'{order}: valor R${dish_value:.2f}')
else:
    print('Erro, produto não encontrado!!!!!!!')