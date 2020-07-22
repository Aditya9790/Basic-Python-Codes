class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
    
    def peek(self): # Tells what is topmost element of stack.
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
    #______________________________________________________________
    def is_match(self, p1, p2): # Checking a perfect match.
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        elif p1 == "[" and p2 == "]":
            return True  
        else:
            return False
    
    def is_paren_balanced(self, paren_string): # Checking Balanced Parenthesis.
        s = Stack()
        is_balanced = True
        index = 0
        while index < len(paren_string) and is_balanced:
            paren = paren_string[index]
            if paren in "([{": # Check whether the steing is in {([.
                s.push(paren) # If there then push in stack.
            else: # If not then
                if s.is_empty(): # Check whether the stack is empty
                    is_balanced = False
                else:
                    top = s.pop() # If not empty then check whether the char that is popped out is matched.
                    if not self.is_match(top, paren):
                        is_balanced = False
            index += 1
        if s.is_empty() and is_balanced:
            return True
        else:
            return False


s = Stack()
a = "()[]"
print(s.is_paren_balanced(a))
