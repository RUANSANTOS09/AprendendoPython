files = ['dados.csv', 'log.txt', 'config.json', 'relatorio.csv', 'backup.txt']
extension = (s.split('.')[-1] for s in files)
print(next(extension))