# The task was taken from
# https://www.youtube.com/watch?v=IWvbPIYQPFM
#

from random import choice


N = 50
M = 50
COLORS = [1, 2, 3]
# Generate colors
data = [0] * N
for i in range(N):
    data[i] = [0]*M
    for j in range(M):
        data[i][j] = choice(COLORS)

for line in data:
    print(*line)


colors_results = {}


def get_neighbors(i, j):
    """ This function returns all neighbors with
        the same colour.
    """

    color = data[i][j]
    data[i][j] = '*'  # mark all visited nodes by *

    results = []
    if i > 0 and data[i-1][j] == color:
        results.append((i-1, j))
    if j > 0 and data[i][j-1] == color:
        results.append((i, j-1))
    if i < N-1 and data[i+1][j] == color:
        results.append((i+1, j))
    if j < N-1 and data[i][j+1] == color:
        results.append((i, j+1))
    return results


def find_connected(i, j):
    color = data[i][j]
    connected_nodes = get_neighbors(i, j)

    if not connected_nodes:
        return 1

    result = 1
    for node in connected_nodes:
        if data[node[0]][node[1]] != '*':
            result += find_connected(*node)

    # Save information about the largest group
    # of fields with the same colour:
    if color not in colors_results or colors_results[color] < result:
        colors_results[color] = result

    return result


# Just iterate throw all the fields and recursevly
# mark all visited nodes by *, collecting the data
# about the number of nearest fields with the same colors
for i in range(N):
    for j in range(M):
        if data[i][j] != '*':
            res = find_connected(i, j)

for line in data:
    print(*line)

print(colors_results)
