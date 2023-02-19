import sys

sys.stdin = open("input.txt")


def makePool(n, m):  # m 개 중 n 개를 조합한다 mCn
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # j 개 중 i 개를 조합한다 jCi
            if j == i:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = j
            else:
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    makePool(n, m)
