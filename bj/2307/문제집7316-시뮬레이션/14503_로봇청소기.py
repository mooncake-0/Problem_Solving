'''
S : 12: 57
E :  1 :45 (50분..?) 실수 디버깅하는데 한 10 분 잡아먹은거 버려도 40분
'''

import sys
from collections import deque

sys.stdin = open("input_14503.txt")
input = sys.stdin.readline

'''
실수 줄이기
하란대로 잘 짜기
별로 포인트가 없는 단순 구현문제
실버 수준의 DFS 문제인듯
'''

# N, M 3 ~ 50

I, J = map(int, input().split())
ii, ij, dir = map(int, input().split())  # d 는 북동남서 순으로 0,1,2,3
room = [list(map(int, input().split())) for _ in range(I)]

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
d_vector = {0: [(-1, 0), (1, 0)], 1: [(0, 1), (0, -1)], 2: [(1, 0), (-1, 0)], 3: [(0, -1), (0, 1)]}  # 북동남서의 방향벡터


def pro1():
    global room
    dq = deque()
    dq.append((ii, ij))

    while dq:

        cur_position = dq.popleft()
        # 0 은 청소 안됨, # 2는 청소됨, # 1은 벽
        if room[cur_position[0]][cur_position[1]] == 0:
            room[cur_position[0]][cur_position[1]] = 2


def judge_next(cur_position):
    global dir
    dir = dir - 1
    if dir == -1:
        dir = 3
    mi, mj = cur_position[0] + d_vector[dir][0][0], cur_position[1] + d_vector[dir][0][1]
    if room[mi][mj] == 0:  # 해당 방을 청소할 수 있다
        dfs((mi, mj))
    else:
        judge_next(cur_position)


def dfs(cur_position):
    global room
    # 현재 방 청소
    if room[cur_position[0]][cur_position[1]] == 0:
        room[cur_position[0]][cur_position[1]] = 2
    exists = False
    for k in range(4):
        mi = cur_position[0] + di[k]
        mj = cur_position[1] + dj[k]
        if room[mi][mj] == 0:
            exists = True
            break

    if exists:  # 청소할 곳이 있다면
        judge_next(cur_position)

    else:  # 청소할 곳이 없다면
        back_vector = d_vector[dir][1]  # 후진 방향
        mi, mj = cur_position[0] + back_vector[0], cur_position[1] + back_vector[1]
        if room[mi][mj] == 2:
            dfs((mi, mj))


# DFS 가 맞는 것 같아서 방향을 튼다
def pro2():
    dfs((ii, ij))  # id
    cnt = 0
    for x in room:
        # print(x)
        for j in x:
            if j == 2:
                cnt += 1
    print(cnt)


def main():
    pro2()


main()
