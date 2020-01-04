# reverse words of a sentence

# "I Love My India"   =>    "India My Love I"

def reverse(s):
    s1 = s.split(" ")
    new_word = s1[::-1]
    return "",join(reversed(new_word))
s= "I Love My India"
print(reverse(s)
