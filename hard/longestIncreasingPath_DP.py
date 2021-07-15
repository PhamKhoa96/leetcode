"""
329. Longest Increasing Path in a Matrix

https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
"""


from typing import List

matrix = [[1, 2]]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        global stored_dp
        stored_dp = {}

        output = -1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output = max(output, self.longestIncreasingPath1(
                    matrix, [i, j]) + 1)

        return output

    def longestIncreasingPath1(self, matrix, start_point) -> int:
        global stored_dp

        m = len(matrix)
        n = len(matrix[0])

        y = start_point[0]
        x = start_point[1]

        if x < 0 or x >= n or y < 0 or y >= m:
            return 0

        current_value = matrix[y][x]

        around = self.findAround(matrix, start_point)

        valid_points = []
        for point in around:
            if current_value < matrix[point[0]][point[1]]:
                valid_points.append(point)

        if valid_points:
            output = -1
            for valid_point in valid_points:
                if str(valid_point) in stored_dp:
                    output = max(output, stored_dp[str(valid_point)])
                else:
                    output = max(output, self.longestIncreasingPath1(
                        matrix, valid_point))

            stored_dp[str(start_point)] = 1 + output
            return 1 + output

        stored_dp[str(start_point)] = 0
        return 0

    def findAround(self, matrix, start_point):
        result = []
        m = len(matrix)
        n = len(matrix[0])

        y = start_point[0]
        x = start_point[1]

        if x - 1 >= 0:
            result.append([y, x-1])
        if x + 1 < n:
            result.append([y, x+1])
        if y - 1 >= 0:
            result.append([y-1, x])
        if y+1 < m:
            result.append([y+1, x])
        return result


a = Solution()
print(a.longestIncreasingPath(matrix))
