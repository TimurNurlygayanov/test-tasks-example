# Task: get N number after "." of Eiler number "e"
# Note: e is very short value in math lib.

from math import e


def get(n):
    global e  # Eiler number

    e = str(e)

    if not n.isdigit() or int(n) + 1 >= len(e) or int(n) < 1:
        return 'ERROR'

    return e[int(n) + 1]


n = input('Please enter N: ')
print(get(n))
