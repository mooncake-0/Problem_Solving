import sys

sys.stdin = open("input_11726.txt")
input = sys.stdin.readline

'''
dp[n] 까지 방법의 수가 저장되었다고 생각해보자.
dp[n+1] 이라면 네모 타일 하나가 붙을 것이다
dp[n+2] 라면 네모 타일 두 개가 붙는 것은 사실 n+1 에서 중복되는 카운트, 따라서 가로 두개만 붙는 겨우만 더해진다
여기까지 하면 됨. 나머지는 다 누적될 것 
'''

# 2*1  은  한가지
# 2*2  은 두가지
N = int(input())
dp = [0] + [0] * N
if N <=3:
    print(N)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[len(dp)-1]%10007)
