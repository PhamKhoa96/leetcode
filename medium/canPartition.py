"""
416. Partition Equal Subset Sum
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""


# Recursive
# check if in nums, there is any subset has total value of elements equal to sum
def isSubsetSum(nums, n, sum):
    if n < 0 and sum != 0:
        return False
    elif sum == 0:
        return True
    elif nums[n] > sum:
        return False
    else:
        return isSubsetSum(nums, n-1, sum) or isSubsetSum(nums, n-1, sum - nums[n])


def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    else:
        return isSubsetSum(nums, len(nums) - 1, sum(nums)/2)


print(canPartition([9, 1, 2, 4, 10]))


# DP
def isSubsetSum1(nums, n, sum1):
    global h

    h = [[None]*int(((sum(nums))+1)) for i in range(len(nums)+1)]

    n = int(n)
    sum1 = int(sum1)

    for i in range(n+1):
        for j in range(sum1+1):
            if i == 0 and j != 0:
                h[i][j] = False
            elif j == 0:
                h[i][j] = True
            elif nums[i] > sum1:
                h[i][j] = False
            else:
                h[i][j] = h[i-1][j] or h[i-1][j-nums[i]]

    return h[n][sum1]


def canPartition1(nums):
    if sum(nums) % 2 != 0:
        return False

    return isSubsetSum1(nums, len(nums) - 1, sum(nums)/2)


print(canPartition1([1, 2, 3, 5]))
