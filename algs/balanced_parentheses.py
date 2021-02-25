# Here is an example of implementation
# of a function which checks if the string of
# parentheses is balanced or not
# Based on https://www.youtube.com/watch?v=IhJGJG-9Dx8

# Balanced strings:
# {()()}
# {}()[][{(())}]
# Not Balanced strings:
# }{
# {([)}


def reverse(char: str) -> str:
    if char == '}':
        return '{'
    if char == ')':
        return '('
    return '['


def check_string(my_str: str) -> bool:
    stack = []

    for char in my_str:
        if char in '{[(':
            stack.append(char)
        else:
            previous_open = stack.pop()
            if reverse(char) != previous_open:
                return False

    if len(stack) > 0:
        return False

    return True


examples = ['{}{}{}()', '[[[[[]]]]]',
            '{}()[][{(())}]', '{([)}',
            '{{]]{{]]]]]]']

for example in examples:
    res = check_string(example)
    print('{0:20} {1}'.format(example, res))
