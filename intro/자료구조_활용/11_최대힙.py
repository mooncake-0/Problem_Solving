import sys
import heapq as hq

# 파이썬에서 최대힙은 등호 변경을 통해서 구현한다.
sys.stdin = open("input_11.txt")
a = []
while True:
    num = int(input())
    if num == 0:
        print(hq.heappop(a) * -1)
    elif num == -1:
        break
    else:
        hq.heappush(a, -num)
