# Find a pair with maximum product in array of Integers

# Input: arr[] = {1, 4, 3, 6, 7, 0}
# Output: {6,7}

# Input: arr[] = {-1, -3, -4, 2, 0, -5}
# Output: {-4,-5}

# method -1
# def maxProduct(l):
#     newArray = []
#     for i in l:
#         if i < 0:
#             newArray.append(-i)
#         else:
#             newArray.append(i)
#     max1 = 0
#     max2 = 0
#     for i in newArray:
#         if max1 < i:
#             max1 = i
#     newArray.pop(max1)
#     for i in newArray:
#         if max2 < i:
#             max2 = i
#     if -max1 in l:
#         max1 = -max1
#     if -max2 in l:
#         max2 = -max2
#     print(max1, max2)

#method - 2
# Time Complexity : O(n2)
# def maxProduct(l):
#     if len(l) < 2:
#         print('Pair can not exist')
#         return
#     a = l[0]
#     b = l[1]
#     maxProd = a*b
#     for i in range(0, len(l)):
#         for j in range(i+1, len(l)):
#             if l[i]*l[j] > maxProd:
#                 maxProd = l[i]*l[j]
#                 a = l[i]
#                 b = l[j]
#     print(a, b)
#     print(maxProd)


# maxProduct([-1, -3, -4, 2, 0, -5])

# method - 3
# Time Complexity : O(nlogn)

def maxProduct(l):
    l.sort()
    sum1 = l[0]*l[1]
    sum2 = l[len(l)-1]*l[len(l)-2]
    if sum1 > sum2:
        print(l[0], l[1])
    else:
        print(l[len(l)-1], l[len(l)-2])


maxProduct([-1, -3, -4, 2, 0, -5])
