def sort(a):
    n = len(a)-1
    for i in range(n*n):
        pos = i%n
        if a[pos] > a[pos+1]:
            a[pos], a[pos+1] = a[pos+1],a[pos]
    return a
a = [4,5,3,12,1,18]
print(sort(a))