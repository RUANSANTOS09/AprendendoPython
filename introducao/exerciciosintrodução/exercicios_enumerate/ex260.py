temperatures = [22, 35, 18, 40, 25, 38]
for number, temperature in enumerate(temperatures, start=1):
    if temperature > 30:
        print(f'Alerta na temperatura {number}: - {temperature}°C')