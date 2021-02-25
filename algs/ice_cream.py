# The task was taken from this video
# https://www.youtube.com/watch?v=Ifwf3DBN1sc
# We want to spend all money and buy 2 different flavors

menu = {'Strawberry': 2,
        'Blueberry': 7,
        'Nutella': 13,
        'Vanilla': 5,
        'Banana': 4,
        'Bublegum': 13,
        'Chocolate': 5}


def buy_ace_cream(menu, total_money: int) -> list:
    difference_hash = {}

    # Create a hashmap with diff in the price
    for i, (item, price) in enumerate(menu.items()):
        diff = total_money - price
        difference_hash.setdefault(diff, []).append((item, i))

    results = set()  # we need to take only unique combinations of flavors

    for i, (item, price) in enumerate(menu.items()):
        for j, pos in difference_hash.setdefault(price, []):
            if j != item:  # check if it is not the same flavour
                results.add((min(i, pos), max(i, pos)))

    return list(results)


examples = [10, 13, 18, 4, 7, 101]
for total_money in examples:
    result = buy_ace_cream(menu, total_money)
    print('${0:4} -> {1}'.format(total_money, result))
