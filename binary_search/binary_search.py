def binarySearch(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        # in languages like C++ or Java calculating the middle like middle = (start + end) // 2
        # can generate an integer overflow if the sum of start and end is bigger than the integer
        # maximum supported number, to solve it:
        # middle = start + ((end - start) // 2)
        middle = (start + end) // 2
        if target > nums[middle]:
            start = middle + 1
        elif target < nums[middle]:
            end = middle - 1
        else:
            return True

    return False


binarySearch([0, 1, 2, 3, 4, 5, 6], 0)
