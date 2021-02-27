# Here is an examples of how generators work
#
#

import sys
from random import choice


# Compare memory required for the string and generator:
for s in ['Test me', 'test me harder'*1000]:
    a = (k for k in s)

    msg = 'Size of string with {0} characters:'
    print(msg.format(len(s)), sys.getsizeof(s))

    print('Size of iterator:', sys.getsizeof(a))
    print(' - ' * 20)


def get_characters(n: int) -> str:
    all_chars = [chr(s) for s in range(65, 90)]

    for i in range(n):
        res = yield choice(all_chars)
        if res == 'Test':
            exit(1)



for i in get_characters(10):
    print(i)

