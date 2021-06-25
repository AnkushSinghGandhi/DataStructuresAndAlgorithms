# this solution has complexity of O(n*n)

arr1 = [1,2,3]
arr2 = [9,1,4]

def same(arr1, arr2):

    if(len(arr1) != len(arr2)):
        return False

    for i in range (0, len(arr1)):

        corret_index = arr2.index(arr1[i] ** 2)
        arr2.pop(corret_index)

    return True

print(same(arr1, arr2))