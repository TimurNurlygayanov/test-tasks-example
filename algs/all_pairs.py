# The task is to generate "pairwise" all pairs
# combinations for the list of parameters


def get_permutations(array: list) -> list:
    if len(array) == 1:
        return array

    last_char = array[-1]
    results = set()
    previous_results = get_permutations(array[:-1])

    for r in previous_results:
        for i in range(len(r) + 1):
            results.add(r[:i] + last_char + r[i:])

    return list(results)


def get_all_unique_combinations(array, n_of_parameters_to_combine=2):
    if len(array) == 1:
        return array

    results = []
    combinations = set()
    permutations = get_permutations(array)

    for value in permutations:
        is_value_new = False

        for i in range(len(value) - n_of_parameters_to_combine + 1):
            new_combination = value[i:i + n_of_parameters_to_combine]

            if new_combination not in combinations:
                combinations.add(new_combination)
                is_value_new = True

        if is_value_new:
            results.append(value)

    return results


examples = [['a'], ['a', 'b'], ['a', 'b', 'c'], ['t', 'e', 's', 't']]
for example in examples:
    res = get_all_unique_combinations(example, 2)
    print('{0} {1:2} -> {2}'.format(example, len(res), res))
