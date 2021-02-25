# The task is to get the string and generate all permutations
# possible for this string.


import itertools


# Easy way by using the itertools
def get_permutations(my_str: str) -> list:
    return list(''.join(x) for x in itertools.permutations(my_str))


def get_permutations(my_str: str) -> list:
    if len(my_str) == 1:
        return [my_str]

    last_char = my_str[-1]
    results = set()
    previous_results = get_permutations(my_str[:-1])

    for r in previous_results:
        for i in range(len(r) + 1):
            results.add(r[:i] + last_char + r[i:])

    return list(results)


examples = ['a', 'ab', 'abc', 'test']
for example in examples:
    res = get_permutations(example)
    print('{0:10} {1} -> {2}'.format(example, len(res), res))
