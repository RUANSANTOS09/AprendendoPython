data_cities = {
    'São Paulo': 12,
    'Salvador': 34,
    'Curitiba': 8,
    'Gramado': 11
}
for city,temperature in data_cities.items():
   print(f'{city}: {temperature}')
   data_cities[city] = (temperature * 9/5) + 32
   print(f'{city} : {(temperature * 9 / 5) + 32}°F')
print(data_cities)