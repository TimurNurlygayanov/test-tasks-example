my_strings = ['aaaaaa', 'bbbbb', 'cccc']

result = {k: len(k) for k in my_strings}
print(result)


result = {}
for string in my_strings:
    result[string] = len(string)

print(result)
