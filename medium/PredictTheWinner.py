"""
486. Predict the Winner
"""

nums = [0, 0, 7, 6, 5, 6, 1]


def PredictTheWinner1(nums):
    n = len(nums)

    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums)
    else:
        # print(f"'{nums[0]}' '+' 'PredictTheWinner1({nums[2:]})'")
        # print(f"'{nums[0]}' '+' 'PredictTheWinner1({nums[1:n-1]})'")
        # print(f"'{nums[n-1]}' '+' 'PredictTheWinner1({nums[:n-2]})'")
        # print(f"'{nums[n-1]}' '+' 'PredictTheWinner1({nums[1:n-1]})'")
        # print("-----------")
        return max(nums[0] + min(PredictTheWinner1(nums[2:]),  PredictTheWinner1(nums[1:n-1])),
                   nums[n-1] + min(PredictTheWinner1(nums[:n-2]),
                                   nums[n-1] + PredictTheWinner1(nums[1:n-1])))


print(PredictTheWinner1(nums))


def PredictTheWinner(nums):
    result = PredictTheWinner1(nums)

    if result >= sum(nums)/2:
        return True
    else:
        return False


print(PredictTheWinner(nums))
