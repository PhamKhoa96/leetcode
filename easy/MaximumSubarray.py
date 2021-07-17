"""
53. Maximum Subarray
"""


nums = [-1]


def findMax(arr):
    n = len(arr)

    output = -2147483648

    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or i == j or i-j > 0:
                continue
            output = max(output, arr[i][j])

    return output


def maxSubArray(nums):
    n = len(nums)

    table = [[-2147483648]*(n+1+1) for x in range(n+1+1)]

    for i in range(n+1):
        for j in range(i, n+1):
            if (n - j) > n or (n - j) < 0 or (n - i) > n + 1 or (n - i) < 1:
                continue
            if j - i == 1:
                table[n - i][n - i] = 0
            if n - j >= n:
                table[n - j][n - i] = 0 + \
                    table[n - j + 1][n - i]
            else:
                table[n - j][n - i] = nums[n -
                                           j] + table[n - j + 1][n - i]

    return findMax(table)


print(maxSubArray(nums))
