def balance(myStr):
    open = ["[","{","("]
    close = ["]","}",")"]
    stack = []
    for i in myStr:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i) 
            if ((len(stack) > 0) and (open[pos] == stack[len(stack)-1])): 
                stack.pop()
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    

myStr = "[{}{})(]"
print(balance(myStr))