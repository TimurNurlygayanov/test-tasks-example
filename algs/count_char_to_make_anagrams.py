# This task was taken from
# https://www.youtube.com/watch?v=3MwRGPPB4tw
#


def compare(string1: str, string2: str) -> int:
    chars1 = {k: string1.count(k) for k in string1}
    chars2 = {k: string2.count(k) for k in string2}

    result = 0

    for char, count in chars1.items():
        result += abs(count - chars2.get(char, 0))

    for char, count in chars2.items():
        if char not in chars1:
            result += count

    return result


examples = [('hello', 'billion'),
            ('test me', 'not test me')]

for sample in examples:
    result = compare(*sample)
    print('{0} -> {1}'.format(sample, result))
