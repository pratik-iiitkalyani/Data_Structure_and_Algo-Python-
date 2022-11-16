# Longest Span with same Sum in two Binary arrays

# Input: arr1[] = {0, 1, 0, 0, 0, 0};
#        arr2[] = {1, 0, 1, 0, 0, 1};
# Output: 4
# The longest span with same sum is from index 1 to 4.

def longest_span(l1, l2):

    maxLen = 0
    for i in range(0, len(l1)-1):
        sum1 = 0
        sum2 = 0
        for j in range(i, len(l1)-1):
            sum1 += l1[j]
            sum2 += l2[j]

            if (sum1 == sum2):
                length = j-i+1
                if length >maxLen:
                    maxLen = length
    return maxLen

print(longest_span([0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]))
