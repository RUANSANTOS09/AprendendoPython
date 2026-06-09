def division(k,j):
    return round(k/j,2)
if __name__ == '__main__':
  while True:
        try:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Foi digitado um caractere diferente de número. Tente novamente!!')

  try:
      result = division(num1,num2)
  except ZeroDivisionError:
      print(f'Não é possível dividir por zero!')
  else:
      print(f'A divisão entre {num1} e {num2} = {result}')
  finally:
      print('\nFim do cálculo')

