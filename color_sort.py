'''Вам дан массив nums длины n, каждый элемент которого представляет собой «цвет»: 0 означает красный, 1 означает белый и 2 означает синий.
Вам необходимо отсортировать его на месте (т.е. не создавая нового массива) так,
чтобы все элементы одного цвета соседствовали друг с другом и шли по порядку «красные, белые, потом синие».
Запрещено использовать какую-либо встроенную функцию сортировки.
Напишите функцию color_sort(nums), которая будет принимать на вход список чисел и выдавать список чисел, отсортированных в нужном порядке.

Примеры:

nums = [2, 0, 1, 0, 2] даст [0, 0, 1, 2, 2]

nums = [2, 1, 0] даст [0, 1, 2]

nums = [2, 1, 1, 0, 0, 2, 2] даст [0, 0, 1, 1, 2, 2, 2]'''

'''Для решения этой задачи можно воспользоваться алгоритмом "Сортировка в один проход" (Dutch National Flag Algorithm), 
который был предложен Эдсгером Дейкстрой. Этот алгоритм позволяет отсортировать массив, 
содержащий три различных элемента, за один проход по массиву.
Идея алгоритма заключается в том, что мы используем три указателя: low, mid и high. 
Указатель low указывает на начало группы красных элементов, указатель mid указывает на начало группы белых элементов, 
а указатель high указывает на начало группы синих элементов.
Мы проходим по массиву и сравниваем текущий элемент с цветом. 
В зависимости от результата меняем элементы местами и сдвигаем указатели.'''

def color_sort(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

if __name__ == '__main__':

    print(color_sort([2, 0, 1, 0, 2]))
    print(color_sort([2, 1, 0]))
    print(color_sort([2, 1, 1, 0, 0, 2, 2]))