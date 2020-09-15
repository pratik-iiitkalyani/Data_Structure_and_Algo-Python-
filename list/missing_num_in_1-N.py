l = [1,2,3,4,6]

# complexity O(n) 

def missing_num(l):
    max = 0
    sum = 0
    for i in l:
        if i > max:
            max = i
        sum += i
    return max*(max+1)/2-sum

print(missing_num(l))