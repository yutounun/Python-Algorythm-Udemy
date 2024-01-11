class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, given_list):
        if given_list.length < 1:
            return

        # original pointer
        p1 = self.head
        # given_list pointer
        p2 = given_list.head
        new_head = Node(0)  # 新しいリストのダミーヘッド
        p_new = new_head  # 新しいリストの現在のポインタ

        # Compare values of each list
        while p1 and p2:
            if p1.value < p2.value:
                p_new.next = p1
                p1 = p1.next
            else:
                p_new.next = p2
                p2 = p2.next
            p_new = p_new.next

        # どちらかのリストが終わった場合、残りの要素を追加
        if p1:
            p_new.next = p1
        elif p2:
            p_new.next = p2

        # 新しいリストのヘッドを更新
        self.head = new_head.next


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
