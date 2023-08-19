import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()  # 이 순서대로 뽑아야함
# 자기 앞까지의 합을 기록해 놓자
sums = [0] * N
total = 0

for idx in range(N):
    if idx == 0:
        sums[idx] = times[idx]
    else:
        sums[idx] = sums[idx - 1] + times[idx]
    total += sums[idx]

print(total)