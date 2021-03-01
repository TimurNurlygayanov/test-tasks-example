# The task was taken from
# https://www.udemy.com/course/11-essential-coding-interview-questions/
# So we have two lists and we want to find all
# equal elements in these lists


# First solution, it took 20 minutes to solve it
def common_elements(array1: list, array2: list) -> list:
    i = 0
    j = 0
    result = []

    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            result.append(array1[i])
            i += 1
            j += 1
        elif i < len(array1) and array1[i] < array2[j]:
            i += 1
        elif j < len(array2):
            j += 1

    return result


# Second solution, it took 1 minute to solve it
# but only after I solved it with the first solution..
def common_elements(array1: list, array2: list) -> list:
    return list(set(array1) & set(array2))


examples = [{'a': [1, 2, 4, 6],
             'b': [3, 4, 6, 7]},
            {'a': [1, 6, 9],
             'b': [2, 7, 123]},
            {'a': [1, 2, 3],
             'b': [1, 2, 3]}]

for sample in examples:
    result = common_elements(sample['a'], sample['b'])
    print('{a} {b} -> {r}'.format(**sample, r=result))
