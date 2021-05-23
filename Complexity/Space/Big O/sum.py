def sum(n):
    # One assignment
    total = 0  
    # One assignment of i for loop
    for i in range(0, len(n)):
        # Total won't take space because we are just adding to it.
        total += n[i]
    return total

# Space complexity is dependent on assignments.
# How much space is required to run an algo.
# And in Big O notation we look on big picture.
# complexity here is 2 which is constant.
# So complexity in Big O notation is O(1).
