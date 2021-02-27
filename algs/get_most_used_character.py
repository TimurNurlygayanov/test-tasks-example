# The task is: get the most used character in
# the string.


# The shortest implementation with python magic.
# Complexity: ~ O(N), memory: N
def get_top_char(my_str: str) -> str:
    return max((my_str.count(s), s) for s in my_str)[1]


# The solution #2 with saving the map of
# each character and the number of times we saw this
# character in the string
# Complexity: O(N), memory: N + M
# (where M is the number of characters in the alphabet)
def get_top_char(my_str: str) -> str:
    all_characters = {}

    # create map of character and the count of
    # this character in the string:
    for s in my_str:
        all_characters.setdefault(s, 0)
        all_characters[s] += 1

    return max(all_characters.items(), key=lambda x: x[1])[0]


examples = ['Test', 'osgmoidgvjfsmogijermgisfmsidlk',
            '1231231231231231231231231231231231']

for example in examples:
    res = get_top_char(example)
    print('{0:50} {1:5}'.format(example, res))
