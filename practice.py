'''Методы класса Person:

__init__(self, name, age, address, phones): конструктор класса, принимающий аргументы name, age, address и phones для
инициализации соответствующих атрибутов объекта.
get_name(self): метод для возврата имени человека в виде строки.
get_age(self): метод для возврата возраста человека в виде целого числа.
get_address(self): метод для возврата адреса человека в формате строки "street, city, zipcode".
get_phones(self): метод для возврата списка телефонов человека в формате списка строк "type: number".'''


# data = {
#     "name": "John",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "zipcode": "10001"
#     },
#     "phones": [
#         {"type": "home", "number": "212-555-1234"},
#         {"type": "work", "number": "646-555-5678"}
#     ]
# }
# [data, data_1, ...., data_n]


class DataBase:

    def __init__(self):
        self.data = []

    def add_person(self, name, age, street, city, zipcode, phone_type, number):
        self.data.append({'name': name,
                          'age': age,
                          'address': {
                              'street': street,
                              'city': city,
                              'zipcode': zipcode},
                          'phones': [
                              {'phone_type': phone_type, 'number': number}
                          ]})

    def get_name(self, user_number):  # 10.35784523145 - 12
        for person in self.data:  # person - data | len(self.data) < 10_000, inbound_dictionary < 4lev(17 rates) time
            if person['phones'][0]['number'] == user_number:
                return f'name - {person["name"]}'
        return f'person with phone number - {user_number} not found!'

    # stamp deviation time limit for completion

    def get_age(self, name):
        for person in self.data:
            if person['name'] == name:
                return f'name - {name}, age - {person["age"]}|\nuse - get_name to get\ninfo about phone number and name'

    def get_address(self, name):
        for person in self.data:
            if person['name'] == name:
                address = person['address']
                return f'Address: {address["street"]}, {address["city"]}, {address["zipcode"]}'
        return f'Person with name {name} not found.'

    def get_phones(self, name):
        for person in self.data:
            if person['name'] == name:
                phones = [f'{phone["phone_type"]}- {phone["number"]}' for phone in person['phones']]
                return phones
        return f'Person with name {name} not found.'

    def get_all_people(self):
        return self.data


import random
import string

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Julia']
ages = [30, 24, 19, 35, 28, 42, 33, 26, 31, 40, 66, 71, 38, 47, 55, 18, 47]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
          "Dallas", "San Jose",
          "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Seattle",
          "Denver", "Washington"]

streets = ["Main Street", "First Avenue", "Maple Avenue", "Elm Street", "Oak Street", "Park Avenue", "Pine Street",
           "Cedar Avenue", "Sunset Boulevard", "Broadway",
           "Washington Street", "Church Street", "Lakeview Drive", "River Road", "Spring Street", "Highland Avenue",
           "Forest Avenue", "Hillcrest Drive", "Willow Street", "Meadow Lane"]


def generate_person():
    user_name = random.choice(names)
    user_age = random.choice(ages)
    user_street = random.choice(streets)
    user_city = random.choice(cities)
    user_zipcode = ''.join(random.choices(string.digits, k=6))
    user_phone_type = random.choice(['Mobile', 'Home', 'Work'])
    user_number = '+1' + ''.join(random.choices(string.digits, k=10))

    return user_name, user_age, user_street, user_city, user_zipcode, user_phone_type, user_number


data_base = DataBase()

for _ in range(50):
    user_name, user_age, user_street, user_city, user_zipcode, phone_type, user_number = generate_person()
    data_base.add_person(user_name, user_age, user_street, user_city, user_zipcode, phone_type, user_number)

all_people = data_base.get_all_people()

print(data_base.get_name('+19369128889'))  # Поиск по номеру телефона
print(data_base.get_age('Alice'))  # Поиск по имени
print(data_base.get_address('Bob'))  # Поиск по имени
print(data_base.get_phones('David'))
for user in all_people:
    print(user)




