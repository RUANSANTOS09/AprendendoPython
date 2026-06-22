status = ['ok', 'erro', 'ok', 'erro', 'ok']
for index, value in enumerate(status, start=1):
    if value == 'erro':
      print(f'Falha na tarefa {index}')