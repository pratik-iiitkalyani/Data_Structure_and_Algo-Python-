# find the prime number between two number

# method-1
# time complexity - 0(n^2)
lower = int(input("enter the lower num: "))
upper = int(input("enter the upper num: "))
# print("Prime numbers between",lower,"and",upper,"are:")

# for num in range(lower, upper + 1):
#     # prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# method-1
# skip the even number
for num in range(lower, upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        if num % 2 != 0 & num > 2:
            continue
        else:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
