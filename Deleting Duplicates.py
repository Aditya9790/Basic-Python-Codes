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
#________________________________________________________________________________   
    def delete_duplicate(self):
        d = {} # Create a dictionary to store the values that we have encountered before.
        prev = None
        cur = self.head
        while cur is not None:
            if cur.data in d: # Remove the duplicate.
                prev.next = cur.next
                cur = None
            else:
                d[cur.data] = 1
                prev = cur
            cur = prev.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(2)
llist.append(6)
llist.append(7)
llist.append(8)
llist.append(6)
llist.append(2)
llist.delete_duplicate()
llist.print_list()