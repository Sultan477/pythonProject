# В этой задаче мы познакомимся с алгоритмом QuickSelect.
# Вам дан массив array и число k.
# Найдите в этом массиве k-ый наибольший элемент, не используя сортировки.
# Напишите функцию kth_largest(array, k),
# которая на вход будет принимать массив и число k и будет возвращать k-ый наибольший элемент.

def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return  i

def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    length = pivot_index - low + 1

    if length == k:
        return arr[pivot_index]
    elif k < length:
        return quick_select(arr, low, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, high, k - length)

def kth_largest(array, k):
    if k > 0 and k <= len(array):
        return quick_select(array, 0, len(array) - 1, k)
    else:
        return None


if __name__ == '__main__':
    array = [3, 2, 1, 5, 4]
    k = 2
    result = kth_largest(array, k)
    print(result)