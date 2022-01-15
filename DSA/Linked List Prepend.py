class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next =  self.head
        self.node = new_node

llist = LinkedList()
llist.prepend_list("A")
llist.prepend_list("B")
llist.print_list()
