# str = "abaabcbac"
# find number of substring which contain at least one a,b,c 

def countSubString(str):
    a = 0
    b = 0
    c = 0
    for i in str:
        if i == a:
            a = 1+2*a
        elif i == b:
            b = a+2*b
        else:
            c = b+2*c
    return c
str = "abc"
print(countSubString(str))