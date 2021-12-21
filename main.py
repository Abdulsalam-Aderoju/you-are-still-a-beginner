guests = ["Aderoju", "Danny", "Samuel"]
guests.insert(0, "Tobi")
guests.append("Abdulsalam")
guests.pop(0)
print(len(guests))
print(guests)

players = ["Messi", "Rashford", "Ronaldo", "Martial"]
for player in players:
    print(player, "is a very good footballer")

cubes = [digit ** 3 for digit in range(0, 10)]
print(cubes)

color = "Green"
if color == "Red":
    print("Alien just earned 15 points")
elif color == "Green":
    print("Alien just earned 5 points")
else:
    print("Alien just earned 10 points")

users = ["Admin", "Abdulsalam", "Aderoju", "Muhammad"]
for user in users:
    if user == "Admin":
        print("Welcome", user, "would you like to see a status report?")
    else:
        print("Welcome", user, "Thank you for logging in again")

current_user = users = ["Admam", "Abdulsalam", "Aderoju", "Muhammad"]
new_user = ["Aderoju", "Danny", "Muqsit"]
all_user = new_user + current_user
print(sorted(all_user))
for user in new_user:
    if user in current_user:
        print(user, "had been used")
    else:
        print(user, "is available")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0["X_position"] = 0
alien_0["Y_position"] = 25
print(alien_0["color"])

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print()

for key, value in user_0.items():
    print("key:", key)
    print("value:", value)
    print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)
for name, language in favorite_languages.items():
    print(name, "loves to use", language)

for name in favorite_languages.keys():
    print(name.title())
if "Erin" not in favorite_languages:
    print("Erin please take our poll")
for name in sorted(favorite_languages.keys()):
    print(name.title(), "Thank you for taking the poll")

print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())

users = {
    "Muh_law": {
        "First name": "Muhammad",
        "Last name": "Lawwal",
        "Location": "Ajah"
    },
    "Abd_Roju": {
        "First name": "Abdulsalam",
        "Last name": "Aderoju",
        "Location": "Kaduna"
    }
}
print(users)

for name, user_info in users.items():
    print("Username:", name)
    full_name = user_info["Last name"] + " " + user_info["First name"]
    location = user_info["Location"]

    print("Full Name:", full_name)
    print("Location: ", location)
    print()

# name = input("Please enter your name: ")
# print("Hello", name)

# age = input("How old are you: ")
# print(age)
# age = int(age)
# age >= 18

# height = int(input("How tall are you, in inches: "))
# if height >= 48:
#    print("You are tall enough to ride")
# else:
#    print("sorry, you are younger that the required age to ride")

# number = int(input("Write a number and I will tell you if it is a multiple of 10 or not: "))
# if number % 10 == 0:
#    print("It is a multiple of 10")
# else:
#   print("It is not a multiple of 10")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "Tell me something, and I will repeat it back to you. "
prompts = "Enter 'Quit' to end the program: "
statement = prompt + prompts
# message = ""
# while message != "Quit":
#    message = (input(statement))
#    print(message)

# active = True
# while active:
#    message = input(statement)

#    if message == "Quit":
#        active = False
#    else:
#        print(message)

# SAME AS.......
# while True:
#    message = input(statement)
#    if message == "Quit":
#        break
#    else:
#        print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

# message = int(input("How old are you? "))
# if message < 3:
#    print("Your ticket is free")
# elif message <= 12:
#    print("Your ticket is $10")
# else:
#    print("Your ticket is $15")

# message = input("Write your age here Or enter 'Quit' to end you ticket application: ")
# while message == "Quit":
#    break
# else:
#    if message < 3:
#        print("Your ticket is free")
#    elif message <= 12:
#        print("Your ticket is $10")
#    else:
#        print("Your ticket is $15")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user.....: ", current_user.title())
    confirmed_users.append(current_user)
    print()

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while "cat" in pets:
    pets.remove("cat")
print(pets)

'''responses = {}
polling_active = True
while polling_active:
    name = input("What is your name?")
    response = input("Which Mountain would you love to climb someday?")
    responses[name]  = response

    repeat = input("Would you like to let another person take the poll (Yes/No)?")
    if repeat == "No":
        polling_active = False
print()
print(".......Poll Results........")
for name, response in responses.items():
    print(name.title(), "will like to climb mountain", response, "someday")'''


# ......FUNCTION.......
def greet_user(username):
    print("Hello,", username.title())


greet_user("Katikati")


def favourite_book(title):
    print("One of my favourite books is", title.title())


favourite_book("The rise of Katikati")


def describe_animal(animal_type, pet_name="Katikati"):
    print("I have a", animal_type)
    print("Its name is", pet_name)


describe_animal("Dog")
# ........OR........
describe_animal(animal_type="Dog", pet_name="Kosere")


def describe_city(state, capital="Ikeja"):
    print(capital, "is in", state)


describe_city("Lagos")
describe_city("Nassarawa", "Lafia")
describe_city("Niger", "Minna")


def get_formatted_name(last_name, first_name):
    full_name = last_name + " " + first_name
    return full_name


musician = get_formatted_name("Aderoju", "Abdussalaam")
print(musician)


