# Write a program to reverse an array or string
# using temp var
#method - 1
def reverse(string):
    i = 0
    j = len(string)-1
    string = list(string)
    while(i<j):
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        i += 1
        j -= 1
    return "".join(string)

str = "abc"
print(reverse(str))

# method - 2
# using recursion
def reverse()

