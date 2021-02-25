# The task was taken from
# https://www.youtube.com/watch?v=GBuHSRDGZBY
#


def find_best_matches(array_a: list, array_b: list, num: int) -> list:
    results = []

    array_a = sorted(array_a)
    array_b = sorted(array_b)

    x = len(array_a) - 1
    y = 0

    while x >= 0 and y < len(array_b):
        num_check = array_a[x] + array_b[y]

        results.append((abs(num - num_check), x, y))

        if num_check <= num:
            y += 1
        else:
            x -= 1

    # sort to show the optimal solution first
    results = sorted(results, key=lambda x: x[0])
    # choose only the best combinations
    results = [(array_a[x[1]], array_b[x[2]])
               for x in results if x[0] == results[0][0]]

    return results


examples = [{'a': [2, 4, 6], 'b': [3, 7, 15], 'n': 5},
            {'a': [2], 'b': [3], 'n': 7},
            {'a': [2, 17, 23, 56], 'b': [3, 4, 7, 14, 18, 22], 'n': 65}]

for sample in examples:
    result = find_best_matches(sample['a'], sample['b'], sample['n'])
    print('{n} {a} {b} -> {result}'.format(result=result, **sample))
