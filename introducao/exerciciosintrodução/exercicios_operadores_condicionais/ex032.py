idade = int(input('Digite sua idade: '))
verifica_cadastro = str(input('Tem cadastro? Responda S para sim e N para não: '))
if(idade >= 18 and not verifica_cadastro == 'N' ):
    print('Acesso liberado!')
elif(idade < 18 and not verifica_cadastro == 'N'):
    print('Acesso negado, você tem {} anos e não é maior de idade.'.format(idade))
else:
    print('Acesso negado. Você precisa ter cadastro.')