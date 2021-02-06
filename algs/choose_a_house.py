# The task was taken from
# https://www.youtube.com/watch?v=rw4s4M3hFfs
#

blocks = [
    {
        'school': True,
        'shop': True,
        'gym': False
    },
    {
        'school': True,
        'shop': False,
        'gym': False
    },
    {
        'school': False,
        'shop': False,
        'gym': False
    },
    {
        'school': True,
        'shop': False,
        'gym': False
    },
    {
        'school': False,
        'shop': False,
        'gym': True
    }
]

desired_places = ['school', 'shop', 'gym']

#
# The solution is to do one iteration over the list,
# but on each iteration check 2 elements:
# 0 and N
# 1 and N-1
# ...
# N-1 and 1
# N and 0


start = 0
end = len(blocks) - 1

results = [{k: end for k in desired_places}
           for i in range(end + 1)]

while start != end:
    for r in desired_places:
        if blocks[start][r]:
            results[start][r] = 0
        elif start > 0 and results[start - 1][r] < results[start][r]:
            results[start][r] = results[start - 1][r] + 1

        last = end - start
        if blocks[last][r]:
            results[last][r] = 0
        elif end < len(blocks) - 1 and results[last + 1][r] < results[start][r]:
            results[last][r] = results[last + 1][r] + 1

    start += 1
    end -= 1

# Here we have "points" for each block:
print(results)

# Get the index and sum of points for the block with
# minimum number of points:
res = min([(sum(r.values()), i) for i, r in enumerate(results)])

msg = 'Block {0} is most optimal with score {1}'
print(msg.format(res[1], res[0]))
