class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Printing the elements of list.
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Inserting at the end
    def append(self, data):
        new_node = Node(data)

        # If list is empty.
        if self.head is None:
            self.head = new_node
            return

        # If there are already some elements in the list.
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

# Inserting at the beginning
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next =  self.head
        self.head = new_node
        
    # Inserting in between
    def insert(self, prev_node, data):

        if not prev_node:
            print("Previous Node not present")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
# If want to send string as a node in insert:
    '''def insert(self, prev_node, data):
        new_node = Node(data)
        cur_node = self.head

        while cur_node.data != prev_node:
            cur_node = cur_node.next
            if cur_node is None:
                print("previous node is not present in the list")
                return
        new_node.next = cur_node.next
        cur_node.next = new_node'''

    # Deletion
    def delete_node(self, key):
        cur_node = self.head
        # Deleting a head node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Deleting a node which isn't a head node.
        prev = None
        # Keep a track of previous and the current element
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Counting elements of list or no. of nodes
    def length_of_list(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    # Counting length in a recursive manner

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + len_recursive(node.next)




llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#print("By Simple Loop:", llist.length_of_list())
#print("By Recursive Call:", llist.len_recursive(llist.head))
#llist.delete_node("B")
llist.prepend("E")
#llist.insert(llist.head.next.next, "K")
llist.print_list()