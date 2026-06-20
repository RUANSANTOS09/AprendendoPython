try:
    manipulator = open('log_processamento','r', encoding='utf8')
except IOError:
    print('O arquivo não foi encontrado!!!')
else:
    for number, line in enumerate(manipulator, start=1):
        line = line.rstrip()
        print(f'{number}: {line}')
    manipulator.close()
