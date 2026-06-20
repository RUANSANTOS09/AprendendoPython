import os
print(os.getcwd())
list_items = os.listdir()
for item in list_items:
    if os.path.isfile(item):
      print(f'{item} É um arquivo')
    elif os.path.isdir(item):
        print(f'{item} É uma pasta')
    else:
        print('Seu arquivo não é um arquivo e não é uma pasta')