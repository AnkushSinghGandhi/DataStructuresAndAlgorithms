# this solution has a complexity of O(n) 
# frequency counter pattern is used

arr1 = [1,7,3]
arr2 = [9,1,4]

def same(arr1, arr2):

    if(len(arr1) != len(arr2)):
        return False

    frequecy_counter1 = {}
    frequecy_counter2 = {}

    for val in arr1:

        if (val in frequecy_counter1):
            frequecy_counter1[val] += 1

        else:
            frequecy_counter1[val] = 1

    for val in arr2:
        
        if (val in frequecy_counter2):
            frequecy_counter2[val] += 1

        else:
            frequecy_counter2[val] = 1

    for val in frequecy_counter1:
        
        if (val ** 2 not in frequecy_counter2):
            return False

        if frequecy_counter2[val ** 2] != frequecy_counter1[val]:
            return False

    return True

print(same(arr1, arr2))