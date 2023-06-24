def quickSort(array, low_index, high_index):
    if low_index < high_index:
        p = partition(array, low_index, high_index)
        quickSort(array, low_index, p - 1)
        quickSort(array, p + 1, high_index)


def partition(arr, lowIndex, highIndex):
    pivot = arr[highIndex]
    limiter = lowIndex - 1

    for index in range(lowIndex, highIndex):
        if arr[index] <= pivot:
            limiter = limiter + 1
            arr[index], arr[limiter] = arr[limiter], arr[index]

    arr[limiter + 1],arr[highIndex] = arr[highIndex],arr[limiter + 1]

    return limiter + 1


def is_anagram(first_string, second_string):
    if (len(first_string) == 0 and len(second_string) == 0):
        return (first_string, second_string, False)
    letras1 = list(first_string.lower())
    letras2 = list(second_string.lower())
    quickSort(letras1, 0, len(letras1) - 1)
    quickSort(letras2, 0, len(letras2) - 1)
    palavra1 = "".join(map(str, letras1))
    palavra2 = "".join(map(str, letras2))
    return (palavra1, palavra2, palavra1 == palavra2)
# código do quickSort disponível em: https://app.betrybe.com/
