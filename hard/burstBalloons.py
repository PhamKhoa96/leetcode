""""
312. Burst Balloons
"""

p = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3, 3]


# Recursive
def maxCoins(nums):
    result = -2147483648

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        temp = nums[0]
        nums.remove(min(nums))
        return temp + maxCoins(nums)
    elif len(nums) == 2:
        temp = nums[0]*nums[1]
        nums.remove(min(nums))
        return temp + maxCoins(nums)
    elif len(nums) == 3:
        return max(nums[0]*nums[1] + maxCoins([nums[1], nums[2]]),
                   nums[0]*nums[1]*nums[2] + maxCoins([nums[0], nums[2]]),
                   nums[1]*nums[2] + maxCoins([nums[0], nums[1]])
                   )
    else:
        for i in range(1, len(nums)-1):
            result = max(result, nums[i-1]*nums[i]*nums[i+1] +
                         maxCoins(nums[:i] + nums[i+1:]))
        return result


print(maxCoins(p))


# DP
def maxCoins1(nums):
