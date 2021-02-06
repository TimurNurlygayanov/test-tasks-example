# Example of simple FDS algorithm
# Based on https://www.youtube.com/watch?v=sBJ7ana1fgI
# with some small changes

flights = {'Moscow': ('New York', 'London', 'Paris', 'Beijing'),
           'New York': ('Moscow', 'London', 'Paris'),
           'London': ('New York', 'Moscow', 'Paris'),
           'Paris': ('Moscow', 'London', 'New York'),
           'Saratov': ('Moscow', 'Omsk'),
           'Omsk': ('Moscow', 'Saratov'),
           'Beijing': ('Moscow', 'New York', 'London')}
lengths = {}


def dfs(point, flights, n, used):
    used.add(point)

    for flight_end_point in flights[point]:
        if flight_end_point not in used:
            print(point, '->', flight_end_point)
            lengths[flight_end_point] = n + 1
            used = dfs(flight_end_point, flights, n + 1, used)

    return used


# Calculate length of flights from every city to all other
# available cities:
for point in flights:
    print('From', point)
    print(' - ' * 5)

    used = set()
    lengths = {}

    dfs(point, flights, 0, used)

    print(lengths)
    print('*' * 20)
    print()
