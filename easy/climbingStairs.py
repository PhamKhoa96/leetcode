def climbStairs(n):
    arr = [0]*(n+1)
    print(arr)

    for i in range(n+1):
        if i == 0:
            arr[0] = 0
            continue
        if i == 1:
            arr[1] = 1
            continue
        if i == 2:
            arr[2] = 2
            continue
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


print(climbStairs(5))
