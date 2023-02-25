import sys
import heapq as hq

sys.stdin = open("input_10.txt")
a = []
while True:
    num = int(input())
    if num == 0:
        print(hq.heappop(a))
    elif num == -1:
        break
    else:
        hq.heappush(a, num)
        # 나는 여기서 a.append() 를 하고, 위에서 num ==0 일 시 매번 heapify 해줌. 별로임.
