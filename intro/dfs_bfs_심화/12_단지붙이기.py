import sys

sys.stdin = open("input_12.txt")


def judge_available(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:
        return False
    if town[i][j] == 0:
        return False
    return True


def paint():
    for x in town:
        print(x)
    print("===============================")


def DFS(i, j):
    global cnt
    # 어쨌든 여기에는 왔음
    town[i][j] = 0
    cnt += 1
    for k in range(4):
        mi = i + di[k]
        mj = j + dj[k]
        if judge_available(mi, mj):  # 갈 수 있는 위치를 판별해봄
            # 갈 수 있으면 간다
            # paint()
            DFS(mi, mj)


T = int(input())

for _ in range(T):
    N = int(input())
    town = [list(map(int, input())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # paint()
    cnt_towns = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            if town[i][j] == 1:
                DFS(i, j)
                cnt_towns.append(cnt)

    cnt_towns.sort()
    print(len(cnt_towns))
    for x in cnt_towns:
        print(x)

    # 0 에서 시작해서 탐색을 시작.
    # 1을 발견하면 그 1을 토대로 DFS 를 시작한다
    # 결과적으로 다 0으로 바꾼 다음에, 다시 전체적으로 탐색을 진행한다
    # 즉 탐색하면서 1을 발견할 때마다 DFS를 조지는 것
