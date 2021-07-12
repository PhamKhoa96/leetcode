""""
Ex1:
sunday --> 6 ki tu
saturday --> 8 ki tu
output : 3 : replace,insert,insert
same: suday --> 5 ki tu

suday
sunday
output: 1 : insert ( = 6 - 5)

suday
saturday
output: 3 : insert, insert, insert ( = 8 - 5)

->>> ketqua = max(1,3) = 3



Ex2:
horse --> 5 ki tu
ros --> 3 ki tu
ouput: 3 : replace, remove, remove
same: os -> 2 ki tu

os
horse
output: 3 : insert, insert, insert

os 
ros
output: 1: insert

->>> ketqua = max(3,1) = 3


Ex3:
intention --> 9 ki tu
execution --> 9 ki tu
output: 5 : remove, replace, replace, replace, insert
same: etion --> 5 ki tu

etion
intention
output: 5 : insert, insert, insert, insert, insert

etion
execution
output: 5 : insert, insert, insert, insert, insert

->>> ketqua = max(5,5) = 5


Ex4:
ABCDGH --> 6 ki tu
AEDFHR --> 6 ki tu
output: 4 : replace, insert, replace, insert
same: ADH --> 3 ki tu

ADH
ABCDGH
output: 3 : insert, insert, insert

ADH
AEDFHR
output: 3 : insert, insert, insert

->>> ketqua = max(3,3) = 3 -> sai

"""


def LCS(a, b):
    length_a = len(a)
    length_b = len(b)

    if length_a == 0 or length_b == 0:
        return 0

    elif a[length_a-1] != b[length_b-1]:
        return max(LCS(a[:length_a-1], b[:length_b]), LCS(a[:length_a], b[:length_b-1]))
    else:
        return 1 + LCS(a[:length_a-1], b[:length_b-1])


a = "abc"
b = "def"

print(LCS(a, b))


def minDistance(word1, word2):
    lcs = LCS(word1, word2)
    return max(len(word1) - lcs, len(word2) - lcs)


print(minDistance(a, b))
