import sys
from collections import deque

sys.stdin = open("input_8.txt")

T = int(input())

for _ in range(T):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    sums = 0
    for index in range(N):
        mid = int((N - 1) / 2) # N은 홀수이므로, 일반식을 정리해줄 수 있다.
        if mid >= index:
            parts = farm[index][mid - index:mid + index + 1]
            sums += sum(parts)
        else:
            parts = farm[index][index - mid:3 * mid - index +1]
            sums += sum(parts)
    print(sums)
