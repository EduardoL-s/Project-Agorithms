def find_duplicate(nums):
    if (len(nums) <= 0):
        return False

    numbers = nums
    numbers.sort()

    duplicated = 0

    for number in range(len(numbers)):
        if (type(numbers[number]) != int or numbers[number] < 0):
            return False
        if (number == len(numbers) - 1):
            if (duplicated != 0):
                return duplicated
            return False
        if (numbers[number] == numbers[number + 1]):
            duplicated = numbers[number]
