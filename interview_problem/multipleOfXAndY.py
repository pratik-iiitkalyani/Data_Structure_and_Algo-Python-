# write a code to find out all positive whole
#number x and Y such that x*y = 130

def func(n):
    x  = []
    y = []
    for i in range(1,n):
        if (i*(n)) == 130:
            x.append(i)
            y.append(n-i-1)
    return "{} and {}".format(x, y)



n = 130
print(func(n))