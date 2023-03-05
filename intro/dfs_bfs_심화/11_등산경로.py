import sys

sys.stdin = open("input_11.txt")


def judge_available(post_position, prev_position):
    # 초과할 경우
    if post_position[0] >= N or post_position[0] < 0:
        return False
    if post_position[1] >= N or post_position[1] < 0:
        return False
    # 현재값보다 작을 경우
    if mountains[post_position[0]][post_position[1]] <= mountains[prev_position[0]][prev_position[1]]:
        return False
    return True


def DFS(position):
    global cnt
    if position == end:
        cnt += 1
        return
    else:
        for k in range(4):
            mi = position[0] + di[k]
            mj = position[1] + dj[k]
            if judge_available((mi, mj), position):
                DFS((mi, mj))


T = int(input())

for _ in range(T):
    N = int(input())
    mountains = [list(map(int, input().split())) for _ in range(N)]
    start = (0, 0)
    end = (0, 0)
    max = mountains[0][0]
    min = mountains[0][0]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    cnt = 0

    for i in range(N):
        for j in range(N):
            if max < mountains[i][j]:
                max = mountains[i][j]
                end = (i, j)
            if min > mountains[i][j]:
                min = mountains[i][j]
                start = (i, j)
    DFS(start)
    print(cnt)