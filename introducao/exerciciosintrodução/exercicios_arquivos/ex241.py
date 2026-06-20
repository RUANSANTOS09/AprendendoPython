text = ['Iniciando processamento\n', '150 registros\n', 'Processamento concluído']
try:
    manipulator = open('log_processamento', 'w', encoding='utf-8')
except IOError:
    print('O arquivo não foi encontrado!!!')
else:
    manipulator.writelines(text)
    manipulator.close()
