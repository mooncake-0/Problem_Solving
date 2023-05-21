import sys
from collections import deque

sys.stdin = open("input_7569.txt")
input = sys.stdin.readline


# 100 * 100 * 100 = 1,000,000
J, I, H = map(int, input().split())


# 1 은 익은 토마토, 0 은 익지 않은 토마토, -1 은 들어있지 않은 칸
# (i,j,z) 를 판단하고, 나머지는 BFS 를 돌리는게 좋을 듯
# H 만큼씩 읽으면서 몇 z 인지 판단할 수 있음
tomatoes = []
riped = deque()
not_ripe_cnt = 0
for z in range(H):  # 2번 동안 I를 돌 것이다
    tmp = []
    for i in range(I):
        tmp2 = list(map(int, input().split()))
        for j in range(J):
            # 익은 토마토의 위치를 파악한다
            if tmp2[j] == 1:
                riped.append(((i, j, z), 0))
            if tmp2[j] == 0:
                not_ripe_cnt += 1
        tmp.append(tmp2)
    tomatoes.append(tmp)

di, dj, dz = [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0], [0, 0, 0, 0, 1, -1]

def print_tom(days):
    print(days)
    for z in range(H):
        for i in range(I):
            print(tomatoes[z][i])

    print("================================")


while riped:
    # 현재 riped 안에 있는 갯수를 파악하고, 이게 다 돌면 다음으로 간다
    position, days = riped.popleft()
    # print_tom(days)

    for i in range(6):
        mi = position[0] + di[i]
        mj = position[1] + dj[i]
        mz = position[2] + dz[i]
        if 0 <= mi < I and 0 <= mj < J and 0 <= mz < H and tomatoes[mz][mi][mj] == 0:
            riped.append(((mi,mj,mz), days+1))
            tomatoes[mz][mi][mj] = 1
            not_ripe_cnt -= 1

# BFS 가 끝난 뒤 nrc 가 0 이 아니면 -1 이다
if not_ripe_cnt > 0:
    print(-1)
elif not_ripe_cnt == 0:
    print(days)
else:
    print("??")