def find_duplicate(nums):
    if (len(nums) <= 0):
        return False

    numbers = nums
    numbers.sort()

    for number in range(len(numbers) - 1):
        if (type(numbers[number]) != int or numbers[number] < 0):
            return False

        if (numbers[number] == numbers[number + 1]):
            return numbers[number]
    return False
