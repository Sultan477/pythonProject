def merge(a: list, b: list) -> list:
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result

if __name__ == '__main__':

    a1 = [1, 3, 5, 8]
    b1 = [2, 6, 7, 13]
    print(merge(a1, b1))  # [1, 2, 3, 5, 6, 7, 8, 13]

    a2 = [-5, 0, 4, 9]
    b2 = [1, 1]
    print(merge(a2, b2))  # [-5, 0, 1, 1, 4, 9]

    a3 = []
    b3 = []
    print(merge(a3, b3))  # []

    a4 = []
    b4 = [1, 2, 3]
    print(merge(a4, b4))  # [1, 2, 3]