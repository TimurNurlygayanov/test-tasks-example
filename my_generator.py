
def range2(start=0, stop=1, step=1):
    res = start
    while res < stop:
        yield res
        res += step


for x in range2(1, 10, 3):
    print(x)


print(len(range(1000)))
