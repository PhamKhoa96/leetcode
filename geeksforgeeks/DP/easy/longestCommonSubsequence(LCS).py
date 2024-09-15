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
def findSubsequences(input: str):
    cache = {}
    if len(input) == 0:
        cache[''] = None
        return cache
    for c in findSubsequences(input[:len(input) - 1]):
        cache[c] = None
        cache[c + input[len(input)-1]] = None
    return cache

def LCS(input1, input2):
    result = ''
    tmp = findSubsequences(input1)
    for c in findSubsequences(input2):
        if c in tmp and len(c) > len(result):
            result = c
    return result

print(LCS('AGGTAB', 'GXTXAYB'))