x = -123


def reverse(x):
    temp = ""
    if x == 0:
        return x
    elif x < 0:
        x = -x
        for i in range(len(str(x))):
            temp = temp + str(x)[(len(str(x)) - i - 1)]
        if -int(temp) & -0x80000000 != -0x80000000:
            return 0
        else:
            return -int(temp)
    else:
        for i in range(len(str(x))):
            temp = temp + str(x)[(len(str(x)) - i - 1)]
        if int(temp) & 0x7fffffff != int(temp):
            return 0
        else:
            return int(temp)


print(reverse(x))
