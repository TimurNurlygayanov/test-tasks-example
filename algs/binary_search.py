# Here is the simple example of binary search algorithm
#

a = [1, 2, 3, 4, 5, 7, 20, 30, 45, 70, 70]


def bin_search(array, value):
    start = 0
    end = len(array)
    k = end // 2
    prev_k = -1

    while a[k] != value and k != prev_k:
        prev_k = k

        if a[k] < value:
            start = k
            k = start + (end - start) // 2
        else:
            end = k
            k = start + (end - start) // 2

    if k != prev_k:
        return k


print('Array:', a)

examples = [7, 10, 30, 70, 1]

for example in examples:
    res = bin_search(a, example)
    print('{0} \t->\t {1}'.format(example, res))
