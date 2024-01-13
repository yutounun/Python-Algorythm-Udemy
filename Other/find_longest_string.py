def find_longest_string(words):
    if len(words) == 0:
        return ""
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


string_list = ["apple", "banana", "kiwi", "pear"]
longest = find_longest_string(string_list)
print(longest)


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""
