# The example was taken from here:
# https://www.youtube.com/watch?v=5o-kdjv7FD0
# So we have let's say stair with 4 steps total
# and we can make 1, 2 or 3 steps in one jump,
# We need to find the number of total ways how we
# can jump from the start of the stair to the end


def num_ways(n: int, x: list) -> int:
    """ Recursive non optimal solution. """

    if x is []:
        return 0
    if n == 0:
        return 1

    result = 0
    for i, step in enumerate(x):
        path_length = n

        while path_length >= step:
            path_length = path_length - step
            result += num_ways(path_length, x[i+1:])

    return result


def num_ways2(n: int, x: list) -> int:
    """ Recursive optimal solution. """

    if n == 0:
        return 1

    result = 0
    for step in x:
        if n - step >= 0:
            result += num_ways2(n - step, x)

    return result


def num_ways3(n: int, x: list) -> int:
    """ Non recursive optimal solution. """

    if n == 0:
        return 1

    results = {0: 1}

    for i in range(1, n+1):
        total = 0

        for step in x:
            if i - step >= 0:
                total += results[i - step]

        results[i] = total

    return results[n]


examples = [{'n': 4, 'x': [1, 2]},
            {'n': 2, 'x': [1, 2]},
            {'n': 4, 'x': [1, 3, 5]}]

for sample in examples:
    result = num_ways3(sample['n'], sample['x'])
    print('{0} -> {1}'.format(sample, result))
