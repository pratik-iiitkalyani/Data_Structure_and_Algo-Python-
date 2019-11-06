
# initializes the stack
def createStack():
    stack = []
    return stack

# stack is empty when stack size is 0 
def isEmpty(stack):
    return len(stack) == 0

# function to remove element. it dec the size by 1
def pop(stack):
    if(isEmpty(stack)):
        return str(maxsize - 1)
    return stack.pop()

# Function to add an item to stack. It increases size by 1 
def push(stack, item):
    stack.append(item)
    print(item +" "+ "pushed to stack")

# Function to return the top from stack without removing it
def top(stack):
    if(isEmpty(stack)):
        return str(maxsize - 1)
    return stack[len(stack)-1]

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
# pop(stack)
print(pop(stack) + " popped from stack")
print(top(stack))
print(top(stack) + " is at top of the stack")
print(stack)