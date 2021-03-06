# in 1 to N, one number is missing and other is repeting......find the missing element
# input = [2,1,3,3,5]
# output = 4


# Brute Force

# def missing_number(list):
#     l = []
#     sum = 0
#     repeted_num = 0
#     for i in list:
#         sum += i
#         if i not in l:
#             l.append(i)
#         else:
#             repeted_num += i
            
#     return ((len(list)+1)*len(list)/2)-(sum-repeted_num), repeted_num

l = [2,1,3,3,5]
# print(missing_number(l))

# first sort and traverse the array
# complexity O(nlogn)

# def fun(list):
#     list.sort()
#     # print(list)
#     repeted_num = 0
#     for i in range(len(list)):
#         if list[i] == list[i+1]:
#             repeted_num += list[i]
#             break
#     return repeted_num, 

# print(fun(l))


# method-3(using dictionary)
# time complexity - o(n)+ space-o(n)
def function(list):
    repeted_num = 0
    sum_list = 0
    d = {}
    for i in list:
        d[i] = list.count(i)
    
    for key, value in d.items():
        if value == 2:
            repeted_num += key
        sum_list += key
    return ((len(list)+1)*len(list)/2)-sum_list, repeted_num
        
        

print(function(l))

        
