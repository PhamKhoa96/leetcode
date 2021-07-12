def LCS(a, b, m, n):

    h = [[0]*(n+1)]*(m+1)

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                h[i][j] = 0
                print("case 1")
            elif a[i-1] == b[j-1]:
                h[i][j] = 1 + h[i-1][j-1]
            else:
                h[i][j] = max(h[i-1][j], h[i][j-1])

    print(h)
    return h[m][n]


X = "abcba"
Y = "abcbcba"

print(LCS(X, Y, len(X), len(Y)))
