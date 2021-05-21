import time

def addupto(n):
    total = (n * (n + 1))/2
    return(total)

start = time.time()
addupto(100000)
end = time.time()
print(end - start)