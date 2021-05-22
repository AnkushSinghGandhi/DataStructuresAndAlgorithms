def addupto(n):
    # 1 assignmnet
    total = 0
    # loop runs n times
    for i in range(1, n+1):
        # 1 assignment
        total += i
        return total

# runs 1 times
print(addupto(int(input("Enter value of n: "))))

# Each statement outside a loop will have 1 time complexity.
# And time complexity of statements inside a loop is n. where n is no. of times a loop runs. 
# Big O upper bounds the time complexity.
# wich means an algo can have Big O or less complexity. 
# total complexity is n + 2 but in Big O we look into big picture.
# And we neglect all constants.
# So complexity is O(n).
# O(n^2 + 2n) in this case we neglect 2n because it's lot less then compared to n^2 for bigger input.