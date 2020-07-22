class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #_____________________________________________________________________________

    # Printing the elements of list.
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next
    #_____________________________________________________________________________

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
    #______________________________________________________________

    # Checking Palindrome.
    def is_palindrome(self):
        # Method 1
        s = ""
        p = self.head
        while p is not None:
            s += p.data
            p = p.next
        if s == s[::-1]:
            return "Is Palindrome."
        else:
            return 0

        # Method 2
        

llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")
print(llist.is_palindrome())