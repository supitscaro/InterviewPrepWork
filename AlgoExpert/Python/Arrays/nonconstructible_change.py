# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
# The given coins can have any positive integer value and aren't neccessarily unique

# INPUTS/OUTPUTS
# [1, 1, 4] =>
# change = 1
# change = 1 + 1 = 2
# change = 2 + 3 = 5
# if coin is <= our previous change + 1, we can make all of the change previously
# and all the change between what we can make previously and this new coin

# SOLUTIONS
# sort arr in place
# variable 'change' equal to 0
# for coin in coins:
# if coin > change + 1:
# return change + 1
# change += coin
# return change + 1

def non_constructible_change(coins):
    coins.sort()

    current_change = 0

    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1
