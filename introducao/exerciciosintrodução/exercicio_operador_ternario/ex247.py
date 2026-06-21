size_mb = int(input('Digite o tamanho do arquivo: '))
validation = 'Arquivo dentro do limite' if size_mb <= 50 else 'Arquivo excede o limite'
print(validation)