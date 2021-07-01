# Write a function that returns the minimum amount of total waiting time for all of the queries

# we're given a non-empty array of positive integers representing the amounts of time that specific queries take to excute.
# only one query can be executed at a time, but the queries can be executed in any order

# INPUTS/OUTPUTS
# [3, 2, 1, 2, 6] => 17

# NOTES
# we need the MINIMUM amount of time, so think of how we can add these up in a way that gives us the min time
# if we do it in the order, we get it:
# 3    2       1          2             6
# 0 + (3) + (3 + 2) + (3 + 2 + 1) + (3 + 2 + 1 + 2)
# 0 + 3   +    5    +    6        +  8              = 22 => NOT THE MIN, find another way

# if we do it with arr in asc order:
# [1, 2, 2, 3, 6]
# 0 + (1) + (1 + 2) + (1 + 2 + 2) + (1 + 2 + 2 + 3)
# 0 + 1   +    3    +   5         +   8             = 17

# if we do it with arr in desc order:
# [6, 3, 2, 2, 1]
# 0 + (6) + (6 + 3) + (6 + 3 + 2) + (6 + 3 + 2 + 2)
# 0 +  6  +  9      +  11         + 13             = already too big

# PSEUDOCODE
# arr.sort()

# total_time = 0
# loop through array (for idx in range(len(arr)))
# query_duration = arr[idx]
# remaining_queries = len(arr) - (idx + 1)
# total_time += query_duration * query_duration => we can multiply duration to remaining queries because we know the remaining queries will have to wait that same amount of time, so we preemptively add those in
# return total time


def minimumWaitingTime(queries):
    queries.sort()

    total_min_time = 0
    for idx, duration in enumerate(queries):
        remaining_queries = len(queries) - (idx + 1)
        total_min_time += remaining_queries * duration
    return total_min_time
