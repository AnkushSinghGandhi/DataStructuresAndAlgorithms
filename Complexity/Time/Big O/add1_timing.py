import time

def addupto(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

start = time.time()
addupto(100000)
end = time.time()
print(end - start)