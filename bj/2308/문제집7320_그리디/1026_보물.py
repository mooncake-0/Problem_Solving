import sys

input = sys.stdin.readline

N = int(input()) # <50
a = list(map(int, input().split())) # 얘를 움직여서 최소를 찾는다
b = list(map(int, input().split())) # Fixed

# 제일 큰 수는 제일 작은수와 곱해져야 한다(서로 역순이 되어야 함)
a.sort(reverse=True)
b.sort() # 차피 짝 맞춰줄거니까
S = 0
for idx in range(N):
    S += (a[idx]*b[idx])

print(S)