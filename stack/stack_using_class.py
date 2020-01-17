class Stack:
    def __init__(self):
        self.items = []

    def get_stack(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack is empty"

    def is_empty(self):
        return self.items == []

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return "stack is empty"

s = Stack()

print(s.top())
print(s.top())
s.push("a")
s.push("b")
print(s.get_stack())
s.push(10)
s.push(20)
print(s.pop())
print(s.top())
print(s.get_stack())

    