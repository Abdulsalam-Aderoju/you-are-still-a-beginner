import car

my_car = car.build_car("toyota", "Jeep", color="Black")
print(my_car)

from car import build_profile
my_profile = build_profile("Aderoju", "Muhammad", role = "CEO")
print(my_profile)

#....OR....
from car import build_profile as bp
my_profile = bp("Aderoju", "Muhammad", role = "CEO")
print(my_profile)

#....to import all functions...
from car import *
