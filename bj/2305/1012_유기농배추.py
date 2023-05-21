import sys

sys.stdin = open("input_1012.txt")
input = sys.stdin.readline
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


# 지렁이가 할당되는 영역을 다 0 으로 만들어준다
def DFS(position):
    for i in range(4):
        mi = position[0] + di[i]
        mj = position[1] + dj[i]
        if 0 <= mi < I and 0 <= mj < J and farm[mi][mj] == 1:
            farm[mi][mj] = 0
            DFS((mi, mj))


def pro1():
    cnt = 0
    for i in range(I):
        for j in range(J):
            if farm[i][j] == 1:
                cnt += 1
                DFS((i, j))
    print(cnt)


TC = int(input())

for _ in range(TC):
    J, I, cab_cnt = map(int, input().split())
    farm = [[0] * J for _ in range(I)]

    for _ in range(cab_cnt):
        a, b = map(int, input().split())
        farm[b][a] = 1

    pro1()
