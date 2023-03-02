import sys
from collections import deque

sys.stdin = open("input_7.txt")

T = int(input())

for _ in range(T):

    pos, find = map(int, input().split())
    positions = [0] * 10000
    cnt_pos = [0] * 10000
    positions[pos] = 1
    cnt_pos[pos] = 0  # cnt_pos 란 그 포지션까지 가기 위해 돌린 cnt 값
    # Searching 할 이진 트리를 root node ~ depth 순서대로 넣기 시작한다
    dq = deque()
    dq.append(pos)  # Root Node
    while dq:
        now = dq.popleft()  # 1에대하여 판별한다 (자기가 갈 수 있는 경로를 탐색한다)
        if now == find:
            break
        for next in (now - 1, now + 1, now + 5):  # 탐색 행위
            if 0 < next < 10000:
                if positions[next] != 1:
                    dq.append(next)
                    positions[next] = 1
                    cnt_pos[next] = cnt_pos[now] + 1
    print(cnt_pos[find])
