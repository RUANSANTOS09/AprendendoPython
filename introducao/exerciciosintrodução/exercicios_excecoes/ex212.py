class ValueVeryHighError(Exception):
    def __init__(self):
        pass
if __name__ == '__main__':
    while True:
        try:
            num = int(input('Digite um número menor que 100: '))

            if num > 100:
                raise ValueVeryHighError
            break
        except ValueVeryHighError:
            print('O valor tem que ser menor que 100. Tente novamente!!')
