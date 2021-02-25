# Write a function which checks if the string has
# any repeated characters


# One line implementation using the Python magic.
# Complexity: ~ O(N), memory: N
def check_repeats(my_str: str) -> bool:
    return any(s for s in my_str if my_str.count(s) > 1)


# Implementation #2 with
# "save all visited characters in list" approach.
# Complexity: O(N^2), memory: 2N
def check_repeats(my_str: str) -> bool:
    visited_chars = []
    for s in my_str:
        if s in visited_chars:
            return True
        visited_chars.append(s)

    return False


# implementation #3 with
# "get hash of each character" approach.
# Complexity: O(N), memory: N + M
# (where M is the number of characters in the alphabet)
def check_repeats(my_str: str) -> bool:
    visited_chars = [False for _ in range(256)]

    for s in my_str:
        char_index = ord(s)
        if visited_chars[char_index]:
            return True
        else:
            visited_chars[char_index] = True

    return False


examples = ['Test', 'test', 'DDGFSFSFSFEE',
            '123456789']

for example in examples:
    res = check_repeats(example)
    print('{0:20} {1:5}'.format(example, res))
