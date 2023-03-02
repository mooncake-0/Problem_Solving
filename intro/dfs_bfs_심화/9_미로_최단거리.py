import sys
from collections import deque


def judge_available(mx, my):
    if mx < 0 or mx > 6:
        return False
    if my < 0 or my > 6:
        return False
    if maze[mx][my] == 1:
        return False
    return True


sys.stdin = open("input_9.txt")

# 7*7 격좌판
# (1,1) 에서 출발, (7,7)에서 엔딩
# 갈 수 있는 방법 수 구하기
T = int(input())
for _ in range(T):
    maze = [list(map(int, input().split())) for _ in range(7)]
    distance_counter = [[0] * 7 for _ in range(7)]

    # 동남서북으로 탐색하기 위한 list
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()
    dq.append((0, 0))  # 튜플 형태로 좌표를 추가한다
    maze[0][0] = 1  # 지난 곳을 벽으로 만들어 버린다
    while dq:
        cur_pos = dq.popleft()

        for i in range(4):
            mx = cur_pos[0] + dx[i]
            my = cur_pos[1] + dy[i]
            if judge_available(mx, my):
                maze[mx][my] = 1  # 이동함.
                dq.append((mx, my))
                distance_counter[mx][my] = distance_counter[cur_pos[0]][cur_pos[1]] + 1

    print(distance_counter[6][6])
    # BFS 설계 방식
    # > 1. while queue 뼈대
    # > 2. 현재 노드를 뺴고, 그 노드에서 하는 일을 수행
    # > 3. 하는 일 수행 후, 다음 노드로 들어올 수 있는 노드들을 탐색하고, queue 에 밀어 넣는다
