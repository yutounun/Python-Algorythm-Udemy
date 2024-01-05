def item_in_common(l1, l2):
    dict = {}
    # {1: True, 3: True, 5: True}
    for val in l1:
        dict[val] = True

    for val in l2:
        if val in dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]


print(item_in_common(list1, list2))


"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
