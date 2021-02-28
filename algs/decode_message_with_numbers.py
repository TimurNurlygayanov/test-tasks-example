# The task was taken from
# https://www.youtube.com/watch?v=qli-JCrSwuk
# I've spent several hours to solve it..
# and then just 10 minutes for the new solution
# after I watched the full video..


DECODE_TABLE = {str(i): chr(k) for i, k
                in enumerate(range(97, 123), start=1)}


def verify_str(msg: str) -> bool:
    for symbol in msg.split('+'):
        if symbol not in DECODE_TABLE:
            return False
    return True


def generate_options(msg: str) -> list:
    if len(msg) == 1:
        return [msg]
    if len(msg) == 2:
        return [msg, msg[0] + '+' + msg[1]]

    result = []

    options = generate_options(msg[1:])
    for o in options:
        num = o.split('+')
        if len(num[0]) == 1:
            k = '+'.join([msg[0] + num[0]] + num[1:])
            result.append(k)
        num = msg[0] + '+' + '+'.join(num)
        result.append(num)

    options = generate_options(msg[2:])
    for o in options:
        num = msg[:2] + '+' + o
        result.append(num)

    return result


def count_all_options(msg: str) -> int:
    result = generate_options(msg)
    result = [r for r in list(set(result)) if verify_str(r)]
    return len(result)


def helper(msg: str, k: int) -> int:
    if k == 0 or k == 1:
        return 1
    if msg[0] == '0':
        return 0

    s = len(msg) - k
    result = helper(msg, k-1)

    if int(msg[s:s+2]) < 27:
        result += helper(msg, k-2)

    return result


def count_number_of_options(msg: str) -> int:
    return helper(msg, len(msg))


examples = ['12', '123', '01', '123231', '99', '911']
for sample in examples:
    result = count_number_of_options(sample)
    print('{0} -> {1}'.format(sample, result))
