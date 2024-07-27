# Сначала попробуем решить brut force методом

def brut_most_water(container):
    result = 0
    n = len(container)
    for i in range(n):
        for j in range(i+1, n):
            s_cand = min(container[i], container[j]) * (j - i)
            result = max(result, s_cand)
    return result # здесь задача решается за О(n^2) не очень хорошо

# Теперь попробуем решить с нормальной асимптотикой через жадный алгоритм

def speed_most_water(container):
    # length of height
    n = len(container)

    i, j = 0, n - 1

    result = 0

    while i < j:

        res = max(res, (j - i) * min(container[i], container[j]))


        if container[i] < container[j]:
            i += 1
        else:
            j -= 1
    return result

if __name__ == '__main__':

    # Пример массива высот стен
    heights = [5, 2, 3, 4, 6, 10, 7, 1, 9, 8]

    # Вызов функции brut_most_water
    print("Brut force result:", brut_most_water(heights))

    # Вызов функции speed_most_water
    print("Speed result:", speed_most_water(heights))
