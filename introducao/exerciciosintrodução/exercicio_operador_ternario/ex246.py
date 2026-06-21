status = input('Digite "sucesso" se o registro esteja completo ou "falha" caso tenha falhado: ')

result = 'Registro processado' if status == 'sucesso' else 'Registro rejeitado'
print(result)