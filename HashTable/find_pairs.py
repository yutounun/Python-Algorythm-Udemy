def find_pairs(arr1, arr2, target):
    """
    @returns tuple
    """
    set1 = set(arr1)
    rtn = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            rtn.append((complement, num))
    return rtn
        


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""