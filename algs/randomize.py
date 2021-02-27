# He is the example of function which returns
# some pseudo random integers


def get_random(start=0, end=100, seed=2^6):
    i = (11^end) * (11 + start)  # just get some non zero number

    while True:
        # key elements here:
        # 1) start from start + "something"
        # 2) do % (end - start) to get numbers withing [start, end]
        number = start + ((i ^ 5) * start + seed) % (end - start)

        yield number
        i += 1


for i, value in enumerate(get_random(10, 100)):
    print(value)

    if i > 100:
        break

