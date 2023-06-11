import sys
from collections import deque

input = sys.stdin.readline

start, tg_start = map(int, input().split())
visited = [-1] * 500001
# start > 수빈이는 1초 동안 -1, +1, *2 에 대해 이동할 수 있다
# tg 은 매초 위치가 +a 씩 증가한다
# a 는 1초 뒤 +1 2초뒤 +1+2, 3초 두 ㅣ+1+2+3 씩 증가한다

'''
1초 = 1 + 1 = 1+1
2초 = 1 + 1 + 2 = 1+3
3초 = 1 + 1 + 2 + 3 = 1+6
4초 = 1 + 1 + 2 + 3 + 4 = 1+10
5초 = .... = 1 + 15
...
t = 1 + n(n+1)/2
'''

# 따라서 동생의 위치는 t 초 뒤에는 t = 1 + (t(t+1)/2)

dq = deque()
dq.append((start, 0))
visited[start] = 1
is_done = False

# 미리 동생의 t초별 포지션들을 표시해놔보자
for t in range(1000):

    tg = tg_start + (t * (t + 1) // 2)
    if tg > 500000:
        break
    else:
        visited[tg] = t

while dq:

    # print(len(dq))
    cur_position, times = dq.popleft()

    if visited[cur_position] == times:
        is_done = True
        print(times)
        break

    for i in range(3):
        if i == 0:  # cur_position +1
            if cur_position + 1 <= 500000 and visited[cur_position + 1] != -2:
                if visited[cur_position + 1] == -1:
                    visited[cur_position + 1] = -2
                dq.append((cur_position + 1, times + 1))
        elif i == 1:  # cur_position -1
            if cur_position - 1 >= 0 and visited[cur_position - 1] != -2:
                if visited[cur_position - 1] == -1:
                    visited[cur_position - 1] = -2
                dq.append((cur_position - 1, times + 1))
        else:  # cur_position *2
            if cur_position * 2 <= 500000 and visited[cur_position * 2] != -2:
                if visited[cur_position * 2] == -1:
                    visited[cur_position * 2] = -2
                dq.append((cur_position * 2, times + 1))

if not is_done:
    print(-1)
