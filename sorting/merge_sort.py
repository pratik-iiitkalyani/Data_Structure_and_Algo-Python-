def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        l = list[0:mid]
        r = list[mid+1:len(list)-1]
        mergeSort(l)
        mergeSort(r)
    
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            list[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            list[k] = r[j]
            j += 1
            k += 1

def printList(list):
    for i in range(len(list)):
        print(list[i])


list = [12, 11, 13, 5, 6, 7]
print(mergeSort(list))
            