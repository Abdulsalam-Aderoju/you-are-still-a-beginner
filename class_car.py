class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_level = 0

    def get_descriptive_name(self):
        full_name = (self.year, self.manufacturer, self.model)
        return full_name

    def read_odometer(self):
        print("This car has", self.odometer_reading, "miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gas):
        self.gas_level = + gas
        print("The gas level in the tank is now", self.gas_level)



class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car uses a battery of", self.battery_size, "KWh")
    def get_range(self):
        if self.battery_size == 75:
            range = 230
        elif self.battery_size == 100:
            range = 300
        print("This car can go about", range, "on a full charge")
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
#       USING THE CLASS 'Battery' AS AN ATTRIBUTE IN THIS CLASS
        self.battery = Battery()
    def fill_gas_tank(self, gas):
        print("This car doesn't need a gas tank")
