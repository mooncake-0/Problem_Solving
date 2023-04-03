import sys
from collections import deque

sys.stdin = open("input_26.txt")
input = sys.stdin.readline

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def judge_available(position):
    if position[0] < 0 or position[0] >= I:
        return False
    if position[1] < 0 or position[1] >= J:
        return False
    if place[position[0]][position[1]] == '0':
        return False
    return True


def main():
    global I, J, place
    J, I = map(int, input().split())

    # map 은 100 * 100 으로, 이중배열로 충분
    place = [list(map(str, input().strip())) for _ in range(I)]

    ir_j, ir_i = map(int, input().split())
    irradiate = (ir_i - 1, ir_j - 1)

    time = 0

    dq = deque()
    dq.append((irradiate, time))
    place[irradiate[0]][irradiate[1]] = "0"

    while dq:

        position, time = dq.popleft()
        for k in range(4):
            mi = di[k] + position[0]
            mj = dj[k] + position[1]
            if judge_available((mi, mj)):
                dq.append(((mi, mj), time + 1))
                place[mi][mj] = "0"

    survival = 0

    for i in range(I):
        for j in range(J):
            if place[i][j] == "1":
                survival += 1
    print(time + 3)
    print(survival)


main()
