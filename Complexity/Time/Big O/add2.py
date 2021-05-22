def addupto(n):
    # 1 assignmnet
    total = (n * (n + 1))/2
    return(total)

# runs 1 time 
print(addupto(int(input("Enter value of n: "))))

# total complexity is 2 but in Big O we neglect all constants.
# So complexity is O(1).
# O(1000) = O(1)
# O(20) = O(1)