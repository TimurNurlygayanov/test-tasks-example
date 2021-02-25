# Here you can find the basic implementation
# of a Quick Sort on Python
# Note: builtin function "sorted" is using the quick
# sort algorithm as well.

from random import randint


def quick_sort(array: list) -> list:
    print('Array', array)
    if len(array) <= 1:
        return array

    start = 0
    end = len(array) - 1

    stone_position = randint(start, end)
    stone = array[stone_position]
    print('Stone', stone)

    while start <= end:
        while array[start] < stone:
            start += 1

        while array[end] > stone:
            end -= 1

        if start <= end:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp

            start += 1
            end -= 1

            print('Swap -> ', array)

    if stone_position:
        array = quick_sort(array[:stone_position + 1]) + \
                quick_sort(array[stone_position + 1:])

    return array




examples = [[1, 2, 3, 5, 6, 7],
            [23, 4, 5, 1, -5, 11101],
            [7, 6, 5, 4, 3, 2, 1, 1],
            [1, 1, 1, 1], [1, ], []]
# examples = [[7, 5, -1, 3]]

for example in examples:
    res = quick_sort(example[:])
    print('{0}  -> {1}'.format(example, res))
