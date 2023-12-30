class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(my_linked_list, k):
    """
    - Don't use length propperty
    - Utilize two pointers
    """
    fast = my_linked_list.head
    slow = my_linked_list.head

    # fast moves k steps forward
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4    
"""
