import sys
from collections import deque

sys.stdin = open("input_13.txt")


def judge_available(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    if total_map[i][j] == 0:
        return False
    return True


def paint():
    for x in total_map:
        print(x)
    print("===============================")


T = int(input())

for _ in range(T):
    N = int(input())
    total_map = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 이번엔 대각선까지 판단해야한다
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    for i in range(N):
        for j in range(N):
            if total_map[i][j] == 1:  # 1을 발견하면 탐색하기 시작한다
                cnt += 1
                dq = deque()
                dq.append((i, j))  # 포지션을 추가한다
                while dq:
                    ci, cj = dq.popleft()
                    total_map[ci][cj] = 0  # 지난게 맞으니까 일단 0으로 바꾼다
                    # paint()
                    # print(cnt)
                    for k in range(8):
                        mi = ci + di[k]
                        mj = cj + dj[k]
                        if judge_available(mi, mj):
                            dq.append((mi, mj))

    print(cnt)
