def prime(number):
    list = []
    for num in range(2, number):
        if num>1:
            for i in range(2, num^2):
                if num%i == 0:
                    break
                else:
                    list.append(num)
    return list

print(prime(10))