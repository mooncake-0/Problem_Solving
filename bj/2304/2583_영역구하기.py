import sys

sys.stdin = open("input_2583.txt")
input = sys.stdin.readline
### Recursion Error ~~ Memory Error 사이를 왓다갔다 하면 이거 10000정도로 조절해보면 됨
### 기본 값이 1000이기 때문
sys.setrecursionlimit(10000)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def judge_available(position):
    global I, J
    if position[0] < 0 or position[0] >= I:
        return False
    if position[1] < 0 or position[1] >= J:
        return False
    if plate[position[0]][position[1]] == 1:
        return False
    return True


def dfs(position):
    global plate, cnt
    # position 탐색했음 표시
    plate[position[0]][position[1]] = 1
    cnt += 1
    for m in range(0, 4):
        mi = position[0] + di[m]
        mj = position[1] + dj[m]
        if judge_available((mi, mj)):
            dfs((mi, mj))


# 모양만 유지되는거면 그림이 뒤집혀도 큰 상관 없음. 그대로 I,J 좌표계로 도입
def main():
    global plate, cnt, I, J
    I, J, D = map(int, input().split())
    plate = [[0] * J for _ in range(I)]
    coords = [list(map(int, input().split())) for _ in range(D)]
    for coord in coords:
        j1, i1, j2, i2 = coord[0], coord[1], coord[2], coord[3]
        # 이 구간의 모든 지점들을 1로 만든다
        # 한 칸씩 줄기 때문에, j2, i2 는 1 씩 뺀 상태로 색칠시킨다
        for ii in range(i1, i2):
            for jj in range(j1, j2):
                plate[ii][jj] = 1

    empty_blocks = []
    for i in range(I):
        for j in range(J):
            if plate[i][j] == 0:
                cnt = 0
                dfs((i, j))
                empty_blocks.append(cnt)
    empty_blocks.sort()
    print(len(empty_blocks))
    print(*empty_blocks)


main()
