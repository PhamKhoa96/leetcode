"""
392. Is Subsequence
"""


def isSubsequence(s, t):
    current_index = 0

    if len(s) == 0:
        return True

    for j in range(len(t)):
        if current_index < len(s):
            if t[j] == s[current_index]:
                current_index = current_index + 1

    if current_index == len(s):
        return True
    else:
        return False


s = "ca"
t = "abc"

print(isSubsequence(s, t))
