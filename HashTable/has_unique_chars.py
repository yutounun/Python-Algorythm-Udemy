def has_unique_chars(string):
    word = set()

    for char in string:
        if char in word:
            return False
        word.add(char)
    return True


print(has_unique_chars("abcdefg"))  # should return True
print(has_unique_chars("hello"))  # should return False
print(has_unique_chars(""))  # should return True
print(has_unique_chars("0123456789"))  # should return True
print(has_unique_chars("abacadaeaf"))  # should return False

# eedsa → False
# dhfye → True

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""
