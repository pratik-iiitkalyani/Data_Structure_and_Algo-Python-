# method - 1 

def min_square(num):
    if (num == 0) or (num == 1):
        return num
    for i in range(1,num):
        if i*i > num:
            return i-1
    
print(min_square(2))

# method - 2

# def minimum_of_square(x):
#     #base case
#     if (x == 0) or (x == 1):
#         return x
#     start = 1
#     end = x
#     while(start <= end):
#         mid = (start + end)//2
#         if mid*mid == x:
#             return mid
#         elif mid*mid < x:
#             start = mid+1
#             ans = mid
#         else:
#             # mid*mid >x
#             end = mid-1
            
#     return ans

# print(minimum_of_square(8))
