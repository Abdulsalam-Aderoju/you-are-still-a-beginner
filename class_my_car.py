import class_car
from class_car import Car, ElectricCar

my_new_car = Car("Audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar("Tesla", "Model S", 2019)
my_tesla.battery.describe_battery()

my_beetle = class_car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())