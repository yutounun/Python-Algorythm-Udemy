def merge(l1, l2):
    rtn = []
    p1 = 0
    p2 = 0

    while p1 != len(l1) and p2 != len(l2):
        if l1[p1] < l2[p2]:
            rtn.append(l1[p1])
            p1 += 1
        else:  # l2[p2] is less or equal to l1[p1]
            rtn.append(l2[p2])
            p2 += 1

    # Add remaining elements from l1 or l2
    if p1 < len(l1):
        rtn += l1[p1:]
    if p2 < len(l2):
        rtn += l2[p2:]
    return rtn


print(merge([1, 2, 7, 8], [3, 4, 5, 6]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
 """
