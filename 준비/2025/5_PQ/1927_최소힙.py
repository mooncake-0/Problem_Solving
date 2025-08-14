import sys, heapq

input = sys.stdin.readline

# 입력이 0 이면 hq 에서 최솟값 뽑기
# 입력이 0 이 아니면 hq 에 넣기
arr = []
N = int(input())
for _ in range(N):
    given = int(input())
    if given == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, given)
