tamanho = float(input('Uma distância em metros: '))
conversorCentimetro = tamanho * 100
conversorMilimetro = tamanho * 1000
conversorKM = tamanho / 1000
conversorHectometros = tamanho / 100
conversorDec = tamanho / 10
conversorDecimetros = tamanho * 10
print('A medida de {}m corresponde a\n{}cm\n{}mm\n{}KM\n{}HM'.format(tamanho,conversorCentimetro,conversorMilimetro,conversorKM,conversorHectometros))
print('{}DAM\n{}dm'.format(conversorDec,conversorDecimetros))