# Example was taken from
# https://www.youtube.com/watch?v=sn0DWI-JdNA
# We have amount of money and the coins,
# and we need to find out how many ways of exchange
# we have


def get_exchange(total_amount: int, coins: list) -> int:
    if total_amount == 0:
        return 1
    if len(coins) == 0:
        return 0

    options_count = 0

    for i, coin in enumerate(coins):
        remains_money = total_amount
        while remains_money >= coin:
            remains_money -= coin
            options_count += get_exchange(remains_money, coins[i+1:])

    return options_count


examples = [{'amount': 20, 'coins': [5, 3, 1]},
            {'amount': 79, 'coins': [50, 25, 10, 5, 1]},
            {'amount': 27, 'coins': [7, 5, 3, 1]},
            {'amount': 3, 'coins': [7, 5, 3, 1]},
            {'amount': 51, 'coins': [12, 8, 2]}]

for sample in examples:
    result = get_exchange(sample['amount'], sample['coins'])
    print('{0} -> {1}'.format(sample, result))
