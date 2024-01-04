class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key_arg):
        index = self.__hash(key_arg)

        if self.data_map[index] is None:
            return None

        for el in self.data_map[index]:
            key = el[0]
            val = el[1]
            if key == key_arg:
                return val


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)

print("Bolts:", my_hash_table.get_item("bolts"))
print("Washers:", my_hash_table.get_item("washers"))
print("Lumber:", my_hash_table.get_item("lumber"))


"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""
