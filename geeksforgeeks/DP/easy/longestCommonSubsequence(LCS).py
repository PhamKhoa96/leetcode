# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
import sys
print(sys.getrecursionlimit())

# 1. Naive approach
"""
Input: S1 = “AGGTAB”, S2 = “GXTXAYB”
Output: 4
Explanation: The longest common subsequence is “GTAB”.
"""

# https://www.geeksforgeeks.org/print-subsequences-string/
# top-down (memoization)
def findSubsequence(input: str):
    cache = {}
    if len(input) == 0:
        cache[''] = None
        return cache
    for c in findSubsequence(input[:len(input) - 1]):
        cache[c] = None
        cache[c + input[len(input)-1]] = None
    return cache

# bottom-up (tabulation)
def findSubsequence2(input: str):
    arr = ['']
    for i in range(0, len(input)):
        arrTmp = []
        for j in arr:
            arrTmp.append(j+input[i])
        arr = arr + arrTmp
    return arr

def LCS(input1, input2, _callback = None):
    result = ''
    tmp = _callback(input1)
    for c in _callback(input2):
        if c in tmp and len(c) > len(result):
            result = c
    return result

print(LCS('AGGTAB', 'GXTXAYB', findSubsequence))
print(LCS('AGGTAB', 'GXTXAYB', findSubsequence2))
