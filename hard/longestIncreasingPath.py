"""
329. Longest Increasing Path in a Matrix

https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
"""

matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]


def findAround(matrix, start_point):
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


def longestIncreasingPath(matrix, start_point) -> int:
    m = len(matrix)
    n = len(matrix[0])

    y = start_point[0]
    x = start_point[1]

    if x < 0 or x >= n or y < 0 or y >= m:
        return 0

    current_value = matrix[y][x]

    around = findAround(matrix, start_point)

    valid_points = []
    for point in around:
        if current_value < matrix[point[0]][point[1]]:
            valid_points.append(point)

    if valid_points:
        output = -1
        for valid_point in valid_points:
            output = max(output, longestIncreasingPath(matrix, valid_point))
        return 1 + output

    return 0


def longestIncreasingPathTotal(matrix):
    output = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            output = max(output, longestIncreasingPath(matrix, [i, j]) + 1)

    return output


print(longestIncreasingPathTotal(matrix))
