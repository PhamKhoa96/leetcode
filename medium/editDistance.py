# recursive
def minDistance(word1, m, word2, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    elif word1[m-1] == word2[n-1]:
        return minDistance(word1, m-1, word2, n-1)
    else:
        return 1 + min(
            minDistance(word1, m-1, word2, n),  # Remove
            minDistance(word1, m, word2, n-1),  # Insert
            minDistance(word1, m-1, word2, n-1)  # Replace
        )


word1 = "b"
word2 = "a"

print(minDistance(word1, len(word1), word2, len(word2)))


# DP
def minDistance1(word1, word2):
    m = len(word1)
    n = len(word2)

    if m == 0:
        return n
    if n == 0:
        return m

    h = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                h[i][j] = j
            elif j == 0:
                h[i][j] = i
            elif word1[i-1] == word2[j-1]:
                h[i][j] = h[i-1][j-1]
            else:
                h[i][j] = 1 + min(h[i-1][j], h[i][j-1], h[i-1][j-1])

    print(h)

    return h[m][n]


print(minDistance1(word1, word2))
