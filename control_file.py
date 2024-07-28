# Задача 1: Чтение строк из файла и определение самой длинной строки
# Прочитайте строки из файла strings.txt, найдите самую длинную строку и выведите её на экран.

import random as rnd


def write_rnd_numb(file_path='random_numbers.txt', count=20, start=1, stop=100):
    with open(file_path, 'w') as file:
        for _ in range(count):
            number = rnd.randint(start, stop)
            file.write(f'{number}\n')
        print('complete')


# write_rnd_numb()



# Задача 3: Запись и чтение списка чисел с добавлением
# Пользователь вводит 10 чисел. Сохраните эти числа в файл numbers.txt, каждое число на новой строке.
# Затем добавьте ещё 5 чисел в этот же файл без удаления предыдущих.

def read_write_file(file_path='numbers.txt', lst=[1,2,6,3,7,9,3,5,4,0]):
    with open(file_path, 'a') as file:
        for i in lst:
            file.write(f'{i}\n')


# digits_1 = [int(input('Input yours digits-')) for _ in range(3)]
# digits_2 = [int(input('Input yours digits-')) for _ in range(1)]
# read_write_file(lst=digits_1)
# read_write_file(lst=digits_2)

# ---------------------------
# Задача 4: Создание файла отчета с данными о количестве слов в строках
# Пользователь вводит 5 строк. Запишите эти строки в файл report.txt, добавив к каждой строке количество слов в ней.

def count_words_in_string(s):
    words = s.split()
    return len(words)

lines = []
for i in range(5):
    line = input(f'Введите строку {i+1}: ')
    word_count = count_words_in_string(line)
    lines.append(f"{line} - колличество слов: {word_count}")

with open('report.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
# ---------------------------
# Задача 5: Запись чисел с фильтрацией по диапазону
# Пользователь вводит 10 чисел. Запишите в файл filtered_numbers.txt только те числа, которые находятся в диапазоне от 10 до 50.

numbers = []
for i in range(10):
    number = int(input(f"Введите число {i+1}: "))
    numbers.append(number)

filtered_numbers = [num for num in numbers if 10 <= num <= 50]

with open("filtered_numbers.txt", "w") as file:
    for num in filtered_numbers:
        file.write(str(num) + "\n")

print("Числа успешн записаны в файл filtered_numbers.txt")
