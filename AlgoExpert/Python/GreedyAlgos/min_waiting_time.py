# Write a function that returns the minimum amount of total waiting time for all of the queries

def minimumWaitingTime(queries):
    queries.sort()

    total_min_time = 0
    for idx, duration in enumerate(queries):
        remaining_queries = len(queries) - (idx + 1)
        total_min_time += remaining_queries * duration
    return total_min_time
