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

