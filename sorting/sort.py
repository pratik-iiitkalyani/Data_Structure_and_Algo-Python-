def sort(a,n):
    j = -1
    for i in range(n):
        if a[i] < 1:
            j = j+1
            a[i],a[j] = a[j],a[i]
    return a
a = [0,0,1,1,0,1,0,0]
n = len(a)
print(sort(a,n))
