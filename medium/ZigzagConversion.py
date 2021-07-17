"""
6. ZigZag Conversion

PAYPALISHIRING


row = 1         --> distance = 1

row = 2         --> distance = 2


row = 3
P   A   H   N   --> distance = 4 = 2*(row-1)    --> row 0
A P L S I I G
Y   I   R       --> distance = 4    --> row 2


row = 4         --> distance = 6    --> row 0
P     I    N
A   L S  I G
Y A   H R
P     I         --> distance = 6    --> row 3


row = 6
P         R     --> distance = 10
A       I I
Y     H   N
P   S     G
A I
L


"""

s = "PAYPALISHIRING"


def getCharater(s, x, y, distance):
    n = len(s)

    result = ""

    if x == y or y - x == distance:
        while (x < n):
            result = result + s[x]
            x = x + distance
        return result

    while(x < n or y < n):
        if y >= n:
            result = result + s[x]
        elif x >= n:
            result = result + s[y]
        else:
            result = result + s[x] + s[y]
        x = x + distance
        y = y + distance

    return result


def convertZigzag(s, numRows):
    result = ""

    if numRows == 0:
        return result
    if numRows == 1:
        return s

    distance = 2*(numRows - 1)

    for i in range(numRows):
        result = result + getCharater(s, 0 + i, 0 + distance - i, distance)

    return result


print(convertZigzag(s, 1))

# convertZigzag(s, 4)
