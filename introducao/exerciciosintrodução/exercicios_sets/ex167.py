fruits = ['Banana','Banana','Morango','Melancia','Melancia','Abacaxi']
fruits_set = set(fruits)
fruits_set.add('Maçã')
fruits_set.discard('Abacaxi')
print(fruits_set)