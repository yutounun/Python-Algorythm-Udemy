def find_duplicates(nums):
    # Solution1
    # rtn = []
    # map = {}

    # for num in nums:
    #     if num in map and num not in rtn:
    #         rtn.append(num)
    #     else:
    #         map[num] = True
    # return rtn

    # Solution2
    num_counts = {}

    for num in nums:
        # {num: count}
        num_counts[num] = num_counts.get(num, 0) + 1
    # Include keys having a value of more than 1
    # duplicates = [num for num, count in num_counts.items() if count > 1]
    duplicates = []
    for key, count in num_counts.items():
        if count > 1:
            duplicates.append(key)
    return duplicates


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
