time_execution = [45, 120, 300, 89, 600, 15]
g = (f'{time}s - Demorado? {time > 100}' for time in time_execution)
for i in g:
    print(f'{i}')