def arranged_name(last_name, first_name, other_name=""):
    full_name = last_name + " " + first_name + " " + other_name
    return full_name


him = arranged_name("Aderoju", "Abdussalaam", "Olanrewaju")
print(him)
her = arranged_name("Aderoju", "Mutmainnah")
print(her)


def build_person(first_name, last_name):
    person = {"First": first_name, "Last": last_name}
    return person


CEO = build_person("Elon", "Musk")
print(CEO)


# .....FOR OPTIONAL VALUES SUCH AS AGE HERE.....
def builed_person(first_name, last_name, age=None):
    person = {"First": first_name, "Last": last_name}
    person["age"] = age
    return person


COE_baba = builed_person("Elon", "Musk", 56)
print(COE_baba)


def greeting(usernames):
    for username in usernames:
        print("Hello,", username.title())


names = ["Lasis", "Kamoru", "Adebisis"]
greeting(names)

print()


def congratulate(players):
    for player in players:
        print(player, "..you played fantabulously well today")


man_utd_players = ["Rashford", "Sancho", "Greenwood", "Van De Beek"]
congratulate(man_utd_players)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing:", current_design)
        completed_models.append(current_design)


print()


def listing_designs(completed_models):
    print("The following models have been printed: ")
    for model in completed_models:
        print(model)


new_desings = ['tesla case', 'motor pendant', 'alpha jet']
new_models = []

print_model(new_desings, new_models)
listing_designs(new_models)

print()
foods = ["Rice", "Beans", "Weina", "Yam", "Potatoes"]
meals = []


def serve(foods, meals):
    while foods:
        serving = foods.pop()
        print("Serving", serving)
        meals.append(serving)
    print()


def listing(meals):
    print("The following have beeen served: ")
    for meal in meals:
        print(meal)


gadgets = ["Laptop", "phone", "airpods", "keyboard", "smart watch"]
confirmed = []

serve(gadgets, confirmed)
listing(confirmed)


def show_messages(short_messages):
    for short_message in short_messages:
        print(short_message)


print()


def send_messages(short_messages, sent_messages):
    while short_messages:
        message = short_messages.pop()
        print("Sending", message)
        sent_messages.append(message)


short_messages = ["How far", "wasssup", "booni", "how school"]
sent_messages = []

show_messages(short_messages)
send_messages(short_messages[:-1], sent_messages[:])


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile("Aderoju", "Abdussalaam", location="Abati", school="AFIT")
print(user_profile)


def build_car(name, type, **car_specs):
    car_specs["name"] = name
    car_specs["type"] = type
    return car_specs


car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name, "is now sitting")

    def rollover(self):
        print(self.name, "just rolled over!")


my_dog = Dog("Willie", 6)
print("My dog's name is", my_dog.name)
print(my_dog.name, "is", my_dog.age, "years old")
my_dog.sit()
my_dog.rollover()

print()

your_dog = Dog("Lucy", 3)
print("Your dog's name is", your_dog.name)
print(your_dog.name, "is", your_dog.age, "years old")
your_dog.sit()
your_dog.rollover()

print()


class Restaurant:
    def __init__(self, name, cruise_type, location):
        self.name = name
        self.cruise_type = cruise_type
        self.location = location
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name, "is located at", self.location, "in the midst of the biggest hotels in that area")

    def open_restaurant(self):
        print(self.name, "is now open for all different kinds of service it offers")

    def set_number_served(self, set):
        self.number_served = set
        print("we have served", self.number_served, "people today")

    def increment_number_served(self, increase):
        self.number_served += increase
        print("We have have served", self.number_served, "people today")


restaurant = Restaurant("The Aderojus", "Big", "Ajah")
print("The name of this restaurant is", restaurant.name, "with a", restaurant.cruise_type, "cruise type")
print(restaurant.name, "is located in", restaurant.location)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("We have served", restaurant.number_served, "today.")
restaurant.number_served = 60
print("We have served", restaurant.number_served, "today.")
restaurant.set_number_served(200)
restaurant.increment_number_served(30)
print()

restaurant_2 = Restaurant("Twin Faja", "Medium", "Alimosho")
restaurant_2.describe_restaurant()
print()

restaurant_3 = Restaurant("The Shittus", "Small", "Satellite")
restaurant_3.describe_restaurant()
print()

class IceCreamStand(Restaurant):
    def __init__(self, name, cruise_type, location, flavours):
        super().__init__(name, cruise_type, location)
        self.flavours = flavours

    def available_flavours(self):
        print("The following flavours are available: ")
        for flavor in self.flavours:
            print(flavor)

flavours_available = ["Vanilla", "Caramell", "Milky", "Chocolates"]
new_restaurant = IceCreamStand("Callius", "Enlarged", "Ejigbo", flavours_available)
new_restaurant.describe_restaurant()
new_restaurant.available_flavours()

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


my_new_car = Car("Audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# ...TO UPDATE OR MODIFY VALUES...
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(45)
my_new_car.increment_odometer(2000)
my_new_car.read_odometer()

my_new_car.fill_gas_tank(31)

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


my_tesla = ElectricCar("Tesla", "Model S", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank(90)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()




















































