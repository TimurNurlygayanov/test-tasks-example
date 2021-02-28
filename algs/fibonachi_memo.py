# Here is the example
# https://www.youtube.com/watch?v=P8Xa2BitN3I
# Note: with memo it works significantly faster


def fib(n: int, memo=None) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    if not memo:
        memo = [None] * (n+1)
    if memo[n]:
        return memo[n]

    result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result

    return result


res = fib(120)
print(res)
