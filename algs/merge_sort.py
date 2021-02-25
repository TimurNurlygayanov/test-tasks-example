# The example was taken from this video:
# https://www.youtube.com/watch?v=KF2j-9iSf4Q


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    half_index = len(array) // 2
    array = merge_sort(array[:half_index]) + merge_sort(array[half_index:])

    i = 0
    j = half_index
    result = []

    while i < half_index or j < len(array):
        print(array, i, j)
        if i < half_index and (j == len(array) or array[i] <= array[j]):
            result.append(array[i])
            i += 1
        if j < len(array) and (i == half_index or array[j] <= array[i]):
            result.append(array[j])
            j += 1

    return result


examples = [[1, 2, 3], [1, 1, 1, 1],
            [4, 7, 1, 0], [5, 4, 3, 2, 1],
            [10101, -4, 222, 4, 2, 1, 7, 964, -1],
            [1], []]

for sample in examples:
    result = merge_sort(sample[:])
    print('{0} -> {1}'.format(sample, result))
