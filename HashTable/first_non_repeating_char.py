def first_non_repeating_char(string):
    dict = {}
    for char in string:
        dict[char] = dict.get(char, 0) + 1

    for char in string:
        if dict.get(char) == 1:
            return char
    return None


print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))

print(first_non_repeating_char("aabbcc"))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
