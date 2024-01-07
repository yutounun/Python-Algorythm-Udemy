class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def r_contains(self, val):
        return self.__r_contains(self.root, val)

    def __r_contains(self, current, target_val):
        if current is None:
            return False

        if current.value == target_val:
            return True

        # left
        if current.value > target_val:
            return self.__r_contains(current.left, target_val)
        if current.value < target_val:
            return self.__r_contains(current.right, target_val)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST Contains 27:")
print(my_tree.r_contains(27))

print("\nBST Contains 17:")
print(my_tree.r_contains(17))


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
