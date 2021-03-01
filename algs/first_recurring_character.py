# The task was taken from
# https://www.youtube.com/watch?v=GJdiM-muYqc
#


def get_first_recurring_char(msg: str) -> str:
    hash_map = set()

    for s in msg:
        if s in hash_map:
            return s
        hash_map.add(s)


samples = ['ABCDA', 'AABBBFFFF',
           'ACB', 'ABFSDFSDFSDFAB',
           'BCABA']
for sample in samples:
    result = get_first_recurring_char(sample)
    print('{0} -> {1}'.format(sample, result))
