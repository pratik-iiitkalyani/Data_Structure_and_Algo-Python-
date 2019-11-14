# write a code to find out all positive whole
#number x and Y such that x*y = 130

def func():
    i = 1
    n = 130
    x = 0
    y = 0
    while i*n == 130:
        x += i
        y += n
        # if i<=26:
        print("{} and {}".format(x, y))
        if (i%2 == 0): 
            i += 3
            n = int(130/i)
        elif (i%2 != 0):
            i *= 2
            n = int(130/i)
        # elif (i%2 == 0 and i>= 26):
        #     i += 39
        #     n = int(130/i)
        x = 0
        y = 0
        # else:
        #     print(i)
        #     x = 0
        #     y = 0
        #     if (i%2 == 0): 
        #         i += 39
        #         n = int(130/i)
        #         print("{} and {}".format(x, y))
        #     elif (i%2 != 0):
        #         i *= 2
        #         n = int(130/i)
        #         print("{} and {}".format(x, y))

func()