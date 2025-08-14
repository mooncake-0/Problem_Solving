import sys, heapq

input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    given = int(input())
    if given == 0:
        if arr:
            a = heapq.heappop(arr)
            print(a[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(given), given))