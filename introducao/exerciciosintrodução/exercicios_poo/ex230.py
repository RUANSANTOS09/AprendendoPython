class Sensor:
    def __init__(self):
        self.__temperatures = []


    def set_temperatures(self, temperatures):
        self.__temperatures.append(temperatures)

    def get_average_temperatures(self):
        return sum(self.__temperatures) / len(self.__temperatures)

    def get_status(self):
        if self.get_average_temperatures() > 30:
            print('Alerta: temperatura alta!!')
        elif self.get_average_temperatures() < 0 :
            print('Alerta: temperatura baixa!!!')
        else:
            print('Temperatura normal')

my_temperatures = Sensor()
my_temperatures.set_temperatures(30)
my_temperatures.set_temperatures(30)
my_temperatures.set_temperatures(40)
my_temperatures.set_temperatures(20)
my_temperatures.set_temperatures(10)
print(my_temperatures.get_average_temperatures())
my_temperatures.get_status()
