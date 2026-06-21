status = ['ok', 'erro', 'ok', 'ok', 'erro', 'ok']
index_error = (i for i,s in enumerate(status) if s == 'erro')
for i in index_error:
    print(f'{i}')
