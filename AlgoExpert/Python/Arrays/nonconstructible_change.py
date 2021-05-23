# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
# The given coins can have any positive integer value and aren't neccessarily unique

def non_constructible_change(coins):
    coins.sort()

    current_change = 0

    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
