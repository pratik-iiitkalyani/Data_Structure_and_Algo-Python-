# Write a program to print the words of a string in reverse order.
# Sample Test Cases:
# INPUT: Hi I am example for this program
# OUTPUT: Program this for example am I Hi

def revrseSentanse(str):
    # spilt all the word present in the sentance
    sentance = str.split(" ")
    # the first letter of last word of sentance will be capital
    sentance[-1] = sentance[-1].title()

    # reverse the sentance
    input = sentance[::-1]

    # join the words
    output = ' '.join(input)
    return output


str = "Hi I am example for this program"
print(revrseSentanse(str))
