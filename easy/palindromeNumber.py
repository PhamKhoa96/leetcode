x = -1241


def isPalindrome(x):
    if x < 0:
        return False
    flag = True
    for i in range(len(str(x))):
        if i >= len(str(x)) - i - 1:
            return flag
        if str(x)[i] == str(x)[len(str(x)) - i - 1]:
            continue
        else:
            flag = False


print(isPalindrome(x))
