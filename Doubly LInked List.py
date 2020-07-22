class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #______________________________________________________________
    
    # Appending in the list
    def append(self, data):
        new_node = Node(data)
        # Checking whether the list is empty.
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node 
            new_node.prev = cur_node
            new_node.next = None
    #___________________________________________________________

    # Prepending in list.
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:   
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    #____________________________________________________________
     
     # Adding after a node.
    def add_after_node(self, key, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node is not None:
            if cur_node.next is None and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                nxt = cur_node.next
                cur_node.next = new_node
                new_node.next = nxt
                new_node.prev = cur_node
                nxt.prev = new_node
            cur_node = cur_node.next
    #____________________________________________________________
    def add_before_node(self, key, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node is not None:
            if cur_node.prev is None and cur_node.data == key:
                self.prepend(data)
                return
            elif cur_node.data == key:
                bef = cur_node.prev
                cur_node.prev = new_node
                new_node.prev = bef
                bef.next = new_node
                new_node.next = cur_node
            cur_node = cur_node.next
    #____________________________________________________________
    def delete(self, key):# Delete a node.
        cur_node = self.head
        if cur_node and cur_node.data == key: # If node is head node.
            nxt = cur_node.next
            nxt.prev = None
            self.head = nxt
            cur_node = None
            return
        while cur_node is not None and cur_node.data != key:
            cur_node = cur_node.next
        if cur_node is None:
            return
        if cur_node.next is not None: # If node is not a head and not a last node.
            nxt = cur_node.next
            bef = cur_node.prev
            nxt.prev = bef
            bef.next = nxt
            cur_node = None
        
        last_node = self.head
        while last_node.next is not None: # If a node is last node.
            last_node = last_node.next
        bef = last_node.prev # Set bef as equal to last_node's previous pointer and then set bef's next to none and last_node's next to none.
        bef.next = None
        last_node = None
    
    #____________________________________________________________
    def reverse(self): # Reversing the list.
        temp = None
        cur_node = self.head
        while cur_node is not None:
            temp = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = temp
            cur_node = cur_node.prev
        if temp is not None:
            self.head = temp.prev
    #______________________________________________________________
    
    # Printing elements of list.
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

ddlist = DoublyLinkedList()
ddlist.append(1)
ddlist.append(2)
ddlist.append(3)
ddlist.append(4)
ddlist.add_after_node(2, 100)
ddlist.add_before_node(4, 7)
#ddlist.delete(1)
#ddlist.delete(100)
#ddlist.delete(4)
#ddlist.delete(7)
ddlist.reverse()
ddlist.print_list()


