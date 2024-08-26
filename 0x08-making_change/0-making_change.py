#!/usr/bin/python3
'''DSA Challenge
'''


def makeChange(coins, total):
    '''determine the fewest number of coins needed to meet a given amount total
    '''
    if total <= 0:
        return 0
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while total > 0:
        if coin_idx >= n:
            return -1
        if total - sorted_coins[coin_idx] >= 0:
            total -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
