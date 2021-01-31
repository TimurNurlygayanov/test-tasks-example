# Append list to itself
a = [1, 2, 3, 4]
a.append(a)
a.append('3')
print(a, a[4])

# Create list from the list of lists
my_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
res = sum(my_list, [])
print(res)

# With list generator
res = [y for x in my_list for y in x]
print(res)

# With Reduce
from functools import reduce
from operator import add

res = reduce(add, my_list)
print(res)

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])

print(a | b)  # combine sets (OR)
print(a & b)  # find common elements (AND)
print(a ^ b)  # find unique elements in both sets (XOR)

# Create class inline
NewType = type('NewType', (object,), {'x': 'hello'})
c = NewType()
print(c)
print(c.x)

# Unpacking
first, second, *rest = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(rest)

# How Try/Except works
try:
    print()
except Exception as e:
    print('Here is our exception:', e)
else:
    print('Try passed, except was not called')
finally:
    print('do this anyway at the end')

print(' - ' * 20)

# How it works when in it has several levels
try:
    try:
        DD
    except FileExistsError as e:
        print('Inner exception handler', e)
    finally:
        print('Inner finally')
except Exception as e:
    print('Here is our exception:', e)
else:
    print('Try passed, except was not called')
finally:
    print('do this anyway at the end')

print(' - ' * 20)

# Crazy lists
a = [1, 2]
b = a
b.append(3)
print(a)

c = a[:]  # the right way to copy dicts
c.append('4')
print(a)

print(' - ' * 20)

# Do not init value with list like this
def foo(x=[]):
    x.append('AAA')
    print(x)

foo()
foo()

print(' - ' * 20)

def jim(phrase):
    return 'Jim says: "%s".' % phrase

def say_something(person, phrase):
    print(person(phrase))

say_something(jim, 'hey guys')

# Round can be with negative numbers:
print(round(1234.5678, -2))

import this

print(' - ' * 20)

a = [(1, 2), (3, 4), (5, 6)]
res = zip(*a)
print(list(res))

a = [1, 2, 4, 5, 6, 7]
b = [7, 8, 9]
res = dict(zip(a, b))
print(res)
res = list(zip(a, b))
print(res)

print(a)
print(*a)  # hmm....

a[::2] = a[::-2]  # Create a mirror effect
print(a)


from collections import Counter
s = 'habrahabr'
res = Counter(s)
print(res)
# The same:
res = {k: s.count(k) for k in s}
print(res)

# Map
numbers = [1, 2, 3, 4, 5]
res = map(lambda x: x * x, numbers)
res2 = (x*x for x in numbers)   # create generator
print(list(res), list(res2))

# Filter
res = filter(lambda x: x < 4, numbers)
res2 = (x for x in numbers if x < 4)  # create generator
print(list(res), list(res2))

