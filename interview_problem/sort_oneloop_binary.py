# sort in one loop
# binary input
def sort(list):
    j = -1
    for i in range(len(list)-1):
        if list[i]<1:
            j = j+1
            list[i], list[j] = list[j], list[i]
    return list
list = [0,1,0,1,0,1,1]
print(sort(list))