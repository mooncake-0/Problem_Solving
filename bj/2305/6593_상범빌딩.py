import sys
from collections import deque

sys.stdin = open("input_6593.txt")
input = sys.stdin.readline

dz, di, dj = [0, 0, 0, 0, 1, -1], [0, 1, 0, -1, 0, 0], [1, 0, -1, 0, 0, 0]


def bfs(cur_pos, exit_pos):
    global tower

    dq = deque()
    dq.append((cur_pos, 0))
    tower[cur_pos[0]][cur_pos[1]][cur_pos[2]] = "#"

    while dq:
        pos, times = dq.popleft()

        if pos == exit_pos:
            return times

        for i in range(6):
            mz = pos[0] + dz[i]
            mi = pos[1] + di[i]
            mj = pos[2] + dj[i]
            if 0 <= mz < L and 0 <= mi < R and 0 <= mj < C and (tower[mz][mi][mj] == "." or tower[mz][mi][mj] == "E"):
                tower[mz][mi][mj] = "#"  # 더이상 못 움직이게 바꾼다
                dq.append(((mz, mi, mj), times + 1))
    # 끝까지 못탈출하면
    return -1


def main():
    global L, R, C, tower
    while True:
        L, R, C = map(int, input().split())
        if L == 0 and R == 0 and C == 0:
            break

        # L 번 동안 I = R, J = C 인 것들이 나올 것임을 명시 # L번 = z 축
        tower = []
        for z in range(L):
            tmp2 = []
            for i in range(R):
                tmp = list(map(str, input().strip()))
                for j in range(C):
                    if tmp[j] == "S":
                        cur_pos = (z, i, j)
                    if tmp[j] == "E":
                        exit_pos = (z, i, j)
                tmp2.append(tmp)
            tower.append(tmp2)
            a = input()  # 공백값 제거
        result = bfs(cur_pos, exit_pos)
        if result == -1:
            print("Trapped!")
        else:
            print("Escaped in " + str(result) + " minute(s).")


main()
