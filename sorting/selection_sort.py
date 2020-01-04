def sort(nums):
    for i in range(5):
        min = 0
        for j in range(i,6):
            if nums[j] < nums[min]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp
    return nums
nums = [5,3,8,6,7,2]
print(sort(nums))