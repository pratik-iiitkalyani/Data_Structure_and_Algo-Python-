# from a given list we have to find first missing +ve number
# input - [-8,0,10,11], output - 1
# input - [1,-2,3,0], output - 2


# method-1
# time complexity - o(nlogn)
def missing_positive_num(list):
    list.sort()
    for i in list:
        if i+1 not in list and i+1> 0 and i+1 < len(list)+1:
            return i+1
        else:
            continue

l = [-8,0,10,1]
l1 = [-1, 2, 3, 1, 4]
print(missing_positive_num(l1))

# method-2
# time complexity - o(n) + o(1)

# def missing_first_positive_num(list):
#     for i in range(len(list)):
#         if list[i] > 0 and list[i] < len(list)+1:
#             list[list[i]] = list[i]
#             print(list[i])
#         else:
#             continue
#     print(list)
    
    # i = 1
    # while(i<len(list)):
    #     if list[i] != i:
    #         return i

# print(missing_first_positive_num(l1))