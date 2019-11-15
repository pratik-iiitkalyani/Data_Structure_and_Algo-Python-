# write a code to find out all positive whole
#number x and Y such that x*y = 130

def multiply():
    i = 1
    x = y = 0
    n = 130
    while i*n == 130 and i < 11:
        x += i
        y += n
        print(f"{x} and {y}")
        x = 0
        y = 0
        if (i%2 == 0): 
            i += 3
            n = int(130/i)
        elif (i%2 != 0):
            i *= 2
            n = int(130/i)
    
multiply()
        
