# São imutávéis

tupla = (2,4,6,7,9)
print(tupla)

halogenios = ('F','Cl','Br','I','At')
gases_nobres = ('He','Ne','Ar', 'Xe','Kr','Rn')
elementos = halogenios + gases_nobres
t1 = (1,1,1,2,3,1,2,4,5,6,2)
print(t1.count(1))
print(halogenios[0:2])
print(elementos)
print('Cl' in halogenios)
print(sum(t1))

#Operações não disponiveis em tuplas: sort(), .append(), .reverse(), .pop()...
for elemento in elementos:
     print(f'Elemento químico: {elemento}')


grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)


grupo1 = ['Li','Na','K', 'Rb','Cs','Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))