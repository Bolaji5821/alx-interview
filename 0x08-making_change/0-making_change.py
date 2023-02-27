#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        num_coins += total // coin
        total %= coin
    if total != 0:
        return -1
    return num_coins
