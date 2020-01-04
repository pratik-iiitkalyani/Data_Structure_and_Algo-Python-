# there is a string you have to replace vowel with vowel from back end
# e->u
# o->o

# Write a function that takes a string as input and reverse only the vowels of a string.


# method - 1

# def reverseVowels(s):
#     # str to list ('str' object does not support item assignment)
#     s = list(s)
#     vowel = "aeiouAEIUO"
#     i = 0
#     j = len(s) - 1
#     while (i < j):
#         while (s[i] not in vowel and i < min(len(s) - 1,j)):
#             i += 1
#         while (s[j] not in vowel and j > max(0,i)):
#             j -= 1
#         s[i],s[j] = s[j],s[i]
#         i += 1
#         j -= 1
#     return ''.join(s)
# str = "Hello, How are you"
# print(reverseVowels(str))



# method - 2

def reverseVowels(s):
    s = list(s)       # str to list ('str' object does not support item assignment
    vowel = "aeiouAEIUO"
    i = 0
    j = len(s) - 1
    while (i < j):
        if s[i] in vowel:
            if s[j] in vowel:
                s[i],s[j] = s[j],s[i]
            j -=1
        i += 1    
    return ''.join(s)
str = "Hello, How are you"
print(reverseVowels(str))
