# The example of task was taken from
# https://www.youtube.com/watch?v=4UWDyJq8jZg


def get_year_on_max_population(data: list) -> int:
    """ Naive solution with M*logM + M*N + N complexity. """
    first_birth = min(data, key=lambda x: x['birth'])
    last_death = max(data, key=lambda x: x['death'])

    results = {0: 0}
    max_year = 0

    for i in range(first_birth['birth'], last_death['death'] + 1):
        results[i] = 0

        for person in data:
            if person['birth'] <= i <= person['death']:
                results[i] += 1

        if results[i] > results[max_year]:
            max_year = i

    return max_year


def get_year_on_max_population(data: list):
    """ With naive hashmap. Complexity M1*N,
        where M1 is the medium life length.
    """

    hashmap = {}
    for person in example:
        for i in range(person['birth'], person['death'] + 1):
            hashmap.setdefault(i, 0)
            hashmap[i] += 1

    if hashmap:
        return max(hashmap.items(), key=lambda x: x[1])

    return None


def get_year_on_max_population(data: list):
    """ Optimized solution with hashmap. """

    hashmap = {}
    for person in example:
        hashmap.setdefault(person['birth'], 0)
        hashmap.setdefault(person['death'] + 1, 0)

        hashmap[person['birth']] += 1
        hashmap[person['death'] + 1] -= 1  # we count -1 only after

    result = 0
    result_max = 0
    result_max_year = None

    # Get sorted list of years with births and deaths
    hashmap_keys_sorted = sorted(hashmap)

    for year in hashmap_keys_sorted:
        result += hashmap[year]

        if result > result_max:
            result_max = result
            result_max_year = year

    return result_max_year


example = [{'birth': 1750, 'death': 1860},
           {'birth': 1820, 'death': 1901},
           {'birth': 1890, 'death': 1945},
           {'birth': 1771, 'death': 1945}]
# example = [{'birth': 1750, 'death': 1740}]

result = get_year_on_max_population(example)
print('Result: {0}'.format(result))
