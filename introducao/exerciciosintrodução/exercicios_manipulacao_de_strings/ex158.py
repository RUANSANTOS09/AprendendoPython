senha = str(input('Digite uma senha: '))
valida = True
if not any(caractere.isdigit() for caractere in senha):
    print('Senha deve conter pelo menos um numero')
    valida = False
if (len(senha) <= 8 ):
    print('Senha deve ter pelo menos 8 caracteres')
    valida = False
if ' ' in senha:
    print('Senha não pode conter espaços')
    valida = False
if valida:
    print('Senha valida!')