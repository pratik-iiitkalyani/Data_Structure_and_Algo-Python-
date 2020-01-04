
def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)

def isEmpty(stack): 
    if len(stack) == 0: 
        return true 

def pop(stack): 
    if isEmpty(stack): return
    return stack.pop()

def reverse(string):
    n = len(string) 
    stack = createStack() 
  
    for i in string: 
        push(stack, i)

    string="" 
  
    for i in range(0,n):
        string+=pop(stack)
          
    return string 
string = "aqtw"
print(reverse(string))
