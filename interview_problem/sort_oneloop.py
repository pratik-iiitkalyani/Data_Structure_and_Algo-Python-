# sort in one loop
def sort(list):
    n = len(list)-1
    for i in range(n*n):
        pos = i%n
        if list[pos]>list[pos+1]:
            list[pos], list[pos+1] = list[pos+1], list[pos]
    return list
list = [3,5,1,6,10]
print(sort(list))