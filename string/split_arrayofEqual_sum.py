A = [2,1,4,7,12]
def split_list(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    half = sum/2
    sum1 = 0
    for i in range(len(A)):
        sum1 += A[i]
        if sum1 == half:
            break
    return sum1
print(split_list(A))