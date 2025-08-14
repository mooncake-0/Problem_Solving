import sys, heapq

input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    given = int(input())
    if given == 0:
        if arr:
            print(-1*heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, -1*given)
