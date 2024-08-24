#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed to meet total.
    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount for which we need to make change.
    Returns:
        int: The fewest number of coins needed to meet the total,
              or -1 if it's not possible to meet the total.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
