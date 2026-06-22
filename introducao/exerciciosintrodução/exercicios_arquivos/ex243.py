question = input('Digite uma palavra e encontre-a no arquivo: ')
try:
    manipulator = open('../exercicio_with/log_processamento', 'r', encoding='utf-8')
    for line in manipulator:
        line = line.rstrip()
        if question in line:
            print(f'Linha encontrada')
            print(line)
except IOError:
    print('Arquivo não encontrado')
else:
    manipulator.close()
