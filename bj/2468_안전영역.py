import sys

sys.stdin = open("input_2468txt")

sys.setrecursionlimit(10 ** 6)


def judge_safe(i, j):
    if i < 0 or i >= N or j < 0 or j >= N:  # 판별 불필요
        return False
    if checker[i][j] == -1:  # 이미 지난 안전영역
        return False
    if area[i][j] <= rain_height:
        return False
    return True


def paint(checker):
    for x in checker:
        print(x)


# 해당 포지션을 판별하고, 주변에도 안전지역이 있는지를 판별한다
def DFS(i, j):
    checker[i][j] = -1
    # paint(checker)
    # print(rain_height, "-------------------------------------------------------")
    for k in range(4):
        mi = i + di[k]
        mj = j + dj[k]
        if judge_safe(mi, mj):
            DFS(mi, mj)


T = int(input())
#
for _ in range(T):
    N = int(input())
    area = []
    highest = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        if highest < max(tmp):
            highest = max(tmp)
        area.append(tmp)

    max_area = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 범위 i = lowest + 1 <= i < highest 까지 돌거임 # 이게 아닌 이유 --> "아무 지역도 물에 잠기지 않을 수도 있다" 라는 멘트 때문 --> 꼭 최소부터 시작할 필요가 없음.
    for rain_height in range(highest):
        cnt = 0
        #  체킹용을 계속 만들어서 사용하고 버린다 (deepcopy 같은거는 메모리 사용량이 큼, 뭐 사실 쓰면 안되는건 아닌데 지양하는게 좋을 듯)
        checker = [[0] * N for _ in range(N)]
        # rain_height가 지정되고, 각 rain_height 이하인 모든 곳이 잠긴다. 일 경우 안전지역의 갯수를 판별하라
        for i in range(N):
            for j in range(N):
                if checker[i][j] != -1 and area[i][j] > rain_height:
                    cnt += 1
                    DFS(i, j)
        if max_area < cnt:
            max_area = cnt
    print(max_area)