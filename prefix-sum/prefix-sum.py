def prefixSum(array):
    prefixSum = [0] * (len(array) + 1)

    for i in range(len(array)):
        prefixSum[i + 1] = prefixSum[i] + array[i]


def prefixSum2(array):
    prefixSum = [0]

    for num in array:
        prefixSum.append(prefixSum[-1] + num)


def prefixSum3(array):
    prefixSum = [0]

    for i, num in enumerate(array):
        prefixSum.append(prefixSum[i] + num)


class PrefixSumProblem:
    def __init__(self, nums):
        self.nums = nums
        self.prefixSum = self.calculatePrefixSum()

    def calculatePrefixSum(self):
        prefixSum = [0] * 10001
        for i in range(len(self.nums)):
            prefixSum[i + 1] = prefixSum[i] + self.nums[i]

        return prefixSum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]
