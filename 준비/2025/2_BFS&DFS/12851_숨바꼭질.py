import sys
from collections import deque

sys.stdin = open("input_12851.txt")

# 수빈이는 언제나 x-1, x+1 혹은 2x 로 이동
# 그 때마다 3가지 선택을 가지고 이동

# N, K 는 <=100,000
N, K = map(int, input().split())
dq = deque()
dq.append((N, 0))
prev_path_cnt = 0
record = 0

while dq:

    cur_p, path_cnt = dq.popleft()
    if prev_path_cnt + 1 == path_cnt:  # 바뀌는 지점 (이전것들 집계하고 넘어가야 한다)
        if record > 0:
            break

    prev_path_cnt = path_cnt  # 통과하면 최신화

    if cur_p == K:
        record += 1

    # 3가지 선택이 있음
    for next in (cur_p + 1, cur_p - 1, cur_p * 2):
        if 0 <= next <= 100000:
            dq.append((next, path_cnt + 1))

# 현재 상황 출력
print(prev_path_cnt)
print(record)
