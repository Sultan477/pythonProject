print('hello world')
# # Условный оператор
# if 5 > 4:
#     print('Yes')
#
# elif 5 == 5:
#     print('Equal')
#
# else:
#     print(None)
#
# # Сложные условия
# if n > 5 and n < 10:
#     print(n)
# elif n == 2 or n >= 0:
#     print(n)
#
# else:
#     print(n)
#
# # Типы данных
# # change None to any value
#
# a = 'Freedom'
#
# print(type(a))
#
# # Операции над строками и числами
# a = None
# b = None
# print(b + a)
#
# # Приоритет операций
# print((9 + 1) * 3)
#
# # Цикл с предусловием
# while n >= 0:
#     print(5)
#
# # Отладка программ
# # print inside programm to check current value of variable
#
# # Цикл For
# n = [1, 4, 2, 5, 6]
# for i in range(len(n)):
#     print(n[i])
#
# # Вложенные циклы
# if wrestllers <= 4:
#     print('Semifinal')
#     if wrestllers <= 2:
#         print('final')
#
# def two_sum(a: int, b: int) -> int:
#     '''Pass'''
#     return a + b
#
# print(two_sum(a=4, b=5))


import math

# print(math.pi)
# print(math.e)


# Основные математические функции:
#
# math.sqrt(x): Возвращает квадратный корень из x.
# math.pow(x, y): Возвращает x в степени y.
# math.factorial(x): Возвращает факториал числа x.
# math.gcd(x, y): Возвращает наибольший общий делитель чисел x и y.
# math.ceil(x): Округляет x до ближайшего большего целого числа.
# math.floor(x): Округляет x до ближайшего меньшего целого числа.

# print("Синус 90 градусов:", math.sin(math.radians(90)))
# print("Косинус 0 градусов:", math.cos(math.radians(0)))
# print("Тангенс 45 градусов:", math.tan(math.radians(45)))
#
#
# print(math.ceil(10.001))

import random

# random.random(): Возвращает случайное число с плавающей запятой в диапазоне от 0.0 до 1.0.
# random.uniform(a, b): Возвращает случайное число с плавающей запятой в диапазоне от a до b.
# random.randint(a, b): Возвращает случайное целое число в диапазоне от a до b (включительно).
# random.randrange(start, stop, step): Возвращает случайное число из диапазона от start до stop с шагом step.
# Выбор случайного элемента:
#
# random.choice(seq): Возвращает случайный элемент из последовательности seq.
# random.choices(population, weights=None, *, cum_weights=None, k=1): Возвращает список длины k из элементов population с возможностью задания весов.
# random.sample(population, k): Возвращает список из k уникальных элементов из population.
# Перемешивание последовательности:
#
# random.shuffle(seq): Перемешивает последовательность seq на месте.
# Генерация случайных байтов:
#
# random.getrandbits(k): Возвращает случайное целое число с k битами.
# population = list(range(20))
#
# random.choices(population, weights=None, *, cum_weights=None, k=1)

# a = ['red', 'blue', 'orange', 'red', 'blue', 'blue']


# print(random.getrandbits(11))
# print(int(10))

import datetime

# datetime.date: Для работы с датами (год, месяц, день).
# datetime.time: Для работы с временем (часы, минуты, секунды, микросекунды).
# datetime.datetime: Для работы с датой и временем вместе.
# datetime.timedelta: Для представления разницы между двумя датами или временем.
# Создание объектов:
#
# datetime.date(year, month, day): Создает объект даты.
# datetime.time(hour=0, minute=0, second=0, microsecond=0): Создает объект времени.
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Создает объект даты и времени.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Создает объект разницы во времени.
# Текущая дата и время:
#
# datetime.datetime.now(): Возвращает текущие дату и время.
# datetime.datetime.today(): Возвращает текущие дату и время.
# datetime.date.today(): Возвращает текущую дату.
# Форматирование и парсинг:
#
# datetime.datetime.strftime(format): Форматирует объект datetime в строку.
# datetime.datetime.strptime(date_string, format): Преобразует строку в объект datetime согласно заданному формату.
# Атрибуты объектов:
#
# date.year, date.month, date.day: Возвращают соответствующие части даты.
# time.hour, time.minute, time.second, time.microsecond: Возвращают соответствующие части времени.


# print(datetime.date.today())


# Напишите функцию, которая симулирует бросок кубика (возвращает случайное число от 1 до 6).

import random

# def cube_toss(n=1):
#     result = []
#     for _ in range(n):
#         a = random.randint(1, 6)
#         result.append(a)
#     return result
#
#
# print(cube_toss(10))

# Напишите программу, которая выбирает 6 случайных уникальных чисел из диапазона от 1 до 49 (аналог лотереи).

# def bingo():
#     lst = list(range(1, 50))
#     smp = random.sample(lst, k=6)
#     return smp
#
#
# print(bingo())

# Напишите функцию, которая принимает список имен и возвращает случайно выбранное имя. Затем модифицируйте функцию, чтобы можно было задавать вес для каждого имени.

# names = ["Alice", "Bob", "Charlie"]
# indx = [random.randint(0, 9) for _ in range(3)]
# # Вес каждого элемента списка передается в отдельном списке целочисленных значений, как аргумент функции
# def choice_name(n):
#     rnd_idnx = random.randint(0, len(n) - 1)
#     return n[rnd_idnx]
#
#
# # print(choice_name(names))
#
# print(indx)
# def rnd_choices(n, ind):
#     return random.choices(n, weights=ind, k=10)
#
# print(rnd_choices(names, indx))

# Напишите функцию, которая генерирует случайный пароль заданной длины.
# Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву, одну цифру и один специальный символ.
# Напишите программу, которая загадывает случайное число от 1 до 100, и предлагает пользователю угадать его. Программа должна давать подсказки ("меньше" или "больше") до тех пор, пока пользователь не угадает число.


# Задача генерации пароля
import random
import string


# def generate_password(lenght):
#     uppercase_letters = string.ascii_uppercase
#     lowercase_letters = string.ascii_lowercase
#     digits = string.digits
#     special_chars = string.punctuation
#
#     password = [random.choice(uppercase_letters),
#                 random.choice(lowercase_letters),
#                 random.choice(digits),
#                 random.choice(special_chars)]
#
#     password.extend(random.choices(string.ascii_letters + string.digits + string.punctuation, k=lenght - 4))
#
#     random.shuffle(password)
#     return ''.join(password)
#
# password = generate_password(10)
# print(password)


# Задача про угадывание числа

def guess_number():
    secret_number = random.randint(1, 100)

    print('Загадано число от 1 до 100. Попробуйте отгадать!')

    while True:
        guess = int(input('Введите ваше предположение: '))

        if guess < secret_number:
            print('Загаданное число больше!')
        elif guess > secret_number:
            print('Загадонное число меньше!')
        else:
            print('Поздравляю вы угадали число!')
            break


guess_number()

print('hello world')
