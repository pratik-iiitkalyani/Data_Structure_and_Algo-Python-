# Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day".

def fun(s):
    i = 0
    s = list(s)
    s1 = ""
    a = "aeiouAEIOU"
    for i in range(len(s)-1):
        if s[i] in a:
            s1+=s[i]
    return s1
str = "Hello, have a good day"
print(fun(str))
