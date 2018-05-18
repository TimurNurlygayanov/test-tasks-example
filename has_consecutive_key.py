# -*- encoding=utf8 -*-

# Given an array of integers ('source'), find the number ('key') that appears specified times ('n')
# consecutively. Return true if such sequence of numbers is found and false otherwise. Use one
# loop.
# has_consecutive_key(source, key, n)
# has_consecutive_key([1, 2, 2], 2, 2) → True
# has_consecutive_key([1, 2, 2], 2, 3) → False
# has_consecutive_key([2, 1, 2], 2, 2) → False


def has_consecutive_key(source, key, n):
    return str([key]*n)[1:-1] in str(source)[1:-1]


print(has_consecutive_key([1, 2, 2], 2, 2))
print(has_consecutive_key([1, 2, 2], 2, 3))
print(has_consecutive_key([2, 1, 2], 2, 2))
print(has_consecutive_key([2, 1, 1, 2, 1], 1, 3))
print(has_consecutive_key([2, 1, 1, 1, 2, 1], 1, 3))