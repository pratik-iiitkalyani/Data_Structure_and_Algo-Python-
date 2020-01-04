def isCreate():
    stack = []
    return stack
def isEmpty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
    print(item+" "+"is pushed")
def pop(stack):
    stack.pop()
    print(stack.pop()+"is poped")
def top(stack):
    return stack[-1]

stack = isCreate()
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(top(stack)) 

