# Example was taken from
# https://www.youtube.com/watch?v=6Gv8vg0kcHc


def buble_sort(array: list) -> list:
    array_len = len(array)

    for i in range(array_len):
        for j in range(i+1, array_len):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array


examples = [[1, 2, 3], [4, 3, 2, 1],
            [1, 1], [],
            [-3, 22313, 1, 0, -4, 2, 6, 9]]

for sample in examples:
    result = buble_sort(sample[:])
    print('{0} -> {1}'.format(sample, result))
