verificador_usuario = str(input('Digite um nome de usuário'))
verificador_senha = int(input('Digite a senha do usuario: '))
verificador = (verificador_usuario == 'admin') and (verificador_senha == 1234)
print('A senha e usuario estão corretas? {}'.format(verificador))
