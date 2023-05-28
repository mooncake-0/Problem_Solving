import sys
from collections import deque

sys.stdin = open("input_5014.txt")
input = sys.stdin.readline

# total < 1,000,000
# u,d M 1,000,000
total, cur, tg, up, down = map(int, input().split())
visited = set()
floors = deque()
floors.append((cur, 0))
visited.add(cur)

is_finished = False
# 1 층 미만, total 초과가 될 수 없음
# 이미 갔던 층은 다시 가지 않는다
while floors:
    cur, times = floors.popleft()
    if cur == tg:
        is_finished = True
        print(times)
        break

    for choice in range(2):
        if choice == 0:
            next_floor = cur + up
        else:
            next_floor = cur - down
        if 0 < next_floor and total >= next_floor and next_floor not in visited:
            visited.add(next_floor)
            floors.append((next_floor, times + 1))

if not is_finished:
    print("use the stairs")