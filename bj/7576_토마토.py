import sys, time
from collections import deque

sys.stdin = open("input_7576.txt")


def judge_available(position):
    i = position[0]
    j = position[1]
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    if box[i][j] != 0:  # 익은 녀석이거나 빈 곳이면 익을 수가 없음
        return False
    return True


T = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for _ in range(T):
    m, n = map(int, input().split())

    # start = time.time()

    box = []
    days = 0
    dq = deque()
    needs_to_rot = 0

    box = [list(map(int, input().split())) for _ in range(n)]

    # 처음 발견되는 1 을 append 해서 사용한다
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                dq.append((i, j))
            elif box[i][j] == 0:
                needs_to_rot += 1

    bfs_depth = 0
    leg_size = len(dq)

    while dq:
        cur_pos = dq.popleft()
        leg_size -= 1

        for k in range(4):
            mi = cur_pos[0] + di[k]
            mj = cur_pos[1] + dj[k]
            if judge_available((mi, mj)):
                # 들어갔을 때 익은 상태로 보내야 한다. 왜냐하면 넣은거 자체가 이미 돌릴 것이란 뜻이고, 이 때 익히지 않으면 다른 인접 노드에서 넣을 수 있기 때문임
                dq.append((mi, mj))
                box[mi][mj] = 1
                needs_to_rot -= 1

        # 다 판별했을 때, leg_size == 0 일 경우, queue 에 있는 것들은 다음 다리들 뿐이다
        if leg_size == 0:
            leg_size = len(dq)
            bfs_depth += 1

    # print("time : ", time.time() - start)

    # 마지막 탈출할 때도 +1 을 하므로, -1 해준다.
    if needs_to_rot == 0:
        print(bfs_depth - 1)
    else:
        print(-1)
