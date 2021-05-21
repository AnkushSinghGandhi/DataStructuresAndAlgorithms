def addupto(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(addupto(int(input("Enter value of n: "))))