a = [1, 2, 3, False]

print(any(a))
print(all(a))

print(vars())

# Access global variable:
a = 'Change me'
globals()['a'] = 'test'
print(a)

z = '  dfsdfd gerhgsge  '
z.strip('.')  # remove . from left and right
z.split('.')  # get the list of strings without .


print('%' * 20)
print()


class Printer(str):

    def __new__(cls, *args, **kwargs):
        def p(e):
            return args[0]

        return p

V = Printer

for _ in (V)(',,,')(V):
    print('Z')



print('%' * 20)
print()

s = 'test'
print(s)
s = 'test'
print(id(s))
s = 'test'
print(id(s[-1]))
