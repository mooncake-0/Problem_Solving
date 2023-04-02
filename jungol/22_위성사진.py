import sys

sys.stdin = open("input_22.txt")
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def judge_available(position):
    global I, J
    if position[0] >= I or position[0] < 0:
        return False
    if position[1] >= J or position[1] < 0:
        return False
    if farm[position[0]][position[1]] == '.':
        return False
    return True


def dfs(position):
    global farm, cnt
    cnt += 1
    farm[position[0]][position[1]] = '.'
    for i in range(4):
        mi = position[0] + di[i]
        mj = position[1] + dj[i]
        if judge_available((mi, mj)):
            dfs((mi, mj))


def main():
    global I, J, farm, cnt
    J, I = map(int, input().split())
    farm = [list(map(str, input().strip())) for _ in range(I)]
    max_val = 0
    for i in range(I):
        for j in range(J):
            if farm[i][j] == '*':
                cnt = 0
                dfs((i, j))
                max_val = max(cnt, max_val)
    print(max_val)


main()
