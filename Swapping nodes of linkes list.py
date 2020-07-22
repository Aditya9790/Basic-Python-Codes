class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#_________________________________________________________________________________
    # Swapping Nodes
    def swap_nodes(self, node1, node2):
        if node1 == node2:
            return
        
        prev1 = None
        cur1 = self.head
        while cur1 is not None and cur1.data != node1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 is not None and cur2.data != node2:
            prev2 = cur2
            cur2 = cur2.next

        # Check whether cur1 and cur2 actually exists.
        if cur1 == cur2:
            print("Cannot swap")

        # If node1 is head node.
        if prev1 == None:
            self.head = cur2
        else:
            prev1.next = cur2

        # If node2 is head node.
        if prev2 == None:
            self.head = cur1
        else:
            prev2.next = cur1

        # Swap the next pointer of 1 and 2.
        cur1.next, cur2.next = cur2.next, cur1.next
#_____________________________________________________________________________

    # Printing the elements of list.
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next
#________________________________________________________________________________
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
    
    # Recursive call to count the length.
    def len_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.len_recursive(node.next)



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.swap_nodes("A", "C")
#llist.print_list()
print(llist.len_recursive(llist.head))