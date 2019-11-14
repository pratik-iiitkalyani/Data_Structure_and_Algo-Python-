# list -> ['5', '4', '3', '1', '2']
# sort

# Noramal Method
l = ['5', '4', '3', '1', '2']
new_list = []
for i in l:
    new_list.append(int(i))
    new_list.sort()
print(new_list)
    
# using list compreshension
li = [int(i) for i in l]
li.sort()
print(li)

# lambda exp
x = lambda l: l
print(x(l))
    
