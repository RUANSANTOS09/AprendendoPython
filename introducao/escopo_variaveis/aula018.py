# Escopo Global e Local

var_global = 'Curso completo de Python'
def escreve_texto():
    global var_global
    var_global = 'Banco de Dados com SQL'
    var_local = 'Ruan'
    print(f'Varíavel Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função esxreve_texto()')
    escreve_texto()
    print('Tentar acessar as variáveis diretamente')
    print(f'Varíavel Global: {var_global}')
