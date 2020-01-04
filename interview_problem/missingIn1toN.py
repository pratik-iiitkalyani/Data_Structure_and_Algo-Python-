# find a 1 missing element in array containg element 1 to N(1 element missing) randomly

# Method - 1

# A = [1,8,3,10,2,5,7,6,9,11]
# sum = 0
# for i in range(len(A)):
#     sum += A[i]

# a = int(max(A))
# total = (a*(a+1))/2
# print("missing num is:" + " "+ str(total-sum))

# method - 2
# def missingNo(A): 
#     n = len(A) 
#     total = (n + 1)*(n + 2)/2
#     sumOfA = sum(A) 
#     return total - sumOfA 
  
# A = [1, 2, 4, 5, 6] 
# c = missingNo(A) 
# print(c) 

# method - 3(using XOR)

def missingNo(a, n): 
    x1 = a[0] 
    x2 = 1
      
    for i in range(1, n): 
        x1 = x1 ^ a[i] 
          
    for i in range(2, n + 2): 
        x2 = x2 ^ i 
      
    return x1 ^ x2 

  
a = [1, 2, 4, 5, 6] 
n = len(a) 
c = missingNo(a, n)  
print(c) 