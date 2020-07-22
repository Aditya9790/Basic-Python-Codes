class Stack():
    def __init__(self):
        self.items = []
    def push(self, items):
        self.items.append(items)
    def pop(self):
        self.items.pop()
    def count_items(self, list):
        count = 0
        while self.items.pop() is not None:
            count += 1
        return count

    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items


    def check_balanced_parens(self, parens):
        s = Stack()
        flag = True
        index = 0
        while index < len(parens):
            paren = paren[index]
            if paren in "([{":
                s.push(paren)
            else:
                if not paren()
                pass

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.get_stack())
print(s.count_items(s))
        