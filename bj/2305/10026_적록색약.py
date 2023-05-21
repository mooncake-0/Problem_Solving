import copy
import sys

sys.setrecursionlimit(10000)
sys.stdin = open("input_10026.txt")
input = sys.stdin.readline

N = int(input())
drawing = [list(map(str, input().strip())) for _ in range(N)]
drawing2 = copy.deepcopy(drawing)

for i in range(N):
    for j in range(N):
        if drawing2[i][j] == 'G':
            drawing2[i][j] = 'R'

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


def DFS(position, evaluator, is_normal):
    global visited
    for i in range(4):
        mi = di[i] + position[0]
        mj = dj[i] + position[1]
        if 0 <= mi < N and 0 <= mj < N and visited[mi][mj] == 0:
            if is_normal:
                if drawing[mi][mj] == evaluator:
                    visited[mi][mj] = 1
                    DFS((mi, mj), evaluator, is_normal)
            else:
                if drawing2[mi][mj] == evaluator:
                    visited[mi][mj] = 1
                    DFS((mi, mj), evaluator, is_normal)


# 일반사람들이 봤을 떄
def pro1(is_normal):
    global visited
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 1:  # 들어간다
                visited[i][j] = 1
                cnt += 1
                if is_normal:
                    DFS((i, j), drawing[i][j], is_normal)
                else:
                    DFS((i, j), drawing2[i][j], is_normal)
    return cnt


def main():
    a = pro1(True)
    b = pro1(False)
    print(a,b)


main()
