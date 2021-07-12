class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_a = len(text1)
        length_b = len(text2)

        if length_a == 0 or length_b == 0:
            return 0

        elif text1[length_a-1] != text2[length_b-1]:
            return max(self.longestCommonSubsequence(text1[:length_a-1], text2[:length_b]), self.longestCommonSubsequence(text1[:length_a], text2[:length_b-1]))
        else:
            return 1 + self.longestCommonSubsequence(text1[:length_a-1], text2[:length_b-1])


a = "abc"
b = "def"

c = Solution()

print(c.longestCommonSubsequence(a, b))
