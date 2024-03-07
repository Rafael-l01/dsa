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


def prefixSum2D(matrix):
    prefixSum = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            prefixSum[i + 1][j + 1] = (
                prefixSum[i + 1][j]
                + prefixSum[i][j + 1]
                - prefixSum[i][j]
                + matrix[i][j]
            )

    return prefixSum


class PrefixSumProblem2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefixSum = self.calculatePrefixSum2D()

    def calculatePrefixSum2D(self):
        prefixSum = [
            [0] * (len(self.matrix[0]) + 1) for i in range(len(self.matrix) + 1)
        ]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                prefixSum[i + 1][j + 1] = (
                    prefixSum[i + 1][j]
                    + prefixSum[i][j + 1]
                    - prefixSum[i][j]
                    + self.matrix[i][j]
                )

        return prefixSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row2 + 1][col1 - 1 + 1]
            - self.prefixSum[row1 - 1 + 1][col2 + 1]
            + self.prefixSum[row1 - 1 + 1][col1 - 1 + 1]
        )

