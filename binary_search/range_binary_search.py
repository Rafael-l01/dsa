# find the minimum value such as value is >= bound, but you don't know exactly what is the bound, you can have
# for example a function that return if you have a number bigger/equal or smaller than the bound for example
def lowerBoundBinarySearch(nums, bound):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] >= bound:
            ans = nums[middle]
            right = middle - 1
        else:
            left = middle + 1

    return ans


# find the maximum value such as value is <= bound, but you don't know exactly what is the bound, you can have
# for example a function that return if you have a number bigger or smaller/equal than the bound for example
def upperBoundBinarySearch(nums, bound):
    left = 0
    right = len(nums) - 1
    ans = -1

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] <= bound:
            ans = nums[middle]
            left = middle + 1
        else:
            right = middle - 1

    return ans
