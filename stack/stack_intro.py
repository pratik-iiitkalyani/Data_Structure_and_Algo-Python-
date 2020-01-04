class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def top(self):
        return self.items[-1]

    def get_stack(self):
        return self.items
    
s = Stack()
s.push(10)
s.push(20)
print(s.get_stack())
s.push("a")
s.push("b")
print(s.get_stack())
s.pop()
print(s.top())