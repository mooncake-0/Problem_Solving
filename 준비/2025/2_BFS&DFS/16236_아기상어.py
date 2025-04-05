'''
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
- 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
----거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
---- 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
'''

import sys
from collections import deque

sys.stdin = open("input_16236.txt")
input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
# 이런건 별로 안중요함.. 그냥 간결하게 짜는게 나음 N이 20 이 최대인데..
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            cur_pos = (i, j)
            sea[i][j] = 0  # cur_pos 만 있으면 됨

cur_size = 2
path_cnt = 0

di, dj = [-1, 0, 1, 0], [0, -1, 0, 1]


# 체크할 사항 (사실상 구현 문제, 메모리 최대한 안쓰는게 중요해보임)
# 1 -> BFS 를 돌면서, 가장 가까운걸 체크할 수 있다. 가장 가까운 "먹을 수 있는 물고기"를 확인 후 먹는다 = 그 위치로 이동
##  사이즈는 상관 없다. 먹을 수 있으면 가장 가까운걸 먹으러 이동한다 (따라서 BFS 안에서 먹을 수 있는거로 판별난다면 BFS 는 종료되어도 된다)
##  BFS 는 위쪽을 우선, 그리고 그 이후 왼쪽을 먼저 돌린다
# 2 -> 먹을 때마다 현재 먹은 갯수를 체크하며 자신 크기만큼 먹었으면 size 증가
# 3 -> 한번 먹은 이후 다시 BFS 를 돌면서 판단한다
# 4 -> 판단하는데 먹을게 없을 때 (다 자신보다 크거나, 이제 그냥 없음) -> 종료

def get_my_fish(candidates):  # 후보군 안에서 가장 적합한 pos 를 반환한다
    # i 가 작을수록 먹힌다. 동일한 i 중엔 j가 작을수록 먹힌ㄷ
    for idx in range(len(candidates)):
        candidates.sort(key=lambda x: (x[0], x[1]))
    return candidates[0]


def bfs(cp):  # 돌리고, 완료 or 없으면 종료 (먹음 완료면 True, 없음이면 False)
    global path_cnt, visited, cur_pos
    dq = deque()
    dq.append((cp, 0))
    prev_path_cnt = 0
    candidates = []
    while dq:

        pos, cur_path_cnt = dq.popleft()
        # path 에 대한 정보를 보관하다가, 1순위가 선정된다면 그 친구를 먹는다
        # candidates 에 보관중이였다고 하자
        # 하지만 지금 pop 된 애가 후보일 수도 있다
        if cur_path_cnt == prev_path_cnt + 1:  # 저번 라운딩에서 갈 후보를 골라야 함
            if candidates:  # 들어있으면 여기서 골라지는거임 # prev_path_cnt 에서 골라진다
                tg = get_my_fish(candidates)
                path_cnt += prev_path_cnt
                sea[tg[0]][tg[1]] = 0  # 먹힌 녀석
                cur_pos = tg
                return True
            else:  # 그냥 최신화 하면 됨 # 후보가 맞는지는 봐야 한다
                prev_path_cnt = cur_path_cnt

        # 현재 포지션에 물고기가 있고, 먹을 수 있는게 발견이면 candidates 에 추가한다
        if sea[pos[0]][pos[1]] != 0 and sea[pos[0]][pos[1]] < cur_size:
            candidates.append(pos)

        for k in range(4):
            mi, mj = pos[0] + di[k], pos[1] + dj[k]
            if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] != 1 and sea[mi][mj] <= cur_size:  # 사이즈가 나랑 같거나 작아야 한다
                visited[mi][mj] = 1
                dq.append(((mi, mj), cur_path_cnt + 1))

    # 마지막에 candidates 를 확인해봤을 때 아무것도 없으면 False 반환
    if not candidates:
        return False
    else:
        tg = get_my_fish(candidates)
        path_cnt += prev_path_cnt
        sea[tg[0]][tg[1]] = 0  # 먹힌 녀석
        cur_pos = tg
        return True

def main():  # 현재 위치로 부터 bfs 함수를 게속 trigger 한다
    global cur_size, visited
    eaten = 0
    visited = [[0] * N for _ in range(N)]
    while True:  # True 면 이미 먹고 온거임
        # 먹은 갯수 체크 해준다
        visited[cur_pos[0]][cur_pos[1]] = 1

        if not bfs(cur_pos):
            break
        eaten += 1
        if eaten == cur_size:  # 도달할 경우
            cur_size += 1
            eaten = 0  # 다시 초기화
        # visited 초기화 (계속 선언시 메모리 초과)
        for i in range(N):
            for j in range(N):
                visited[i][j] = 0
    print(path_cnt)  # 탈출시 False 인 것. 종료


main()
